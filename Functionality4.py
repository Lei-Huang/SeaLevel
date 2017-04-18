import pandas as pd
import os


class Queue:
    """A class designed for holding elements prior to processing.

    Attributes:
        items: A list which holds elements in order.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        if not self.items.__contains__(item):
            self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def fourth_level_functionality(file_path, sea_level=0):
    """Fourth level functionality.

    The program computes the number of separate connected land areas (islands)
    within the area covered by the data file at given sea level.

    Args:
        file_path: A string stands for the path of given file.
                The program will determine whether it is valid or not.
        sea_level: A float number stands for the expected sea level.
                The default value is 0.

    Returns:
        count: An int stands for the number of islands in given sea level.

    """

    # Judge whether the import file path exist or not
    if not os.path.exists(file_path):
        return print("Wrong file path!")

    # Judge whether the import spacing is valid(>0) or not
    if sea_level < 0:
        return print("Please enter a sea level above or equal to 0.")

    # Read the file
    df = pd.read_csv(file_path, header=None, sep=' ')

    # Judge whether the file is suitable for YXZ format or not.
    if df.empty or not len(df.columns) == 3:
        return print('Input file does not match the YXZ format')

    # Judge whether the file is out of bound or not.
    if min(df[0]) < -45 or max(df[0]) > -8 or max(df[1]) > 155 or min(df[1]) < 110:
        return print('Input file has wrong data which is out of the boundary of Australia')

    df[3] = df[2] > 0
    lon = set(df[0])    # A set of longitudes
    lat = set(df[1])    # A set of latitudes
    grid = df[3].values.reshape(len(lon), len(lat))
    # 2d array which store the boolean values if whether the point is above sea level

    index1, row = 0, grid.shape[0]
    index2, col = 0, grid.shape[1]
    count = 0   # Parameter stores the number of islands.

    # The following codes represents the scanning process for all points in the grid.
    # Once the value at the point is true, which means it is above given sea level, it will
    # call breathe_first_search function, which will eliminate all points in this island
    # (turn them into False) and the count will increment by 1.
    # At the end of process, all land will be eliminate from the map and it will count how many
    # islands have been eliminated from the map.

    while index1 < row:
        index2 = 0
        while index2 < col:
            if grid[index1, index2]:
                breathe_first_search(grid, index1, index2)
                count += 1
            index2 += 1
        index1 += 1

    if count > 0:
        print("There are "+str(count)+" islands if sea level raise by "+str(sea_level)+" meters.")
    else:
        print("There is " + str(count) + " island if sea level raise by" + str(sea_level) + " meters.")

    return count


def breathe_first_search(grid, x, y):
    """ Function to eliminate the island from the given point.

        The program computes the number of separate connected land areas (islands)
        within the area covered by the data file at given sea level.
        The function implements the idea of breathe first search.

        Args:
            grid: A numpy 2d array with boolean type which stands for the current map.
                    True means this point is above given sea level, which is land.
                    False means this point is below given sea level, which is sea.
            x: An index stands for the horizontal location of point in Cartesian coordinate
            y: An index stands for the vertical location of point in Cartesian coordinate

        Returns:
            None
    """

    q = Queue()  # Create a new queue
    q.enqueue((x, y))  # Add the starting point into queue
    grid[x, y] = False  # Eliminate starting point from the map.
    while not q.isEmpty():
        current = q.dequeue()  # Pop out the first point in the queue
        nodes = get_neighbours(grid, current[0], current[1])  # Get all adjacent points
        for n in nodes:
            if grid[n[0], n[1]]:  # If the adjacent point is above given sea level.
                grid[n[0], n[1]] = False  # Eliminate this point from the map.
                q.enqueue(n)  # Add the point into queue


def get_neighbours(grid, x, y):
    """ Function to find adjacent points from the given point.

        The function will find all adjacent points in all directions,
        either vertically, horizontally, or diagonally and exclude the points
        which is out of boundary.

        Args:
            grid: A numpy 2d array with boolean type which stands for the current map.
                True means this point is above given sea level, which is land.
                False means this point is below given sea level, which is sea.
            x: An index stands for the horizontal location of point in Cartesian coordinate
            y: An index stands for the vertical location of point in Cartesian coordinate

        Returns:
            output: A list holds the adjacent points in the form of tuples.
    """

    nearby = [(x, y - 1), (x, y + 1),  # Points at left and right
              (x - 1, y), (x + 1, y),  # Points at bottom and top
              (x + 1, y + 1), (x - 1, y - 1),  # Points at right top and left bottom
              (x + 1, y - 1), (x - 1, y + 1)]  # Points at right bottom and left top
    output = []  # The list that stores results
    for i in nearby:
        if not(i[0] < 0  # Points out of left boundary
               or i[1] < 0  # Points out of top boundary
               or i[0] >= grid.shape[0]  # Points out of right boundary
               or i[1] >= grid.shape[1]):  # Points out of bottom boundary
            output.append(i)
    return output

# test cases:

# fourth_level_functionality("sydney250m.txt", 10)
# fourth_level_functionality("tas2k.txt", 0)
# fourth_level_functionality("southcoast1k.txt", 5)
# fourth_level_functionality("au10k.txt", 10)
# fourth_level_functionality("tas1k.txt", 0)
# fourth_level_functionality("southcoast250m.txt", 20)
