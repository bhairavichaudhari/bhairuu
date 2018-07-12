Welcome to Canopy's interactive data-analysis environment!

Kernel running in the 'User' environment.

Pylab is active using TkAgg.

Python 3.5.2 |Enthought, Inc. (x86_64)| (default, Mar  3 2017, 18:53:01) 
Type "copyright", "credits" or "license" for more information.

IPython 5.6.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

import pandas as pd

ds=pd.read_csv("Game_medal.csv",encoding="ISO-8859-1")

ds.head()
Out[12]: 
     City  Edition     Sport Discipline             Athlete  NOC Gender  \
0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men   
1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men   
2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men   
3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men   
4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men   

                        Event Event_gender   Medal  
0              100m freestyle            M    Gold  
1              100m freestyle            M  Silver  
2  100m freestyle for sailors            M  Bronze  
3  100m freestyle for sailors            M    Gold  
4  100m freestyle for sailors            M  Silver  

ds.describe()
Out[13]: 
            Edition
count  29216.000000
mean    1967.713171
std       32.406293
min     1896.000000
25%     1948.000000
50%     1976.000000
75%     1996.000000
max     2008.000000

ds.dtypes
Out[14]: 
City            object
Edition          int64
Sport           object
Discipline      object
Athlete         object
NOC             object
Gender          object
Event           object
Event_gender    object
Medal           object
dtype: object

