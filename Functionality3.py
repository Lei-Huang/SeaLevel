import pandas as pd
import math
import matplotlib.pyplot as plt


def third_level_functionality(file_path, L = -1):
    """
    If L is not provided, the program finds the highest elevation in the given data file,
    divides the range from zero to the highest elevation into a suitable number of steps,
    computes the land area above via the elevation steps and reports the answers to the
    user in a 2-D graph.

    If L is provided, on top of previous computation, the program reports the answer,
    expressed in absolute terms and as a percentage of the land area above the current
    sea level, to the user.

    Args:
        file_path: A string stands for the path of given file.
                The program will determine whether it is valid or not.
        L: A float number stands for elevation.

    Returns:
        None: if L is not given.
        area_query_land,query_land_percen*100: if L is given.

        area_query_land stands for the land area above the L level in square kilometers.
        query_land_percent*100 stands for a percentage of the land area above the current sea level
        Land area above L and the percentage of it to the current land area if L is given.

    """
    df = pd.read_csv(file_path, header=None, sep=' ')

    # Verify whether the file is in YXZ format
    if df.empty or not len(df.columns) == 3:
        return print('Input file does not match the YXZ format')

    if min(df[0]) < -45 or max(df[0]) > -8 or max(df[1]) > 155 or min(df[1]) < 110:
        return print('Input file has wrong data which is out of the boundary of Australia')

    # Calculate horizontal and vertical spaces using second approximation
    vertical_space = (max(df[0])-min(df[0]))/(len(set(df[0]))-1)
    vs_km = 40075/360*vertical_space
    horizontal_spacing = (max(df[1])-min(df[1]))/(len(set(df[1]))-1)
    radians = df[0].apply(math.radians)
    cos = radians.apply(math.cos)
    df[3] = 40075/360*horizontal_spacing*cos
    hs_km = df[3].mean()
    df[4] = vs_km*df[3]  # The retangule area each coordinate pair represents

    # Calculating the second functionality using second approximation
    highest_elevation = max(df[2])
    num_current_land = sum(df[2] > 0)
    current_land = sum(df[4])

    if L == -1:
        elevation = []
        land = []
        iter_elevation = highest_elevation

        while iter_elevation > 0:
            elevation.append(iter_elevation)
            land.append(sum(df[2] >= iter_elevation) / num_current_land * current_land)
            iter_elevation -= highest_elevation * 0.01  # Decrement elevation by 1%

        plt.plot(elevation, land)
        plt.xlabel("Sea level increase")
        plt.ylabel("Area above water")
        plt.title("Functionality 2")
        plt.show()

    # First functionality
    area_per_point = vs_km * hs_km
    area_current_land = area_per_point * num_current_land

    query_land_percent = sum(df[2] > L) / num_current_land
    area_query_land = query_land_percent * area_current_land

    if L == -1:
        pass
    else:
        print("Land area above {} meters: {:.0f} square kilometers;"
              "Percentage of the current land area: {:.2f}%"
              .format(L, area_query_land, query_land_percent*100))
        return area_query_land, query_land_percent*100

# test cases:

# third_level_functionality("sydney250m.txt", 5)
# third_level_functionality('au10k.txt', 2)