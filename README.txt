
COMP1730/6730 Programming for Scientists homework assignment Group 18
=====================================================================


This package implements the framework for homework assignment
You can get assignment specification (and learn more about it) at


    https://wattlecourses.anu.edu.au/mod/page/view.php?id=972812


DEVELOPER
=========
Lei Huang 
   u6041747
   arley_huang@163.com


Gabriel Wei Chu 
   u6133110
   wei.g.chu@gmail.com


TEST
=========
These modules have been tested under:
 - Windows 10 (64-bit).
 - Mac OS X El Capitan with Xcode 7.x (64 bit).
 - Python 3.5.2 with Anaconda 4.1.1 (64-bit) (64-bit)


SETUP
=====
    1. Install Python 3


    2. Numpy, Pandas and Matlibplot are packages are required


    3. To install the packages please run pip or employ the off-shelf Anaconda distribution


ABOUT THE CODE
==============
Upon implementation you will have four py scripts: Functionality1.py, Functionality2.py, Functionality3.py and Functionality4.py. Each script can be run independently and self-fulfilling the functionalities list following. 


Functionality:
Functionality1.py: The program reports the answer, expressed in absolute terms and as a percentage of the land area above the current sea level, to the user.


Functionality2.py: The program finds the highest elevation in the given data file, divides the range from zero to the highest elevation into a suitable number of steps, computes the land area above each of them and reports all the answers to the user in a 2-D graph.


Functionality3.py: The programs acheives the same functionality as Functionality1.py and Functionality2.py, with a different approximation method being employed.


Functionality4.py: The program computes the number of separate connected land areas (islands) within the area covered by the data file at given sea level.

Input Requirements:
Functionality1.py: require the user inputs of file_path, vs_km, hs_km and L.
Functionality2.py: require the user inputs of file_path, vs_km and hs_km.
Functionality3.py: require the user inputs of file_path.
Functionality4.py: require the user inputs of file_path and L.


Operation:
import Functionality1.py as first_f
first_f.first_level_functionality(file_path, vs_km, hs_km, L)


import Functionality2.py as second_f
second_f.second_level_functionality(file_path, vs_km, hs_km)


import Functionality3.py as third_f
third_f.third_level_functionality(file_path, L(optional))


import Functionality4.py as fourth_f
fourth_f.fourth_level_functionality(file_path, L(optional))




CONTACT
=======
Please send bug reports, patches, and other feedback to
    arley_huang@163.com
    wei.g.chu@gmail.com