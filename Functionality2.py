import pandas as pd
import matplotlib.pyplot as plt
import os


def second_level_functionality(file_path, vs_km=0, hs_km=0):
    """Second level functionality.

    The program finds the highest elevation in the given data file,
    divides the range from zero to the highest elevation into a suitable number of steps,
    computes the land area above each of them and reports all the answers to the user in
    the form of 2-d graph.

    Args:
        file_path: A string stands for the path of given file.
                The program will determine whether it is valid or not.
        vs_km:A float number stands for vertical spacing.
        hs_km:A float number stands for horizontal spacing.


    Returns:
        None

    """

    # Judge whether the import file path exist or not
    if not os.path.exists(file_path):
        return print("Wrong file path!")

    # Judge whether the import spacing is valid(>0) or not
    if vs_km <= 0 or hs_km <= 0:
        return print("Please provide correct vertical spacing and horizontal spacing.")

    # Read the file
    df = pd.read_csv(file_path, header=None, sep=' ')

    # Judge whether the file is suitable for YXZ format or not.
    if df.empty or not len(df.columns) == 3:
        return print('Input file does not match the YXZ format')

    # Judge whether the file is out of bound or not.
    if min(df[0]) < -45 or max(df[0]) > -8 or max(df[1]) > 155 or min(df[1]) < 110:
        return print('Input file has wrong data which is out of the boundary of Australia')

    highest_elevation = max(df[2])
    num_current_land = sum(df[2] > 0)
    area_per_point = vs_km * hs_km
    current_land = num_current_land * area_per_point

    elevation = []  # List to store all elevation values
    land = []   # List to store all land area values
    iter_elevation = highest_elevation  # Parameter used in following while loop

    while iter_elevation > 0:
        elevation.append(iter_elevation)
        land.append(sum(df[2] >= iter_elevation)/num_current_land*current_land)
        iter_elevation -= highest_elevation*0.01    # Decrement elevation by 1%

    plt.plot(elevation, land)
    plt.xlabel("Sea level increase")
    plt.ylabel("Area above water")
    plt.title("Functionality 2")
    plt.show()
    return None


# test cases:

# second_level_functionality("sydney250m.txt",0.278,0.231)
# second_level_functionality("tas2k.txt",2.22,1.65)