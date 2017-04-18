import pandas as pd
import os


def first_level_functionality(file_path='', vs_km=0, hs_km=0, L=0):
    """
    The program reports the answer, expressed in absolute terms and as
    a percentage of the land area above the current sea level, to the user.

    Args:
        file_path: A string stands for the path of given file.
                The program will determine whether it is valid or not.
        vs_km:A float number stands for vertical spacing in kilometers.
        hs_km:A float number stands for horizontal spacing in kilometers.
        L: A float number stands for elevation.


    Returns:
        area_query_land, query_land_percen*100:
        area_query_land stands for the land area above the L level in square kilometers.
        query_land_percent*100 stands for a percentage of the land area above the current
        sea level.

    """

    # Judge whether the import file path exist or not
    if not os.path.exists(file_path):
        return print("Wrong file path!")

    # Judge whether the import spacing is valid(>0) or not
    if vs_km <= 0 or hs_km <= 0:
        return print("Please provide correct vertical spacing and horizontal spacing.")

    df = pd.read_csv(file_path, header=None, sep=' ')

    # Verify whether the file is in YXZ format
    if df.empty or not len(df.columns) == 3:
        return print('Input file does not match the YXZ format')

    if min(df[0]) < -45 or max(df[0]) > -8 or max(df[1]) > 155 or min(df[1]) < 110:
        return print('Input file has wrong data which is out of the boundary of Australia')

    # Calculate the land area above L
    num_current_land = sum(df[2] > 0)
    area_per_point = vs_km * hs_km
    area_current_land = area_per_point * num_current_land

    query_land_percent = sum(df[2] > L)/num_current_land
    area_query_land = query_land_percent * area_current_land
    print("Land area above {} meters: {:.0f} square kilometers; "
          "Percentage of the current land area: {:.2f}%"
          .format(L, area_query_land, query_land_percent*100))
    return area_query_land, query_land_percent*100

# test cases:

# first_level_functionality("sydney250m.txt",0.278,0.231,10)
# first_level_functionality("tas2k.txt",2.22,1.65)