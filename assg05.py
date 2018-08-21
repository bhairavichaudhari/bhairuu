# -*- coding: utf-8 -*-
import pandas as pd
ds1=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")
ds1.head()
ds1.shape
ds1.info()
ds1.imdb_score.describe()
ds1['movie_title']   # display movie_title column
ds1['duration'][:10]  # First 10 records of duration column
ds1[['budget','gross']] # select multiple columns
ds1[ds1['duration'] > 120] # select movie more than 2 hr duration

### Remove incomplete rows ####
ds1.country=ds1.country.fillna('') # Will put empty string
ds1.duration=ds1.duration.fillna(ds1.duration.mean()) # will put mean value of duration table
ds1.dropna() # Dropping all rows with any NA values 
ds1.dropna(how='all') # drop rows that have all NA values
ds1.dropna(thresh=5) # at least 5 non-null values, and greater than that will be deleted
ds1.dropna(subset=['title_year'])  # don’t want to include any movie that doesn’t have information on when the movie came out

### Deal with error-prone columns ###
### axis=1 for Column and axis=0 for row it is default

ds1.dropna(axis=1, how='all') # drop the columns with that are all NA values
ds1.dropna(axis=1, how='any') # Drop all columns with any NA values







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

ds1=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")

ds1.head()
Out[30]: 
   color      director_name  num_critic_for_reviews  duration  \
0  Color      James Cameron                   723.0     178.0   
1  Color     Gore Verbinski                   302.0     169.0   
2  Color         Sam Mendes                   602.0     148.0   
3  Color  Christopher Nolan                   813.0     164.0   
4    NaN        Doug Walker                     NaN       NaN   

   director_facebook_likes  actor_3_facebook_likes      actor_2_name  \
0                      0.0                   855.0  Joel David Moore   
1                    563.0                  1000.0     Orlando Bloom   
2                      0.0                   161.0      Rory Kinnear   
3                  22000.0                 23000.0    Christian Bale   
4                    131.0                     NaN        Rob Walker   

   actor_1_facebook_likes        gross                           genres  \
0                  1000.0  760505847.0  Action|Adventure|Fantasy|Sci-Fi   
1                 40000.0  309404152.0         Action|Adventure|Fantasy   
2                 11000.0  200074175.0        Action|Adventure|Thriller   
3                 27000.0  448130642.0                  Action|Thriller   
4                   131.0          NaN                      Documentary   

         num_user_for_reviews language  country  content_rating  \
0         ...                        3054.0  English      USA           PG-13   
1         ...                        1238.0  English      USA           PG-13   
2         ...                         994.0  English       UK           PG-13   
3         ...                        2701.0  English      USA           PG-13   
4         ...                           NaN      NaN      NaN             NaN   

        budget  title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0  237000000.0      2009.0                  936.0        7.9          1.78   
1  300000000.0      2007.0                 5000.0        7.1          2.35   
2  245000000.0      2015.0                  393.0        6.8          2.35   
3  250000000.0      2012.0                23000.0        8.5          2.35   
4          NaN         NaN                   12.0        7.1           NaN   

  movie_facebook_likes  
0                33000  
1                    0  
2                85000  
3               164000  
4                    0  

[5 rows x 28 columns]

ds1.shape
Out[31]: (5043, 28)

ds1.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5043 entries, 0 to 5042
Data columns (total 28 columns):
color                        5024 non-null object
director_name                4939 non-null object
num_critic_for_reviews       4993 non-null float64
duration                     5028 non-null float64
director_facebook_likes      4939 non-null float64
actor_3_facebook_likes       5020 non-null float64
actor_2_name                 5030 non-null object
actor_1_facebook_likes       5036 non-null float64
gross                        4159 non-null float64
genres                       5043 non-null object
actor_1_name                 5036 non-null object
movie_title                  5043 non-null object
num_voted_users              5043 non-null int64
cast_total_facebook_likes    5043 non-null int64
actor_3_name                 5020 non-null object
facenumber_in_poster         5030 non-null float64
plot_keywords                4890 non-null object
movie_imdb_link              5043 non-null object
num_user_for_reviews         5022 non-null float64
language                     5031 non-null object
country                      5038 non-null object
content_rating               4740 non-null object
budget                       4551 non-null float64
title_year                   4935 non-null float64
actor_2_facebook_likes       5030 non-null float64
imdb_score                   5043 non-null float64
aspect_ratio                 4714 non-null float64
movie_facebook_likes         5043 non-null int64
dtypes: float64(13), int64(3), object(12)
memory usage: 1.1+ MB

ds1.imdb_score.describe()
Out[33]: 
count    5043.000000
mean        6.442138
std         1.125116
min         1.600000
25%         5.800000
50%         6.600000
75%         7.200000
max         9.500000
Name: imdb_score, dtype: float64

ds1['movie_title']
Out[34]: 
0                                                AvatarÂ 
1              Pirates of the Caribbean: At World's EndÂ 
2                                               SpectreÂ 
3                                 The Dark Knight RisesÂ 
4       Star Wars: Episode VII - The Force AwakensÂ   ...
5                                           John CarterÂ 
6                                          Spider-Man 3Â 
7                                               TangledÂ 
8                               Avengers: Age of UltronÂ 
9                Harry Potter and the Half-Blood PrinceÂ 
10                   Batman v Superman: Dawn of JusticeÂ 
11                                     Superman ReturnsÂ 
12                                    Quantum of SolaceÂ 
13           Pirates of the Caribbean: Dead Man's ChestÂ 
14                                      The Lone RangerÂ 
15                                         Man of SteelÂ 
16             The Chronicles of Narnia: Prince CaspianÂ 
17                                         The AvengersÂ 
18          Pirates of the Caribbean: On Stranger TidesÂ 
19                                       Men in Black 3Â 
20            The Hobbit: The Battle of the Five ArmiesÂ 
21                               The Amazing Spider-ManÂ 
22                                           Robin HoodÂ 
23                  The Hobbit: The Desolation of SmaugÂ 
24                                   The Golden CompassÂ 
25                                            King KongÂ 
26                                              TitanicÂ 
27                           Captain America: Civil WarÂ 
28                                           BattleshipÂ 
29                                       Jurassic WorldÂ 
                       
5013                                             ManitoÂ 
5014                                            RampageÂ 
5015                                            SlackerÂ 
5016                                        Dutch KillsÂ 
5017                                          Dry SpellÂ 
5018                                           FlywheelÂ 
5019                                             ExeterÂ 
5020                                         The RidgesÂ 
5021                                    The Puffy ChairÂ 
5022                               Stories of Our LivesÂ 
5023                                   Breaking UpwardsÂ 
5024                           All Superheroes Must DieÂ 
5025                                     Pink FlamingosÂ 
5026                                              CleanÂ 
5027                                         The CircleÂ 
5028                                        Tin Can ManÂ 
5029                                           The CureÂ 
5030                                     On the DownlowÂ 
5031                       Sanctuary; Quite a ConundrumÂ 
5032                                               BangÂ 
5033                                             PrimerÂ 
5034                                             CaviteÂ 
5035                                        El MariachiÂ 
5036                                    The Mongol KingÂ 
5037                                          NewlywedsÂ 
5038                            Signed Sealed DeliveredÂ 
5039                          The FollowingÂ             
5040                               A Plague So PleasantÂ 
5041                                   Shanghai CallingÂ 
5042                                  My Date with DrewÂ 
Name: movie_title, Length: 5043, dtype: object

ds1['duration'][:10]
Out[35]: 
0    178.0
1    169.0
2    148.0
3    164.0
4      NaN
5    132.0
6    156.0
7    100.0
8    141.0
9    153.0
Name: duration, dtype: float64

ds1[['budget','gross']]
Out[36]: 
           budget        gross
0     237000000.0  760505847.0
1     300000000.0  309404152.0
2     245000000.0  200074175.0
3     250000000.0  448130642.0
4             NaN          NaN
5     263700000.0   73058679.0
6     258000000.0  336530303.0
7     260000000.0  200807262.0
8     250000000.0  458991599.0
9     250000000.0  301956980.0
10    250000000.0  330249062.0
11    209000000.0  200069408.0
12    200000000.0  168368427.0
13    225000000.0  423032628.0
14    215000000.0   89289910.0
15    225000000.0  291021565.0
16    225000000.0  141614023.0
17    220000000.0  623279547.0
18    250000000.0  241063875.0
19    225000000.0  179020854.0
20    250000000.0  255108370.0
21    230000000.0  262030663.0
22    200000000.0  105219735.0
23    225000000.0  258355354.0
24    180000000.0   70083519.0
25    207000000.0  218051260.0
26    200000000.0  658672302.0
27    250000000.0  407197282.0
28    209000000.0   65173160.0
29    150000000.0  652177271.0
          ...          ...
5013      24000.0          NaN
5014          NaN          NaN
5015      23000.0    1227508.0
5016      25000.0          NaN
5017      22000.0          NaN
5018      20000.0          NaN
5019          NaN          NaN
5020      17350.0          NaN
5021      15000.0     192467.0
5022      15000.0          NaN
5023      15000.0      76382.0
5024      20000.0          NaN
5025      10000.0     180483.0
5026       4500.0     136007.0
5027      10000.0     673780.0
5028      10000.0          NaN
5029    1000000.0      94596.0
5030          NaN          NaN
5031     200000.0          NaN
5032          NaN          NaN
5033       7000.0     424760.0
5034       7000.0      70071.0
5035       7000.0    2040920.0
5036       3250.0          NaN
5037       9000.0       4584.0
5038          NaN          NaN
5039          NaN          NaN
5040       1400.0          NaN
5041          NaN      10443.0
5042       1100.0      85222.0

[5043 rows x 2 columns]

ds1[ds1['duration'] > 120]
Out[37]: 
                 color        director_name  num_critic_for_reviews  duration  \
0                Color        James Cameron                   723.0     178.0   
1                Color       Gore Verbinski                   302.0     169.0   
2                Color           Sam Mendes                   602.0     148.0   
3                Color    Christopher Nolan                   813.0     164.0   
5                Color       Andrew Stanton                   462.0     132.0   
6                Color            Sam Raimi                   392.0     156.0   
8                Color          Joss Whedon                   635.0     141.0   
9                Color          David Yates                   375.0     153.0   
10               Color          Zack Snyder                   673.0     183.0   
11               Color         Bryan Singer                   434.0     169.0   
13               Color       Gore Verbinski                   313.0     151.0   
14               Color       Gore Verbinski                   450.0     150.0   
15               Color          Zack Snyder                   733.0     143.0   
16               Color       Andrew Adamson                   258.0     150.0   
17               Color          Joss Whedon                   703.0     173.0   
18               Color         Rob Marshall                   448.0     136.0   
20               Color        Peter Jackson                   422.0     164.0   
21               Color            Marc Webb                   599.0     153.0   
22               Color         Ridley Scott                   343.0     156.0   
23               Color        Peter Jackson                   509.0     186.0   
25               Color        Peter Jackson                   446.0     201.0   
26               Color        James Cameron                   315.0     194.0   
27               Color        Anthony Russo                   516.0     147.0   
28               Color           Peter Berg                   377.0     131.0   
29               Color      Colin Trevorrow                   644.0     124.0   
30               Color           Sam Mendes                   750.0     143.0   
31               Color            Sam Raimi                   300.0     135.0   
32               Color          Shane Black                   608.0     195.0   
36               Color          Michael Bay                   366.0     150.0   
37               Color          Michael Bay                   378.0     165.0   
               ...                  ...                     ...       ...   
4463             Color             Ham Tran                    15.0     135.0   
4468             Color     Sadyk Sher-Niyaz                    16.0     135.0   
4474   Black and White     Alfred Hitchcock                   144.0     130.0   
4483             Color            Spike Lee                    46.0     123.0   
4498             Color         Sergio Leone                   181.0     142.0   
4528             Color          Shimit Amin                    14.0     150.0   
4530             Color     John G. Avildsen                   141.0     145.0   
4533             Color      Tony Richardson                    30.0     121.0   
4550             Color      Martin Scorsese                   129.0     122.0   
4572   Black and White       Khalid Mohamed                     1.0     167.0   
4580             Color        Scandar Copti                   100.0     124.0   
4584             Color        Peter Jackson                   308.0     135.0   
4593             Color      Vivek Agnihotri                     4.0     160.0   
4622             Color    Michael Taliferro                     NaN     138.0   
4659             Color       Asghar Farhadi                   354.0     123.0   
4688             Color          Steve James                    53.0     170.0   
4694             Color        Peter Jackson                   446.0     201.0   
4708             Color     Michael Wadleigh                    53.0     215.0   
4723             Color        Alex Kendrick                    50.0     122.0   
4747   Black and White       Akira Kurosawa                   153.0     202.0   
4763             Color        Daston Kalili                     NaN     127.0   
4768             Color       Georgia Hilton                     1.0     122.0   
4778             Color            Sam Raimi                   525.0     130.0   
4789             Color           Kay Pollak                    34.0     133.0   
4810   Black and White        D.W. Griffith                    69.0     123.0   
4842             Color         Julie Taymor                   156.0     133.0   
4885   Black and White           King Vidor                    48.0     151.0   
4894             Color    Richard Fleischer                    69.0     127.0   
4912   Black and White  Carl Theodor Dreyer                    54.0     126.0   
5020               NaN      Brandon Landers                     NaN     143.0   

      director_facebook_likes  actor_3_facebook_likes          actor_2_name  \
0                         0.0                   855.0      Joel David Moore   
1                       563.0                  1000.0         Orlando Bloom   
2                         0.0                   161.0          Rory Kinnear   
3                     22000.0                 23000.0        Christian Bale   
5                       475.0                   530.0       Samantha Morton   
6                         0.0                  4000.0          James Franco   
8                         0.0                 19000.0     Robert Downey Jr.   
9                       282.0                 10000.0      Daniel Radcliffe   
10                        0.0                  2000.0          Lauren Cohan   
11                        0.0                   903.0         Marlon Brando   
13                      563.0                  1000.0         Orlando Bloom   
14                      563.0                  1000.0           Ruth Wilson   
15                        0.0                   748.0    Christopher Meloni   
16                       80.0                   201.0  Pierfrancesco Favino   
17                        0.0                 19000.0     Robert Downey Jr.   
18                      252.0                  1000.0           Sam Claflin   
20                        0.0                   773.0            Adam Brown   
21                      464.0                   963.0       Andrew Garfield   
22                        0.0                   738.0          William Hurt   
23                        0.0                   773.0            Adam Brown   
25                        0.0                    84.0    Thomas Kretschmann   
26                        0.0                   794.0          Kate Winslet   
27                       94.0                 11000.0    Scarlett Johansson   
28                      532.0                   627.0  Alexander SkarsgÃ¥rd   
29                      365.0                  1000.0            Judy Greer   
30                        0.0                   393.0         Helen McCrory   
31                        0.0                  4000.0          James Franco   
32                     1000.0                  3000.0           Jon Favreau   
36                        0.0                   464.0            Kevin Dunn   
37                        0.0                   808.0          Sophia Myles   
                      ...                     ...                   ...   
4463                      5.0                     5.0            Kieu Chinh   
4468                    135.0                     0.0     Aziz Muradillayev   
4474                  13000.0                   333.0         Joan Fontaine   
4483                      0.0                   161.0         Elvis Nolasco   
4498                      0.0                    24.0        Luigi Pistilli   
4528                      6.0                    20.0      Shazahn Padamsee   
4530                     80.0                   794.0      Burgess Meredith   
4533                     62.0                    69.0         Susannah York   
4550                  17000.0                   184.0        Keith Richards   
4572                     10.0                    97.0        Manoj Bajpayee   
4580                     13.0                     7.0         Scandar Copti   
4584                      0.0                   310.0           AJ Michalka   
4593                      5.0                   219.0           Anil Kapoor   
4622                    105.0                   110.0         Sticky Fingaz   
4659                      0.0                   620.0          Leila Hatami   
4688                     23.0                     2.0           Arthur Agee   
4694                      0.0                    84.0    Thomas Kretschmann   
4708                     14.0                   136.0          Jimi Hendrix   
4723                    589.0                   150.0             Ken Bevel   
4747                      0.0                     4.0         Minoru Chiaki   
4763                      2.0                     0.0         Rai Alexandra   
4768                    406.0                   152.0             Tim Abell   
4778                      0.0                 11000.0            Mila Kunis   
4789                     10.0                    19.0        Frida Hallgren   
4810                    204.0                     9.0             Mae Marsh   
4842                    278.0                   107.0           T.V. Carpio   
4885                     54.0                     6.0        RenÃ©e AdorÃ©e   
4894                    130.0                    51.0       Robert J. Wilke   
4912                    147.0                     0.0      Sylvia Eckhausen   
5020                      8.0                     8.0       Alana Kaniewski   

      actor_1_facebook_likes        gross  \
0                     1000.0  760505847.0   
1                    40000.0  309404152.0   
2                    11000.0  200074175.0   
3                    27000.0  448130642.0   
5                      640.0   73058679.0   
6                    24000.0  336530303.0   
8                    26000.0  458991599.0   
9                    25000.0  301956980.0   
10                   15000.0  330249062.0   
11                   18000.0  200069408.0   
13                   40000.0  423032628.0   
14                   40000.0   89289910.0   
15                   15000.0  291021565.0   
16                   22000.0  141614023.0   
17                   26000.0  623279547.0   
18                   40000.0  241063875.0   
20                    5000.0  255108370.0   
21                   15000.0  262030663.0   
22                     891.0  105219735.0   
23                    5000.0  258355354.0   
25                    6000.0  218051260.0   
26                   29000.0  658672302.0   
27                   21000.0  407197282.0   
28                   14000.0   65173160.0   
29                    3000.0  652177271.0   
30                     883.0  304360277.0   
31                   24000.0  373377893.0   
32                   21000.0  408992272.0   
36                     894.0  402076689.0   
37                     974.0  245428137.0   
                     ...          ...   
4463                    51.0     638951.0   
4468                     0.0          NaN   
4474                  1000.0          NaN   
4483                  3000.0          NaN   
4498                 16000.0    6100000.0   
4528                   964.0          NaN   
4530                 13000.0  117235247.0   
4533                   883.0          NaN   
4550                   543.0    5355376.0   
4572                   353.0     610991.0   
4580                    20.0     621240.0   
4584                   873.0   43982842.0   
4593                   724.0      49000.0   
4622                   592.0          NaN   
4659                   786.0    7098492.0   
4688                     7.0    7830611.0   
4694                  6000.0  218051260.0   
4708                   262.0   13300000.0   
4723                   848.0   33451479.0   
4747                   304.0     269061.0   
4763                     2.0          NaN   
4768                   358.0          NaN   
4778                 44000.0  234903076.0   
4789                   690.0       9910.0   
4810                   436.0          NaN   
4842                  5000.0   24343673.0   
4885                    81.0          NaN   
4894                   618.0          NaN   
4912                     0.0          NaN   
5020                   720.0          NaN   

                                     genres         ...           \
0           Action|Adventure|Fantasy|Sci-Fi         ...            
1                  Action|Adventure|Fantasy         ...            
2                 Action|Adventure|Thriller         ...            
3                           Action|Thriller         ...            
5                   Action|Adventure|Sci-Fi         ...            
6                  Action|Adventure|Romance         ...            
8                   Action|Adventure|Sci-Fi         ...            
9          Adventure|Family|Fantasy|Mystery         ...            
10                  Action|Adventure|Sci-Fi         ...            
11                  Action|Adventure|Sci-Fi         ...            
13                 Action|Adventure|Fantasy         ...            
14                 Action|Adventure|Western         ...            
15          Action|Adventure|Fantasy|Sci-Fi         ...            
16          Action|Adventure|Family|Fantasy         ...            
17                  Action|Adventure|Sci-Fi         ...            
18                 Action|Adventure|Fantasy         ...            
20                        Adventure|Fantasy         ...            
21                 Action|Adventure|Fantasy         ...            
22           Action|Adventure|Drama|History         ...            
23                        Adventure|Fantasy         ...            
25           Action|Adventure|Drama|Romance         ...            
26                            Drama|Romance         ...            
27                  Action|Adventure|Sci-Fi         ...            
28         Action|Adventure|Sci-Fi|Thriller         ...            
29         Action|Adventure|Sci-Fi|Thriller         ...            
30                Action|Adventure|Thriller         ...            
31         Action|Adventure|Fantasy|Romance         ...            
32                  Action|Adventure|Sci-Fi         ...            
36                  Action|Adventure|Sci-Fi         ...            
37                  Action|Adventure|Sci-Fi         ...            
                                    ...         ...            
4463                                  Drama         ...            
4468         Action|Biography|Drama|History         ...            
4474       Drama|Film-Noir|Mystery|Thriller         ...            
4483                Comedy|Romance|Thriller         ...            
4498                                Western         ...            
4528                           Comedy|Drama         ...            
4530                            Drama|Sport         ...            
4533               Adventure|Comedy|History         ...            
4550            Biography|Documentary|Music         ...            
4572                          Drama|Romance         ...            
4580                            Crime|Drama         ...            
4584                 Drama|Fantasy|Thriller         ...            
4593                               Thriller         ...            
4622                           Comedy|Music         ...            
4659                          Drama|Mystery         ...            
4688                Documentary|Drama|Sport         ...            
4694         Action|Adventure|Drama|Romance         ...            
4708              Documentary|History|Music         ...            
4723                          Drama|Romance         ...            
4747                 Action|Adventure|Drama         ...            
4763                               Thriller         ...            
4768                Action|Mystery|Thriller         ...            
4778               Adventure|Family|Fantasy         ...            
4789             Comedy|Drama|Music|Romance         ...            
4810                      Drama|History|War         ...            
4842          Drama|Fantasy|Musical|Romance         ...            
4885                      Drama|Romance|War         ...            
4894  Adventure|Drama|Family|Fantasy|Sci-Fi         ...            
4912                          Drama|Fantasy         ...            
5020                  Drama|Horror|Thriller         ...            

     num_user_for_reviews    language      country  content_rating  \
0                  3054.0     English          USA           PG-13   
1                  1238.0     English          USA           PG-13   
2                   994.0     English           UK           PG-13   
3                  2701.0     English          USA           PG-13   
5                   738.0     English          USA           PG-13   
6                  1902.0     English          USA           PG-13   
8                  1117.0     English          USA           PG-13   
9                   973.0     English           UK              PG   
10                 3018.0     English          USA           PG-13   
11                 2367.0     English          USA           PG-13   
13                 1832.0     English          USA           PG-13   
14                  711.0     English          USA           PG-13   
15                 2536.0     English          USA           PG-13   
16                  438.0     English          USA              PG   
17                 1722.0     English          USA           PG-13   
18                  484.0     English          USA           PG-13   
20                  802.0     English  New Zealand           PG-13   
21                 1225.0     English          USA           PG-13   
22                  546.0     English          USA           PG-13   
23                  951.0     English          USA           PG-13   
25                 2618.0     English  New Zealand           PG-13   
26                 2528.0     English          USA           PG-13   
27                 1022.0     English          USA           PG-13   
28                  751.0     English          USA           PG-13   
29                 1290.0     English          USA           PG-13   
30                 1498.0     English           UK           PG-13   
31                 1303.0     English          USA           PG-13   
32                 1187.0     English          USA           PG-13   
36                 1439.0     English          USA           PG-13   
37                  918.0     English          USA           PG-13   
                  ...         ...          ...             ...   
4463                 19.0  Vietnamese          USA               R   
4468                 24.0     English   Kyrgyzstan           PG-13   
4474                276.0     English          USA       Not Rated   
4483                  9.0     English          USA             NaN   
4498                780.0     Italian        Italy        Approved   
4528                 35.0       Hindi        India             NaN   
4530                542.0     English          USA              PG   
4533                 56.0     English           UK         Unrated   
4550                 67.0     English          USA           PG-13   
4572                 19.0       Hindi        India             NaN   
4580                 32.0      Arabic      Germany             NaN   
4584                593.0     English          USA           PG-13   
4593                 30.0       Hindi        India             NaN   
4622                  1.0     English          USA           PG-13   
4659                264.0     Persian         Iran           PG-13   
4688                 74.0     English          USA           PG-13   
4694               2618.0     English  New Zealand           PG-13   
4708                 63.0     English          USA               R   
4723                215.0     English          USA              PG   
4747                596.0    Japanese        Japan         Unrated   
4763                  3.0     English          USA             NaN   
4768                 16.0     English          USA               R   
4778                511.0     English          USA              PG   
4789                 94.0     Swedish       Sweden             NaN   
4810                 88.0         NaN          USA       Not Rated   
4842                524.0     English          USA           PG-13   
4885                 45.0         NaN          USA       Not Rated   
4894                108.0     English          USA        Approved   
4912                 49.0      Danish      Denmark       Not Rated   
5020                  8.0     English          USA             NaN   

           budget  title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0     237000000.0      2009.0                  936.0        7.9          1.78   
1     300000000.0      2007.0                 5000.0        7.1          2.35   
2     245000000.0      2015.0                  393.0        6.8          2.35   
3     250000000.0      2012.0                23000.0        8.5          2.35   
5     263700000.0      2012.0                  632.0        6.6          2.35   
6     258000000.0      2007.0                11000.0        6.2          2.35   
8     250000000.0      2015.0                21000.0        7.5          2.35   
9     250000000.0      2009.0                11000.0        7.5          2.35   
10    250000000.0      2016.0                 4000.0        6.9          2.35   
11    209000000.0      2006.0                10000.0        6.1          2.35   
13    225000000.0      2006.0                 5000.0        7.3          2.35   
14    215000000.0      2013.0                 2000.0        6.5          2.35   
15    225000000.0      2013.0                 3000.0        7.2          2.35   
16    225000000.0      2008.0                  216.0        6.6          2.35   
17    220000000.0      2012.0                21000.0        8.1          1.85   
18    250000000.0      2011.0                11000.0        6.7          2.35   
20    250000000.0      2014.0                  972.0        7.5          2.35   
21    230000000.0      2012.0                10000.0        7.0          2.35   
22    200000000.0      2010.0                  882.0        6.7          2.35   
23    225000000.0      2013.0                  972.0        7.9          2.35   
25    207000000.0      2005.0                  919.0        7.2          2.35   
26    200000000.0      1997.0                14000.0        7.7          2.35   
27    250000000.0      2016.0                19000.0        8.2          2.35   
28    209000000.0      2012.0                10000.0        5.9          2.35   
29    150000000.0      2015.0                 2000.0        7.0          2.00   
30    200000000.0      2012.0                  563.0        7.8          2.35   
31    200000000.0      2004.0                11000.0        7.3          2.35   
32    200000000.0      2013.0                 4000.0        7.2          2.35   
36    200000000.0      2009.0                  581.0        6.0          2.35   
37    210000000.0      2014.0                  956.0        5.7          2.35   
          ...         ...                    ...        ...           ...   
4463    1592000.0      2006.0                   24.0        7.4          1.85   
4468    1400000.0      2014.0                    0.0        8.7          2.35   
4474    1288000.0      1940.0                  991.0        8.2          1.37   
4483    1420000.0      2014.0                  372.0        4.1          2.35   
4498    1200000.0      1966.0                   34.0        8.9          2.35   
4528          NaN      2009.0                   22.0        7.5           NaN   
4530     960000.0      1976.0                 1000.0        8.1          1.33   
4533    1000000.0      1963.0                  269.0        6.8          1.37   
4550          NaN      2008.0                  426.0        7.2          1.85   
4572    1000000.0      2000.0                  186.0        6.2          2.35   
4580          NaN      2009.0                   13.0        7.4          1.85   
4584   65000000.0      2009.0                  559.0        6.7          2.35   
4593    1500000.0      2005.0                  668.0        4.8           NaN   
4622    1000000.0      2009.0                  207.0        3.4           NaN   
4659     500000.0      2011.0                  712.0        8.4          1.85   
4688     700000.0      1994.0                    6.0        8.3          1.33   
4694  207000000.0      2005.0                  918.0        7.2          2.35   
4708     600000.0      1970.0                  227.0        8.1          2.20   
4723     500000.0      2008.0                  153.0        6.5          1.85   
4747    2000000.0      1954.0                    8.0        8.7          1.37   
4763     500000.0      2005.0                    0.0        5.8          1.33   
4768          NaN      2015.0                  317.0        2.2           NaN   
4778  215000000.0      2013.0                15000.0        6.4          2.35   
4789   25000000.0      2004.0                   24.0        7.6          1.85   
4810     385907.0      1916.0                   22.0        8.0          1.33   
4842   45000000.0      2007.0                  117.0        7.4          2.35   
4885     245000.0      1925.0                   12.0        8.3          1.33   
4894    5000000.0      1954.0                   53.0        7.2          1.37   
4912          NaN      1955.0                    0.0        8.1          1.37   
5020      17350.0      2011.0                   19.0        3.0           NaN   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
5                   24000  
6                       0  
8                  118000  
9                   10000  
10                 197000  
11                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
30                  80000  
31                      0  
32                  95000  
36                      0  
37                  56000  
                  ...  
4463                  100  
4468                    0  
4474                    0  
4483                  447  
4498                20000  
4528                  773  
4530                    0  
4533                  328  
4550                    0  
4572                   92  
4580                    0  
4584                16000  
4593                   31  
4622                   41  
4659                48000  
4688                    0  
4694                    0  
4708                    0  
4723                    0  
4747                11000  
4763                    0  
4768                  353  
4778                60000  
4789                    0  
4810                  691  
4842                14000  
4885                  226  
4894                    0  
4912                  863  
5020                   33  

[1067 rows x 28 columns]

ds1.country=ds1.country.fillna('')

ds1.duration=ds1.duration.fillna(ds1.duration.mean())

ds1.dropna()
Out[40]: 
                 color       director_name  num_critic_for_reviews  duration  \
0                Color       James Cameron                   723.0     178.0   
1                Color      Gore Verbinski                   302.0     169.0   
2                Color          Sam Mendes                   602.0     148.0   
3                Color   Christopher Nolan                   813.0     164.0   
5                Color      Andrew Stanton                   462.0     132.0   
6                Color           Sam Raimi                   392.0     156.0   
7                Color        Nathan Greno                   324.0     100.0   
8                Color         Joss Whedon                   635.0     141.0   
9                Color         David Yates                   375.0     153.0   
10               Color         Zack Snyder                   673.0     183.0   
11               Color        Bryan Singer                   434.0     169.0   
12               Color        Marc Forster                   403.0     106.0   
13               Color      Gore Verbinski                   313.0     151.0   
14               Color      Gore Verbinski                   450.0     150.0   
15               Color         Zack Snyder                   733.0     143.0   
16               Color      Andrew Adamson                   258.0     150.0   
17               Color         Joss Whedon                   703.0     173.0   
18               Color        Rob Marshall                   448.0     136.0   
19               Color    Barry Sonnenfeld                   451.0     106.0   
20               Color       Peter Jackson                   422.0     164.0   
21               Color           Marc Webb                   599.0     153.0   
22               Color        Ridley Scott                   343.0     156.0   
23               Color       Peter Jackson                   509.0     186.0   
24               Color         Chris Weitz                   251.0     113.0   
25               Color       Peter Jackson                   446.0     201.0   
26               Color       James Cameron                   315.0     194.0   
27               Color       Anthony Russo                   516.0     147.0   
28               Color          Peter Berg                   377.0     131.0   
29               Color     Colin Trevorrow                   644.0     124.0   
30               Color          Sam Mendes                   750.0     143.0   
               ...                 ...                     ...       ...   
4930             Color         Gary Winick                    91.0      78.0   
4931             Color         John Carney                   232.0      85.0   
4933             Color  Michel Orion Scott                    29.0      93.0   
4936             Color         Tobe Hooper                   277.0      88.0   
4941             Color       Michael Moore                    40.0      91.0   
4955             Color       Alex Kendrick                    31.0     111.0   
4956             Color        Travis Cluff                   159.0      81.0   
4959             Color     Robert Townsend                    21.0      81.0   
4962   Black and White       Larry Blamire                    88.0      90.0   
4964             Color           E.L. Katz                   193.0      88.0   
4971             Color      Dennis Iliadis                   241.0     114.0   
4973   Black and White    Darren Aronofsky                   138.0      84.0   
4975             Color     Myles Berkowitz                    32.0      87.0   
4977             Color     Morgan Spurlock                   193.0     100.0   
4978             Color       Brandon Trost                    66.0      82.0   
4979             Color        Joe Swanberg                    65.0      82.0   
4984             Color        Edward Burns                    36.0      98.0   
4987             Color         Lena Dunham                   113.0      98.0   
4997             Color  David Gordon Green                    75.0      90.0   
4998             Color        Kevin Jordan                    21.0      90.0   
5008   Black and White         Kevin Smith                   136.0     102.0   
5011             Color         Neil LaBute                    80.0      97.0   
5012             Color          David Ayer                   233.0     109.0   
5015   Black and White   Richard Linklater                    61.0     100.0   
5025             Color         John Waters                    73.0     108.0   
5026             Color     Olivier Assayas                    81.0     110.0   
5027             Color        Jafar Panahi                    64.0      90.0   
5033             Color       Shane Carruth                   143.0      77.0   
5035             Color    Robert Rodriguez                    56.0      81.0   
5042             Color            Jon Gunn                    43.0      90.0   

      director_facebook_likes  actor_3_facebook_likes          actor_2_name  \
0                         0.0                   855.0      Joel David Moore   
1                       563.0                  1000.0         Orlando Bloom   
2                         0.0                   161.0          Rory Kinnear   
3                     22000.0                 23000.0        Christian Bale   
5                       475.0                   530.0       Samantha Morton   
6                         0.0                  4000.0          James Franco   
7                        15.0                   284.0          Donna Murphy   
8                         0.0                 19000.0     Robert Downey Jr.   
9                       282.0                 10000.0      Daniel Radcliffe   
10                        0.0                  2000.0          Lauren Cohan   
11                        0.0                   903.0         Marlon Brando   
12                      395.0                   393.0       Mathieu Amalric   
13                      563.0                  1000.0         Orlando Bloom   
14                      563.0                  1000.0           Ruth Wilson   
15                        0.0                   748.0    Christopher Meloni   
16                       80.0                   201.0  Pierfrancesco Favino   
17                        0.0                 19000.0     Robert Downey Jr.   
18                      252.0                  1000.0           Sam Claflin   
19                      188.0                   718.0     Michael Stuhlbarg   
20                        0.0                   773.0            Adam Brown   
21                      464.0                   963.0       Andrew Garfield   
22                        0.0                   738.0          William Hurt   
23                        0.0                   773.0            Adam Brown   
24                      129.0                  1000.0             Eva Green   
25                        0.0                    84.0    Thomas Kretschmann   
26                        0.0                   794.0          Kate Winslet   
27                       94.0                 11000.0    Scarlett Johansson   
28                      532.0                   627.0  Alexander SkarsgÃ¥rd   
29                      365.0                  1000.0            Judy Greer   
30                        0.0                   393.0         Helen McCrory   
                      ...                     ...                   ...   
4930                     56.0                   184.0        Aaron Stanford   
4931                    109.0                    18.0     MarkÃ©ta IrglovÃ¡   
4933                      0.0                     2.0        Rowan Isaacson   
4936                    365.0                   177.0            Edwin Neal   
4941                    909.0                    42.0             Pat Boone   
4955                    589.0                    51.0           Erin Bethea   
4956                      3.0                     7.0       Cassidy Gifford   
4959                    467.0                   287.0   Keenen Ivory Wayans   
4962                     56.0                    56.0            Brian Howe   
4964                      3.0                   307.0           Ethan Embry   
4971                     29.0                   616.0         Monica Potter   
4973                      0.0                   194.0         Clint Mansell   
4975                      0.0                   153.0          Tom Ardavany   
4977                    293.0                     0.0        Amanda Kearsan   
4978                     32.0                   128.0           Sean Whalen   
4979                    217.0                   442.0           Lena Dunham   
4984                      0.0                    73.0       Michael McGlone   
4987                    969.0                   433.0         Merritt Wever   
4997                    234.0                    15.0           Eddie Rouse   
4998                      4.0                   113.0        Christa Miller   
5008                      0.0                   216.0      Brian O'Halloran   
5011                    119.0                     7.0           Matt Malloy   
5012                    453.0                   120.0        Martin Donovan   
5015                      0.0                     0.0     Richard Linklater   
5025                      0.0                   105.0            Mink Stole   
5026                    107.0                    45.0       BÃ©atrice Dalle   
5027                    397.0                     0.0     Nargess Mamizadeh   
5033                    291.0                     8.0        David Sullivan   
5035                      0.0                     6.0       Peter Marquardt   
5042                     16.0                    16.0      Brian Herzlinger   

      actor_1_facebook_likes        gross  \
0                     1000.0  760505847.0   
1                    40000.0  309404152.0   
2                    11000.0  200074175.0   
3                    27000.0  448130642.0   
5                      640.0   73058679.0   
6                    24000.0  336530303.0   
7                      799.0  200807262.0   
8                    26000.0  458991599.0   
9                    25000.0  301956980.0   
10                   15000.0  330249062.0   
11                   18000.0  200069408.0   
12                     451.0  168368427.0   
13                   40000.0  423032628.0   
14                   40000.0   89289910.0   
15                   15000.0  291021565.0   
16                   22000.0  141614023.0   
17                   26000.0  623279547.0   
18                   40000.0  241063875.0   
19                   10000.0  179020854.0   
20                    5000.0  255108370.0   
21                   15000.0  262030663.0   
22                     891.0  105219735.0   
23                    5000.0  258355354.0   
24                   16000.0   70083519.0   
25                    6000.0  218051260.0   
26                   29000.0  658672302.0   
27                   21000.0  407197282.0   
28                   14000.0   65173160.0   
29                    3000.0  652177271.0   
30                     883.0  304360277.0   
                     ...          ...   
4930                   376.0    2882062.0   
4931                   200.0    9437933.0   
4933                    58.0     155984.0   
4936                   383.0   30859000.0   
4941                   909.0    6706368.0   
4955                   589.0   10174663.0   
4956                   220.0   22757819.0   
4959                   467.0    5228617.0   
4962                   126.0     110536.0   
4964                  3000.0      59379.0   
4971                   956.0   32721635.0   
4973                  1000.0    3216970.0   
4975                  1000.0     536767.0   
4977                     0.0   11529368.0   
4978                   968.0      40557.0   
4979                 10000.0      30084.0   
4984                   138.0   10246600.0   
4987                   969.0     389804.0   
4997                   552.0     241816.0   
4998                 20000.0     277233.0   
5008                   898.0    3151130.0   
5011                   136.0    2856622.0   
5012                  1000.0   10499968.0   
5015                     5.0    1227508.0   
5025                   462.0     180483.0   
5026                   576.0     136007.0   
5027                     5.0     673780.0   
5033                   291.0     424760.0   
5035                   121.0    2040920.0   
5042                    86.0      85222.0   

                                                 genres         ...           \
0                       Action|Adventure|Fantasy|Sci-Fi         ...            
1                              Action|Adventure|Fantasy         ...            
2                             Action|Adventure|Thriller         ...            
3                                       Action|Thriller         ...            
5                               Action|Adventure|Sci-Fi         ...            
6                              Action|Adventure|Romance         ...            
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...            
8                               Action|Adventure|Sci-Fi         ...            
9                      Adventure|Family|Fantasy|Mystery         ...            
10                              Action|Adventure|Sci-Fi         ...            
11                              Action|Adventure|Sci-Fi         ...            
12                                     Action|Adventure         ...            
13                             Action|Adventure|Fantasy         ...            
14                             Action|Adventure|Western         ...            
15                      Action|Adventure|Fantasy|Sci-Fi         ...            
16                      Action|Adventure|Family|Fantasy         ...            
17                              Action|Adventure|Sci-Fi         ...            
18                             Action|Adventure|Fantasy         ...            
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...            
20                                    Adventure|Fantasy         ...            
21                             Action|Adventure|Fantasy         ...            
22                       Action|Adventure|Drama|History         ...            
23                                    Adventure|Fantasy         ...            
24                             Adventure|Family|Fantasy         ...            
25                       Action|Adventure|Drama|Romance         ...            
26                                        Drama|Romance         ...            
27                              Action|Adventure|Sci-Fi         ...            
28                     Action|Adventure|Sci-Fi|Thriller         ...            
29                     Action|Adventure|Sci-Fi|Thriller         ...            
30                            Action|Adventure|Thriller         ...            
                                                ...         ...            
4930                               Comedy|Drama|Romance         ...            
4931                                Drama|Music|Romance         ...            
4933                                        Documentary         ...            
4936                                    Horror|Thriller         ...            
4941                                        Documentary         ...            
4955                                        Drama|Sport         ...            
4956                                    Horror|Thriller         ...            
4959                                             Comedy         ...            
4962                               Comedy|Horror|Sci-Fi         ...            
4964                 Comedy|Crime|Drama|Horror|Thriller         ...            
4971                              Crime|Horror|Thriller         ...            
4973                             Drama|Mystery|Thriller         ...            
4975                           Biography|Comedy|Romance         ...            
4977                           Comedy|Documentary|Drama         ...            
4978                                             Comedy         ...            
4979                                       Comedy|Drama         ...            
4984                               Comedy|Drama|Romance         ...            
4987                               Comedy|Drama|Romance         ...            
4997                                              Drama         ...            
4998                                     Comedy|Romance         ...            
5008                                             Comedy         ...            
5011                                       Comedy|Drama         ...            
5012                        Action|Crime|Drama|Thriller         ...            
5015                                       Comedy|Drama         ...            
5025                                Comedy|Crime|Horror         ...            
5026                                Drama|Music|Romance         ...            
5027                                              Drama         ...            
5033                              Drama|Sci-Fi|Thriller         ...            
5035                Action|Crime|Drama|Romance|Thriller         ...            
5042                                        Documentary         ...            

     num_user_for_reviews language      country  content_rating       budget  \
0                  3054.0  English          USA           PG-13  237000000.0   
1                  1238.0  English          USA           PG-13  300000000.0   
2                   994.0  English           UK           PG-13  245000000.0   
3                  2701.0  English          USA           PG-13  250000000.0   
5                   738.0  English          USA           PG-13  263700000.0   
6                  1902.0  English          USA           PG-13  258000000.0   
7                   387.0  English          USA              PG  260000000.0   
8                  1117.0  English          USA           PG-13  250000000.0   
9                   973.0  English           UK              PG  250000000.0   
10                 3018.0  English          USA           PG-13  250000000.0   
11                 2367.0  English          USA           PG-13  209000000.0   
12                 1243.0  English           UK           PG-13  200000000.0   
13                 1832.0  English          USA           PG-13  225000000.0   
14                  711.0  English          USA           PG-13  215000000.0   
15                 2536.0  English          USA           PG-13  225000000.0   
16                  438.0  English          USA              PG  225000000.0   
17                 1722.0  English          USA           PG-13  220000000.0   
18                  484.0  English          USA           PG-13  250000000.0   
19                  341.0  English          USA           PG-13  225000000.0   
20                  802.0  English  New Zealand           PG-13  250000000.0   
21                 1225.0  English          USA           PG-13  230000000.0   
22                  546.0  English          USA           PG-13  200000000.0   
23                  951.0  English          USA           PG-13  225000000.0   
24                  666.0  English          USA           PG-13  180000000.0   
25                 2618.0  English  New Zealand           PG-13  207000000.0   
26                 2528.0  English          USA           PG-13  200000000.0   
27                 1022.0  English          USA           PG-13  250000000.0   
28                  751.0  English          USA           PG-13  209000000.0   
29                 1290.0  English          USA           PG-13  150000000.0   
30                 1498.0  English           UK           PG-13  200000000.0   
                  ...      ...          ...             ...          ...   
4930                101.0  English          USA           PG-13     150000.0   
4931                329.0  English      Ireland               R     180000.0   
4933                  9.0  English          USA         Unrated     160000.0   
4936                826.0  English          USA               R      83532.0   
4941                133.0  English          USA               R     160000.0   
4955                382.0  English          USA              PG     100000.0   
4956                150.0  English          USA               R     100000.0   
4959                 32.0  English          USA               R     100000.0   
4962                118.0  English          USA              PG      40000.0   
4964                 52.0  English          USA       Not Rated     200000.0   
4971                279.0  English          USA               R   15000000.0   
4973                586.0  English          USA               R      60000.0   
4975                 83.0  English          USA               R      60000.0   
4977                404.0  English          USA              PG      65000.0   
4978                 22.0  English          USA               R      60000.0   
4979                 23.0  English          USA               R      70000.0   
4984                 36.0  English          USA               R      25000.0   
4987                 35.0  English          USA       Not Rated      65000.0   
4997                 76.0  English          USA         Unrated      42000.0   
4998                 26.0  English          USA               R      40000.0   
5008                615.0  English          USA               R     230000.0   
5011                197.0  English       Canada               R      25000.0   
5012                212.0  English          USA               R   35000000.0   
5015                 80.0  English          USA               R      23000.0   
5025                183.0  English          USA           NC-17      10000.0   
5026                 39.0   French       France               R       4500.0   
5027                 26.0  Persian         Iran       Not Rated      10000.0   
5033                371.0  English          USA           PG-13       7000.0   
5035                130.0  Spanish          USA               R       7000.0   
5042                 84.0  English          USA              PG       1100.0   

      title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0         2009.0                  936.0        7.9          1.78   
1         2007.0                 5000.0        7.1          2.35   
2         2015.0                  393.0        6.8          2.35   
3         2012.0                23000.0        8.5          2.35   
5         2012.0                  632.0        6.6          2.35   
6         2007.0                11000.0        6.2          2.35   
7         2010.0                  553.0        7.8          1.85   
8         2015.0                21000.0        7.5          2.35   
9         2009.0                11000.0        7.5          2.35   
10        2016.0                 4000.0        6.9          2.35   
11        2006.0                10000.0        6.1          2.35   
12        2008.0                  412.0        6.7          2.35   
13        2006.0                 5000.0        7.3          2.35   
14        2013.0                 2000.0        6.5          2.35   
15        2013.0                 3000.0        7.2          2.35   
16        2008.0                  216.0        6.6          2.35   
17        2012.0                21000.0        8.1          1.85   
18        2011.0                11000.0        6.7          2.35   
19        2012.0                  816.0        6.8          1.85   
20        2014.0                  972.0        7.5          2.35   
21        2012.0                10000.0        7.0          2.35   
22        2010.0                  882.0        6.7          2.35   
23        2013.0                  972.0        7.9          2.35   
24        2007.0                 6000.0        6.1          2.35   
25        2005.0                  919.0        7.2          2.35   
26        1997.0                14000.0        7.7          2.35   
27        2016.0                19000.0        8.2          2.35   
28        2012.0                10000.0        5.9          2.35   
29        2015.0                 2000.0        7.0          2.00   
30        2012.0                  563.0        7.8          2.35   
         ...                    ...        ...           ...   
4930      2000.0                  346.0        6.3          1.85   
4931      2007.0                   96.0        7.9          1.85   
4933      2009.0                    2.0        7.4          1.85   
4936      1974.0                  371.0        7.5          1.85   
4941      1989.0                   91.0        7.5          1.66   
4955      2006.0                  150.0        6.7          1.85   
4956      2015.0                   40.0        4.2          1.85   
4959      1987.0                  322.0        7.0          1.85   
4962      2001.0                   76.0        7.0          1.85   
4964      2013.0                  982.0        6.8          2.35   
4971      2009.0                  878.0        6.6          1.85   
4973      1998.0                  512.0        7.5          1.66   
4975      1998.0                  184.0        5.3          1.85   
4977      2004.0                    0.0        7.3          1.78   
4978      2011.0                  407.0        5.6          2.35   
4979      2014.0                  969.0        5.6          1.85   
4984      1995.0                  111.0        6.6          1.85   
4987      2010.0                  529.0        6.3          2.35   
4997      2000.0                   61.0        7.5          2.35   
4998      1999.0                  467.0        7.6          1.85   
5008      1994.0                  657.0        7.8          1.37   
5011      1997.0                  108.0        7.3          1.85   
5012      2014.0                  206.0        5.7          1.85   
5015      1991.0                    0.0        7.1          1.37   
5025      1972.0                  143.0        6.1          1.37   
5026      2004.0                  133.0        6.9          2.35   
5027      2000.0                    0.0        7.5          1.85   
5033      2004.0                   45.0        7.0          1.85   
5035      1992.0                   20.0        6.9          1.37   
5042      2004.0                   23.0        6.6          1.85   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
5                   24000  
6                       0  
7                   29000  
8                  118000  
9                   10000  
10                 197000  
11                      0  
12                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
19                  40000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
24                      0  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
30                  80000  
                  ...  
4930                  132  
4931                26000  
4933                    0  
4936                    0  
4941                  667  
4955                    0  
4956                    0  
4959                  471  
4962                    0  
4964                    0  
4971                    0  
4973                24000  
4975                   30  
4977                    0  
4978                    0  
4979                  812  
4984                  265  
4987                    0  
4997                  451  
4998                    0  
5008                    0  
5011                  489  
5012                10000  
5015                 2000  
5025                    0  
5026                  171  
5027                  697  
5033                19000  
5035                    0  
5042                  456  

[3756 rows x 28 columns]

ds1.dropna(how='all')
Out[41]: 
                 color       director_name  num_critic_for_reviews  \
0                Color       James Cameron                   723.0   
1                Color      Gore Verbinski                   302.0   
2                Color          Sam Mendes                   602.0   
3                Color   Christopher Nolan                   813.0   
4                  NaN         Doug Walker                     NaN   
5                Color      Andrew Stanton                   462.0   
6                Color           Sam Raimi                   392.0   
7                Color        Nathan Greno                   324.0   
8                Color         Joss Whedon                   635.0   
9                Color         David Yates                   375.0   
10               Color         Zack Snyder                   673.0   
11               Color        Bryan Singer                   434.0   
12               Color        Marc Forster                   403.0   
13               Color      Gore Verbinski                   313.0   
14               Color      Gore Verbinski                   450.0   
15               Color         Zack Snyder                   733.0   
16               Color      Andrew Adamson                   258.0   
17               Color         Joss Whedon                   703.0   
18               Color        Rob Marshall                   448.0   
19               Color    Barry Sonnenfeld                   451.0   
20               Color       Peter Jackson                   422.0   
21               Color           Marc Webb                   599.0   
22               Color        Ridley Scott                   343.0   
23               Color       Peter Jackson                   509.0   
24               Color         Chris Weitz                   251.0   
25               Color       Peter Jackson                   446.0   
26               Color       James Cameron                   315.0   
27               Color       Anthony Russo                   516.0   
28               Color          Peter Berg                   377.0   
29               Color     Colin Trevorrow                   644.0   
               ...                 ...                     ...   
5013             Color          Eric Eason                    28.0   
5014             Color            Uwe Boll                    58.0   
5015   Black and White   Richard Linklater                    61.0   
5016             Color     Joseph Mazzella                     NaN   
5017             Color        Travis Legge                     1.0   
5018             Color       Alex Kendrick                     5.0   
5019             Color       Marcus Nispel                    43.0   
5020               NaN     Brandon Landers                     NaN   
5021             Color         Jay Duplass                    51.0   
5022   Black and White          Jim Chuchu                     6.0   
5023             Color          Daryl Wein                    22.0   
5024             Color         Jason Trost                    42.0   
5025             Color         John Waters                    73.0   
5026             Color     Olivier Assayas                    81.0   
5027             Color        Jafar Panahi                    64.0   
5028   Black and White       Ivan Kavanagh                    12.0   
5029             Color    Kiyoshi Kurosawa                    78.0   
5030             Color        Tadeo Garcia                     NaN   
5031             Color  Thomas L. Phillips                    13.0   
5032             Color     Ash Baron-Cohen                    10.0   
5033             Color       Shane Carruth                   143.0   
5034             Color    Neill Dela Llana                    35.0   
5035             Color    Robert Rodriguez                    56.0   
5036             Color     Anthony Vallone                     NaN   
5037             Color        Edward Burns                    14.0   
5038             Color         Scott Smith                     1.0   
5039             Color                 NaN                    43.0   
5040             Color    Benjamin Roberds                    13.0   
5041             Color         Daniel Hsia                    14.0   
5042             Color            Jon Gunn                    43.0   

        duration  director_facebook_likes  actor_3_facebook_likes  \
0     178.000000                      0.0                   855.0   
1     169.000000                    563.0                  1000.0   
2     148.000000                      0.0                   161.0   
3     164.000000                  22000.0                 23000.0   
4     107.201074                    131.0                     NaN   
5     132.000000                    475.0                   530.0   
6     156.000000                      0.0                  4000.0   
7     100.000000                     15.0                   284.0   
8     141.000000                      0.0                 19000.0   
9     153.000000                    282.0                 10000.0   
10    183.000000                      0.0                  2000.0   
11    169.000000                      0.0                   903.0   
12    106.000000                    395.0                   393.0   
13    151.000000                    563.0                  1000.0   
14    150.000000                    563.0                  1000.0   
15    143.000000                      0.0                   748.0   
16    150.000000                     80.0                   201.0   
17    173.000000                      0.0                 19000.0   
18    136.000000                    252.0                  1000.0   
19    106.000000                    188.0                   718.0   
20    164.000000                      0.0                   773.0   
21    153.000000                    464.0                   963.0   
22    156.000000                      0.0                   738.0   
23    186.000000                      0.0                   773.0   
24    113.000000                    129.0                  1000.0   
25    201.000000                      0.0                    84.0   
26    194.000000                      0.0                   794.0   
27    147.000000                     94.0                 11000.0   
28    131.000000                    532.0                   627.0   
29    124.000000                    365.0                  1000.0   
         ...                      ...                     ...   
5013   79.000000                      3.0                    42.0   
5014   80.000000                    892.0                   492.0   
5015  100.000000                      0.0                     0.0   
5016   90.000000                      0.0                     9.0   
5017   90.000000                    138.0                   138.0   
5018  120.000000                    589.0                     4.0   
5019   91.000000                    158.0                   265.0   
5020  143.000000                      8.0                     8.0   
5021   85.000000                    157.0                    10.0   
5022   60.000000                      0.0                     4.0   
5023   88.000000                     38.0                   211.0   
5024   78.000000                     91.0                    86.0   
5025  108.000000                      0.0                   105.0   
5026  110.000000                    107.0                    45.0   
5027   90.000000                    397.0                     0.0   
5028   83.000000                     18.0                     0.0   
5029  111.000000                     62.0                     6.0   
5030   84.000000                      5.0                    12.0   
5031   82.000000                    120.0                    84.0   
5032   98.000000                      3.0                   152.0   
5033   77.000000                    291.0                     8.0   
5034   80.000000                      0.0                     0.0   
5035   81.000000                      0.0                     6.0   
5036   84.000000                      2.0                     2.0   
5037   95.000000                      0.0                   133.0   
5038   87.000000                      2.0                   318.0   
5039   43.000000                      NaN                   319.0   
5040   76.000000                      0.0                     0.0   
5041  100.000000                      0.0                   489.0   
5042   90.000000                     16.0                    16.0   

              actor_2_name  actor_1_facebook_likes        gross  \
0         Joel David Moore                  1000.0  760505847.0   
1            Orlando Bloom                 40000.0  309404152.0   
2             Rory Kinnear                 11000.0  200074175.0   
3           Christian Bale                 27000.0  448130642.0   
4               Rob Walker                   131.0          NaN   
5          Samantha Morton                   640.0   73058679.0   
6             James Franco                 24000.0  336530303.0   
7             Donna Murphy                   799.0  200807262.0   
8        Robert Downey Jr.                 26000.0  458991599.0   
9         Daniel Radcliffe                 25000.0  301956980.0   
10            Lauren Cohan                 15000.0  330249062.0   
11           Marlon Brando                 18000.0  200069408.0   
12         Mathieu Amalric                   451.0  168368427.0   
13           Orlando Bloom                 40000.0  423032628.0   
14             Ruth Wilson                 40000.0   89289910.0   
15      Christopher Meloni                 15000.0  291021565.0   
16    Pierfrancesco Favino                 22000.0  141614023.0   
17       Robert Downey Jr.                 26000.0  623279547.0   
18             Sam Claflin                 40000.0  241063875.0   
19       Michael Stuhlbarg                 10000.0  179020854.0   
20              Adam Brown                  5000.0  255108370.0   
21         Andrew Garfield                 15000.0  262030663.0   
22            William Hurt                   891.0  105219735.0   
23              Adam Brown                  5000.0  258355354.0   
24               Eva Green                 16000.0   70083519.0   
25      Thomas Kretschmann                  6000.0  218051260.0   
26            Kate Winslet                 29000.0  658672302.0   
27      Scarlett Johansson                 21000.0  407197282.0   
28    Alexander SkarsgÃ¥rd                 14000.0   65173160.0   
29              Judy Greer                  3000.0  652177271.0   
                   ...                     ...          ...   
5013       Panchito GÃ³mez                    93.0          NaN   
5014    Katharine Isabelle                   986.0          NaN   
5015     Richard Linklater                     5.0    1227508.0   
5016          Mikaal Bates                   313.0          NaN   
5017         Suzi Lorraine                   370.0          NaN   
5018           Lisa Arnold                    51.0          NaN   
5019       Brittany Curran                   630.0          NaN   
5020       Alana Kaniewski                   720.0          NaN   
5021         Katie Aselton                   830.0     192467.0   
5022         Olwenya Maina                   147.0          NaN   
5023         Heather Burns                   331.0      76382.0   
5024           Jason Trost                   407.0          NaN   
5025            Mink Stole                   462.0     180483.0   
5026       BÃ©atrice Dalle                   576.0     136007.0   
5027     Nargess Mamizadeh                     5.0     673780.0   
5028         Michael Parle                    10.0          NaN   
5029         Anna Nakagawa                    89.0      94596.0   
5030        Michael Cortez                    21.0          NaN   
5031            Joe Coffey                   785.0          NaN   
5032     Stanley B. Herman                   789.0          NaN   
5033        David Sullivan                   291.0     424760.0   
5034       Edgar Tancangco                     0.0      70071.0   
5035       Peter Marquardt                   121.0    2040920.0   
5036        John Considine                    45.0          NaN   
5037    Caitlin FitzGerald                   296.0       4584.0   
5038         Daphne Zuniga                   637.0          NaN   
5039         Valorie Curry                   841.0          NaN   
5040         Maxwell Moody                     0.0          NaN   
5041         Daniel Henney                   946.0      10443.0   
5042      Brian Herzlinger                    86.0      85222.0   

                                                 genres         ...           \
0                       Action|Adventure|Fantasy|Sci-Fi         ...            
1                              Action|Adventure|Fantasy         ...            
2                             Action|Adventure|Thriller         ...            
3                                       Action|Thriller         ...            
4                                           Documentary         ...            
5                               Action|Adventure|Sci-Fi         ...            
6                              Action|Adventure|Romance         ...            
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...            
8                               Action|Adventure|Sci-Fi         ...            
9                      Adventure|Family|Fantasy|Mystery         ...            
10                              Action|Adventure|Sci-Fi         ...            
11                              Action|Adventure|Sci-Fi         ...            
12                                     Action|Adventure         ...            
13                             Action|Adventure|Fantasy         ...            
14                             Action|Adventure|Western         ...            
15                      Action|Adventure|Fantasy|Sci-Fi         ...            
16                      Action|Adventure|Family|Fantasy         ...            
17                              Action|Adventure|Sci-Fi         ...            
18                             Action|Adventure|Fantasy         ...            
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...            
20                                    Adventure|Fantasy         ...            
21                             Action|Adventure|Fantasy         ...            
22                       Action|Adventure|Drama|History         ...            
23                                    Adventure|Fantasy         ...            
24                             Adventure|Family|Fantasy         ...            
25                       Action|Adventure|Drama|Romance         ...            
26                                        Drama|Romance         ...            
27                              Action|Adventure|Sci-Fi         ...            
28                     Action|Adventure|Sci-Fi|Thriller         ...            
29                     Action|Adventure|Sci-Fi|Thriller         ...            
                                                ...         ...            
5013                                       Drama|Family         ...            
5014                              Action|Crime|Thriller         ...            
5015                                       Comedy|Drama         ...            
5016                               Crime|Drama|Thriller         ...            
5017                                     Comedy|Romance         ...            
5018                                              Drama         ...            
5019                            Horror|Mystery|Thriller         ...            
5020                              Drama|Horror|Thriller         ...            
5021                               Comedy|Drama|Romance         ...            
5022                                              Drama         ...            
5023                                            Romance         ...            
5024                                    Sci-Fi|Thriller         ...            
5025                                Comedy|Crime|Horror         ...            
5026                                Drama|Music|Romance         ...            
5027                                              Drama         ...            
5028                                             Horror         ...            
5029                      Crime|Horror|Mystery|Thriller         ...            
5030                                              Drama         ...            
5031                             Comedy|Horror|Thriller         ...            
5032                                        Crime|Drama         ...            
5033                              Drama|Sci-Fi|Thriller         ...            
5034                                           Thriller         ...            
5035                Action|Crime|Drama|Romance|Thriller         ...            
5036                                        Crime|Drama         ...            
5037                                       Comedy|Drama         ...            
5038                                       Comedy|Drama         ...            
5039                       Crime|Drama|Mystery|Thriller         ...            
5040                              Drama|Horror|Thriller         ...            
5041                               Comedy|Drama|Romance         ...            
5042                                        Documentary         ...            

     num_user_for_reviews  language      country  content_rating       budget  \
0                  3054.0   English          USA           PG-13  237000000.0   
1                  1238.0   English          USA           PG-13  300000000.0   
2                   994.0   English           UK           PG-13  245000000.0   
3                  2701.0   English          USA           PG-13  250000000.0   
4                     NaN       NaN                          NaN          NaN   
5                   738.0   English          USA           PG-13  263700000.0   
6                  1902.0   English          USA           PG-13  258000000.0   
7                   387.0   English          USA              PG  260000000.0   
8                  1117.0   English          USA           PG-13  250000000.0   
9                   973.0   English           UK              PG  250000000.0   
10                 3018.0   English          USA           PG-13  250000000.0   
11                 2367.0   English          USA           PG-13  209000000.0   
12                 1243.0   English           UK           PG-13  200000000.0   
13                 1832.0   English          USA           PG-13  225000000.0   
14                  711.0   English          USA           PG-13  215000000.0   
15                 2536.0   English          USA           PG-13  225000000.0   
16                  438.0   English          USA              PG  225000000.0   
17                 1722.0   English          USA           PG-13  220000000.0   
18                  484.0   English          USA           PG-13  250000000.0   
19                  341.0   English          USA           PG-13  225000000.0   
20                  802.0   English  New Zealand           PG-13  250000000.0   
21                 1225.0   English          USA           PG-13  230000000.0   
22                  546.0   English          USA           PG-13  200000000.0   
23                  951.0   English          USA           PG-13  225000000.0   
24                  666.0   English          USA           PG-13  180000000.0   
25                 2618.0   English  New Zealand           PG-13  207000000.0   
26                 2528.0   English          USA           PG-13  200000000.0   
27                 1022.0   English          USA           PG-13  250000000.0   
28                  751.0   English          USA           PG-13  209000000.0   
29                 1290.0   English          USA           PG-13  150000000.0   
                  ...       ...          ...             ...          ...   
5013                 21.0   English          USA             NaN      24000.0   
5014                129.0   English       Canada               R          NaN   
5015                 80.0   English          USA               R      23000.0   
5016                  2.0   English          USA             NaN      25000.0   
5017                  3.0   English          USA             NaN      22000.0   
5018                 49.0   English          USA             NaN      20000.0   
5019                 33.0   English          USA               R          NaN   
5020                  8.0   English          USA             NaN      17350.0   
5021                 71.0   English          USA               R      15000.0   
5022                  1.0   Swahili        Kenya             NaN      15000.0   
5023                  8.0   English          USA             NaN      15000.0   
5024                 35.0   English          USA         Unrated      20000.0   
5025                183.0   English          USA           NC-17      10000.0   
5026                 39.0    French       France               R       4500.0   
5027                 26.0   Persian         Iran       Not Rated      10000.0   
5028                  1.0   English      Ireland             NaN      10000.0   
5029                 50.0  Japanese        Japan             NaN    1000000.0   
5030                  3.0   English          USA             NaN          NaN   
5031                  8.0   English          USA             NaN     200000.0   
5032                 14.0   English          USA             NaN          NaN   
5033                371.0   English          USA           PG-13       7000.0   
5034                 35.0   English  Philippines       Not Rated       7000.0   
5035                130.0   Spanish          USA               R       7000.0   
5036                  1.0   English          USA           PG-13       3250.0   
5037                 14.0   English          USA       Not Rated       9000.0   
5038                  6.0   English       Canada             NaN          NaN   
5039                359.0   English          USA           TV-14          NaN   
5040                  3.0   English          USA             NaN       1400.0   
5041                  9.0   English          USA           PG-13          NaN   
5042                 84.0   English          USA              PG       1100.0   

      title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0         2009.0                  936.0        7.9          1.78   
1         2007.0                 5000.0        7.1          2.35   
2         2015.0                  393.0        6.8          2.35   
3         2012.0                23000.0        8.5          2.35   
4            NaN                   12.0        7.1           NaN   
5         2012.0                  632.0        6.6          2.35   
6         2007.0                11000.0        6.2          2.35   
7         2010.0                  553.0        7.8          1.85   
8         2015.0                21000.0        7.5          2.35   
9         2009.0                11000.0        7.5          2.35   
10        2016.0                 4000.0        6.9          2.35   
11        2006.0                10000.0        6.1          2.35   
12        2008.0                  412.0        6.7          2.35   
13        2006.0                 5000.0        7.3          2.35   
14        2013.0                 2000.0        6.5          2.35   
15        2013.0                 3000.0        7.2          2.35   
16        2008.0                  216.0        6.6          2.35   
17        2012.0                21000.0        8.1          1.85   
18        2011.0                11000.0        6.7          2.35   
19        2012.0                  816.0        6.8          1.85   
20        2014.0                  972.0        7.5          2.35   
21        2012.0                10000.0        7.0          2.35   
22        2010.0                  882.0        6.7          2.35   
23        2013.0                  972.0        7.9          2.35   
24        2007.0                 6000.0        6.1          2.35   
25        2005.0                  919.0        7.2          2.35   
26        1997.0                14000.0        7.7          2.35   
27        2016.0                19000.0        8.2          2.35   
28        2012.0                10000.0        5.9          2.35   
29        2015.0                 2000.0        7.0          2.00   
         ...                    ...        ...           ...   
5013      2002.0                   46.0        7.0          1.78   
5014      2009.0                  918.0        6.3          2.35   
5015      1991.0                    0.0        7.1          1.37   
5016      2015.0                   25.0        4.8           NaN   
5017      2013.0                  184.0        3.3          1.78   
5018      2003.0                   49.0        6.9          1.85   
5019      2015.0                  512.0        4.6          1.85   
5020      2011.0                   19.0        3.0           NaN   
5021      2005.0                  224.0        6.6           NaN   
5022      2014.0                   19.0        7.4           NaN   
5023      2009.0                  212.0        6.2          2.35   
5024      2011.0                   91.0        4.0          2.35   
5025      1972.0                  143.0        6.1          1.37   
5026      2004.0                  133.0        6.9          2.35   
5027      2000.0                    0.0        7.5          1.85   
5028      2007.0                    5.0        6.7          1.33   
5029      1997.0                   13.0        7.4          1.85   
5030      2004.0                   20.0        6.1           NaN   
5031      2012.0                   98.0        5.4         16.00   
5032      1995.0                  194.0        6.4           NaN   
5033      2004.0                   45.0        7.0          1.85   
5034      2005.0                    0.0        6.3           NaN   
5035      1992.0                   20.0        6.9          1.37   
5036      2005.0                   44.0        7.8           NaN   
5037      2011.0                  205.0        6.4           NaN   
5038      2013.0                  470.0        7.7           NaN   
5039         NaN                  593.0        7.5         16.00   
5040      2013.0                    0.0        6.3           NaN   
5041      2012.0                  719.0        6.3          2.35   
5042      2004.0                   23.0        6.6          1.85   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
4                       0  
5                   24000  
6                       0  
7                   29000  
8                  118000  
9                   10000  
10                 197000  
11                      0  
12                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
19                  40000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
24                      0  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
                  ...  
5013                   61  
5014                    0  
5015                 2000  
5016                   33  
5017                  200  
5018                  725  
5019                    0  
5020                   33  
5021                  297  
5022                   45  
5023                  324  
5024                  835  
5025                    0  
5026                  171  
5027                  697  
5028                  105  
5029                  817  
5030                   22  
5031                  424  
5032                   20  
5033                19000  
5034                   74  
5035                    0  
5036                    4  
5037                  413  
5038                   84  
5039                32000  
5040                   16  
5041                  660  
5042                  456  

[5043 rows x 28 columns]

ds1.dropna(thresh=5)
Out[42]: 
                 color       director_name  num_critic_for_reviews  \
0                Color       James Cameron                   723.0   
1                Color      Gore Verbinski                   302.0   
2                Color          Sam Mendes                   602.0   
3                Color   Christopher Nolan                   813.0   
4                  NaN         Doug Walker                     NaN   
5                Color      Andrew Stanton                   462.0   
6                Color           Sam Raimi                   392.0   
7                Color        Nathan Greno                   324.0   
8                Color         Joss Whedon                   635.0   
9                Color         David Yates                   375.0   
10               Color         Zack Snyder                   673.0   
11               Color        Bryan Singer                   434.0   
12               Color        Marc Forster                   403.0   
13               Color      Gore Verbinski                   313.0   
14               Color      Gore Verbinski                   450.0   
15               Color         Zack Snyder                   733.0   
16               Color      Andrew Adamson                   258.0   
17               Color         Joss Whedon                   703.0   
18               Color        Rob Marshall                   448.0   
19               Color    Barry Sonnenfeld                   451.0   
20               Color       Peter Jackson                   422.0   
21               Color           Marc Webb                   599.0   
22               Color        Ridley Scott                   343.0   
23               Color       Peter Jackson                   509.0   
24               Color         Chris Weitz                   251.0   
25               Color       Peter Jackson                   446.0   
26               Color       James Cameron                   315.0   
27               Color       Anthony Russo                   516.0   
28               Color          Peter Berg                   377.0   
29               Color     Colin Trevorrow                   644.0   
               ...                 ...                     ...   
5013             Color          Eric Eason                    28.0   
5014             Color            Uwe Boll                    58.0   
5015   Black and White   Richard Linklater                    61.0   
5016             Color     Joseph Mazzella                     NaN   
5017             Color        Travis Legge                     1.0   
5018             Color       Alex Kendrick                     5.0   
5019             Color       Marcus Nispel                    43.0   
5020               NaN     Brandon Landers                     NaN   
5021             Color         Jay Duplass                    51.0   
5022   Black and White          Jim Chuchu                     6.0   
5023             Color          Daryl Wein                    22.0   
5024             Color         Jason Trost                    42.0   
5025             Color         John Waters                    73.0   
5026             Color     Olivier Assayas                    81.0   
5027             Color        Jafar Panahi                    64.0   
5028   Black and White       Ivan Kavanagh                    12.0   
5029             Color    Kiyoshi Kurosawa                    78.0   
5030             Color        Tadeo Garcia                     NaN   
5031             Color  Thomas L. Phillips                    13.0   
5032             Color     Ash Baron-Cohen                    10.0   
5033             Color       Shane Carruth                   143.0   
5034             Color    Neill Dela Llana                    35.0   
5035             Color    Robert Rodriguez                    56.0   
5036             Color     Anthony Vallone                     NaN   
5037             Color        Edward Burns                    14.0   
5038             Color         Scott Smith                     1.0   
5039             Color                 NaN                    43.0   
5040             Color    Benjamin Roberds                    13.0   
5041             Color         Daniel Hsia                    14.0   
5042             Color            Jon Gunn                    43.0   

        duration  director_facebook_likes  actor_3_facebook_likes  \
0     178.000000                      0.0                   855.0   
1     169.000000                    563.0                  1000.0   
2     148.000000                      0.0                   161.0   
3     164.000000                  22000.0                 23000.0   
4     107.201074                    131.0                     NaN   
5     132.000000                    475.0                   530.0   
6     156.000000                      0.0                  4000.0   
7     100.000000                     15.0                   284.0   
8     141.000000                      0.0                 19000.0   
9     153.000000                    282.0                 10000.0   
10    183.000000                      0.0                  2000.0   
11    169.000000                      0.0                   903.0   
12    106.000000                    395.0                   393.0   
13    151.000000                    563.0                  1000.0   
14    150.000000                    563.0                  1000.0   
15    143.000000                      0.0                   748.0   
16    150.000000                     80.0                   201.0   
17    173.000000                      0.0                 19000.0   
18    136.000000                    252.0                  1000.0   
19    106.000000                    188.0                   718.0   
20    164.000000                      0.0                   773.0   
21    153.000000                    464.0                   963.0   
22    156.000000                      0.0                   738.0   
23    186.000000                      0.0                   773.0   
24    113.000000                    129.0                  1000.0   
25    201.000000                      0.0                    84.0   
26    194.000000                      0.0                   794.0   
27    147.000000                     94.0                 11000.0   
28    131.000000                    532.0                   627.0   
29    124.000000                    365.0                  1000.0   
         ...                      ...                     ...   
5013   79.000000                      3.0                    42.0   
5014   80.000000                    892.0                   492.0   
5015  100.000000                      0.0                     0.0   
5016   90.000000                      0.0                     9.0   
5017   90.000000                    138.0                   138.0   
5018  120.000000                    589.0                     4.0   
5019   91.000000                    158.0                   265.0   
5020  143.000000                      8.0                     8.0   
5021   85.000000                    157.0                    10.0   
5022   60.000000                      0.0                     4.0   
5023   88.000000                     38.0                   211.0   
5024   78.000000                     91.0                    86.0   
5025  108.000000                      0.0                   105.0   
5026  110.000000                    107.0                    45.0   
5027   90.000000                    397.0                     0.0   
5028   83.000000                     18.0                     0.0   
5029  111.000000                     62.0                     6.0   
5030   84.000000                      5.0                    12.0   
5031   82.000000                    120.0                    84.0   
5032   98.000000                      3.0                   152.0   
5033   77.000000                    291.0                     8.0   
5034   80.000000                      0.0                     0.0   
5035   81.000000                      0.0                     6.0   
5036   84.000000                      2.0                     2.0   
5037   95.000000                      0.0                   133.0   
5038   87.000000                      2.0                   318.0   
5039   43.000000                      NaN                   319.0   
5040   76.000000                      0.0                     0.0   
5041  100.000000                      0.0                   489.0   
5042   90.000000                     16.0                    16.0   

              actor_2_name  actor_1_facebook_likes        gross  \
0         Joel David Moore                  1000.0  760505847.0   
1            Orlando Bloom                 40000.0  309404152.0   
2             Rory Kinnear                 11000.0  200074175.0   
3           Christian Bale                 27000.0  448130642.0   
4               Rob Walker                   131.0          NaN   
5          Samantha Morton                   640.0   73058679.0   
6             James Franco                 24000.0  336530303.0   
7             Donna Murphy                   799.0  200807262.0   
8        Robert Downey Jr.                 26000.0  458991599.0   
9         Daniel Radcliffe                 25000.0  301956980.0   
10            Lauren Cohan                 15000.0  330249062.0   
11           Marlon Brando                 18000.0  200069408.0   
12         Mathieu Amalric                   451.0  168368427.0   
13           Orlando Bloom                 40000.0  423032628.0   
14             Ruth Wilson                 40000.0   89289910.0   
15      Christopher Meloni                 15000.0  291021565.0   
16    Pierfrancesco Favino                 22000.0  141614023.0   
17       Robert Downey Jr.                 26000.0  623279547.0   
18             Sam Claflin                 40000.0  241063875.0   
19       Michael Stuhlbarg                 10000.0  179020854.0   
20              Adam Brown                  5000.0  255108370.0   
21         Andrew Garfield                 15000.0  262030663.0   
22            William Hurt                   891.0  105219735.0   
23              Adam Brown                  5000.0  258355354.0   
24               Eva Green                 16000.0   70083519.0   
25      Thomas Kretschmann                  6000.0  218051260.0   
26            Kate Winslet                 29000.0  658672302.0   
27      Scarlett Johansson                 21000.0  407197282.0   
28    Alexander SkarsgÃ¥rd                 14000.0   65173160.0   
29              Judy Greer                  3000.0  652177271.0   
                   ...                     ...          ...   
5013       Panchito GÃ³mez                    93.0          NaN   
5014    Katharine Isabelle                   986.0          NaN   
5015     Richard Linklater                     5.0    1227508.0   
5016          Mikaal Bates                   313.0          NaN   
5017         Suzi Lorraine                   370.0          NaN   
5018           Lisa Arnold                    51.0          NaN   
5019       Brittany Curran                   630.0          NaN   
5020       Alana Kaniewski                   720.0          NaN   
5021         Katie Aselton                   830.0     192467.0   
5022         Olwenya Maina                   147.0          NaN   
5023         Heather Burns                   331.0      76382.0   
5024           Jason Trost                   407.0          NaN   
5025            Mink Stole                   462.0     180483.0   
5026       BÃ©atrice Dalle                   576.0     136007.0   
5027     Nargess Mamizadeh                     5.0     673780.0   
5028         Michael Parle                    10.0          NaN   
5029         Anna Nakagawa                    89.0      94596.0   
5030        Michael Cortez                    21.0          NaN   
5031            Joe Coffey                   785.0          NaN   
5032     Stanley B. Herman                   789.0          NaN   
5033        David Sullivan                   291.0     424760.0   
5034       Edgar Tancangco                     0.0      70071.0   
5035       Peter Marquardt                   121.0    2040920.0   
5036        John Considine                    45.0          NaN   
5037    Caitlin FitzGerald                   296.0       4584.0   
5038         Daphne Zuniga                   637.0          NaN   
5039         Valorie Curry                   841.0          NaN   
5040         Maxwell Moody                     0.0          NaN   
5041         Daniel Henney                   946.0      10443.0   
5042      Brian Herzlinger                    86.0      85222.0   

                                                 genres         ...           \
0                       Action|Adventure|Fantasy|Sci-Fi         ...            
1                              Action|Adventure|Fantasy         ...            
2                             Action|Adventure|Thriller         ...            
3                                       Action|Thriller         ...            
4                                           Documentary         ...            
5                               Action|Adventure|Sci-Fi         ...            
6                              Action|Adventure|Romance         ...            
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...            
8                               Action|Adventure|Sci-Fi         ...            
9                      Adventure|Family|Fantasy|Mystery         ...            
10                              Action|Adventure|Sci-Fi         ...            
11                              Action|Adventure|Sci-Fi         ...            
12                                     Action|Adventure         ...            
13                             Action|Adventure|Fantasy         ...            
14                             Action|Adventure|Western         ...            
15                      Action|Adventure|Fantasy|Sci-Fi         ...            
16                      Action|Adventure|Family|Fantasy         ...            
17                              Action|Adventure|Sci-Fi         ...            
18                             Action|Adventure|Fantasy         ...            
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...            
20                                    Adventure|Fantasy         ...            
21                             Action|Adventure|Fantasy         ...            
22                       Action|Adventure|Drama|History         ...            
23                                    Adventure|Fantasy         ...            
24                             Adventure|Family|Fantasy         ...            
25                       Action|Adventure|Drama|Romance         ...            
26                                        Drama|Romance         ...            
27                              Action|Adventure|Sci-Fi         ...            
28                     Action|Adventure|Sci-Fi|Thriller         ...            
29                     Action|Adventure|Sci-Fi|Thriller         ...            
                                                ...         ...            
5013                                       Drama|Family         ...            
5014                              Action|Crime|Thriller         ...            
5015                                       Comedy|Drama         ...            
5016                               Crime|Drama|Thriller         ...            
5017                                     Comedy|Romance         ...            
5018                                              Drama         ...            
5019                            Horror|Mystery|Thriller         ...            
5020                              Drama|Horror|Thriller         ...            
5021                               Comedy|Drama|Romance         ...            
5022                                              Drama         ...            
5023                                            Romance         ...            
5024                                    Sci-Fi|Thriller         ...            
5025                                Comedy|Crime|Horror         ...            
5026                                Drama|Music|Romance         ...            
5027                                              Drama         ...            
5028                                             Horror         ...            
5029                      Crime|Horror|Mystery|Thriller         ...            
5030                                              Drama         ...            
5031                             Comedy|Horror|Thriller         ...            
5032                                        Crime|Drama         ...            
5033                              Drama|Sci-Fi|Thriller         ...            
5034                                           Thriller         ...            
5035                Action|Crime|Drama|Romance|Thriller         ...            
5036                                        Crime|Drama         ...            
5037                                       Comedy|Drama         ...            
5038                                       Comedy|Drama         ...            
5039                       Crime|Drama|Mystery|Thriller         ...            
5040                              Drama|Horror|Thriller         ...            
5041                               Comedy|Drama|Romance         ...            
5042                                        Documentary         ...            

     num_user_for_reviews  language      country  content_rating       budget  \
0                  3054.0   English          USA           PG-13  237000000.0   
1                  1238.0   English          USA           PG-13  300000000.0   
2                   994.0   English           UK           PG-13  245000000.0   
3                  2701.0   English          USA           PG-13  250000000.0   
4                     NaN       NaN                          NaN          NaN   
5                   738.0   English          USA           PG-13  263700000.0   
6                  1902.0   English          USA           PG-13  258000000.0   
7                   387.0   English          USA              PG  260000000.0   
8                  1117.0   English          USA           PG-13  250000000.0   
9                   973.0   English           UK              PG  250000000.0   
10                 3018.0   English          USA           PG-13  250000000.0   
11                 2367.0   English          USA           PG-13  209000000.0   
12                 1243.0   English           UK           PG-13  200000000.0   
13                 1832.0   English          USA           PG-13  225000000.0   
14                  711.0   English          USA           PG-13  215000000.0   
15                 2536.0   English          USA           PG-13  225000000.0   
16                  438.0   English          USA              PG  225000000.0   
17                 1722.0   English          USA           PG-13  220000000.0   
18                  484.0   English          USA           PG-13  250000000.0   
19                  341.0   English          USA           PG-13  225000000.0   
20                  802.0   English  New Zealand           PG-13  250000000.0   
21                 1225.0   English          USA           PG-13  230000000.0   
22                  546.0   English          USA           PG-13  200000000.0   
23                  951.0   English          USA           PG-13  225000000.0   
24                  666.0   English          USA           PG-13  180000000.0   
25                 2618.0   English  New Zealand           PG-13  207000000.0   
26                 2528.0   English          USA           PG-13  200000000.0   
27                 1022.0   English          USA           PG-13  250000000.0   
28                  751.0   English          USA           PG-13  209000000.0   
29                 1290.0   English          USA           PG-13  150000000.0   
                  ...       ...          ...             ...          ...   
5013                 21.0   English          USA             NaN      24000.0   
5014                129.0   English       Canada               R          NaN   
5015                 80.0   English          USA               R      23000.0   
5016                  2.0   English          USA             NaN      25000.0   
5017                  3.0   English          USA             NaN      22000.0   
5018                 49.0   English          USA             NaN      20000.0   
5019                 33.0   English          USA               R          NaN   
5020                  8.0   English          USA             NaN      17350.0   
5021                 71.0   English          USA               R      15000.0   
5022                  1.0   Swahili        Kenya             NaN      15000.0   
5023                  8.0   English          USA             NaN      15000.0   
5024                 35.0   English          USA         Unrated      20000.0   
5025                183.0   English          USA           NC-17      10000.0   
5026                 39.0    French       France               R       4500.0   
5027                 26.0   Persian         Iran       Not Rated      10000.0   
5028                  1.0   English      Ireland             NaN      10000.0   
5029                 50.0  Japanese        Japan             NaN    1000000.0   
5030                  3.0   English          USA             NaN          NaN   
5031                  8.0   English          USA             NaN     200000.0   
5032                 14.0   English          USA             NaN          NaN   
5033                371.0   English          USA           PG-13       7000.0   
5034                 35.0   English  Philippines       Not Rated       7000.0   
5035                130.0   Spanish          USA               R       7000.0   
5036                  1.0   English          USA           PG-13       3250.0   
5037                 14.0   English          USA       Not Rated       9000.0   
5038                  6.0   English       Canada             NaN          NaN   
5039                359.0   English          USA           TV-14          NaN   
5040                  3.0   English          USA             NaN       1400.0   
5041                  9.0   English          USA           PG-13          NaN   
5042                 84.0   English          USA              PG       1100.0   

      title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0         2009.0                  936.0        7.9          1.78   
1         2007.0                 5000.0        7.1          2.35   
2         2015.0                  393.0        6.8          2.35   
3         2012.0                23000.0        8.5          2.35   
4            NaN                   12.0        7.1           NaN   
5         2012.0                  632.0        6.6          2.35   
6         2007.0                11000.0        6.2          2.35   
7         2010.0                  553.0        7.8          1.85   
8         2015.0                21000.0        7.5          2.35   
9         2009.0                11000.0        7.5          2.35   
10        2016.0                 4000.0        6.9          2.35   
11        2006.0                10000.0        6.1          2.35   
12        2008.0                  412.0        6.7          2.35   
13        2006.0                 5000.0        7.3          2.35   
14        2013.0                 2000.0        6.5          2.35   
15        2013.0                 3000.0        7.2          2.35   
16        2008.0                  216.0        6.6          2.35   
17        2012.0                21000.0        8.1          1.85   
18        2011.0                11000.0        6.7          2.35   
19        2012.0                  816.0        6.8          1.85   
20        2014.0                  972.0        7.5          2.35   
21        2012.0                10000.0        7.0          2.35   
22        2010.0                  882.0        6.7          2.35   
23        2013.0                  972.0        7.9          2.35   
24        2007.0                 6000.0        6.1          2.35   
25        2005.0                  919.0        7.2          2.35   
26        1997.0                14000.0        7.7          2.35   
27        2016.0                19000.0        8.2          2.35   
28        2012.0                10000.0        5.9          2.35   
29        2015.0                 2000.0        7.0          2.00   
         ...                    ...        ...           ...   
5013      2002.0                   46.0        7.0          1.78   
5014      2009.0                  918.0        6.3          2.35   
5015      1991.0                    0.0        7.1          1.37   
5016      2015.0                   25.0        4.8           NaN   
5017      2013.0                  184.0        3.3          1.78   
5018      2003.0                   49.0        6.9          1.85   
5019      2015.0                  512.0        4.6          1.85   
5020      2011.0                   19.0        3.0           NaN   
5021      2005.0                  224.0        6.6           NaN   
5022      2014.0                   19.0        7.4           NaN   
5023      2009.0                  212.0        6.2          2.35   
5024      2011.0                   91.0        4.0          2.35   
5025      1972.0                  143.0        6.1          1.37   
5026      2004.0                  133.0        6.9          2.35   
5027      2000.0                    0.0        7.5          1.85   
5028      2007.0                    5.0        6.7          1.33   
5029      1997.0                   13.0        7.4          1.85   
5030      2004.0                   20.0        6.1           NaN   
5031      2012.0                   98.0        5.4         16.00   
5032      1995.0                  194.0        6.4           NaN   
5033      2004.0                   45.0        7.0          1.85   
5034      2005.0                    0.0        6.3           NaN   
5035      1992.0                   20.0        6.9          1.37   
5036      2005.0                   44.0        7.8           NaN   
5037      2011.0                  205.0        6.4           NaN   
5038      2013.0                  470.0        7.7           NaN   
5039         NaN                  593.0        7.5         16.00   
5040      2013.0                    0.0        6.3           NaN   
5041      2012.0                  719.0        6.3          2.35   
5042      2004.0                   23.0        6.6          1.85   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
4                       0  
5                   24000  
6                       0  
7                   29000  
8                  118000  
9                   10000  
10                 197000  
11                      0  
12                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
19                  40000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
24                      0  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
                  ...  
5013                   61  
5014                    0  
5015                 2000  
5016                   33  
5017                  200  
5018                  725  
5019                    0  
5020                   33  
5021                  297  
5022                   45  
5023                  324  
5024                  835  
5025                    0  
5026                  171  
5027                  697  
5028                  105  
5029                  817  
5030                   22  
5031                  424  
5032                   20  
5033                19000  
5034                   74  
5035                    0  
5036                    4  
5037                  413  
5038                   84  
5039                32000  
5040                   16  
5041                  660  
5042                  456  

[5043 rows x 28 columns]

ds1.dropna(subset=['title_year'])
Out[43]: 
                 color       director_name  num_critic_for_reviews  duration  \
0                Color       James Cameron                   723.0     178.0   
1                Color      Gore Verbinski                   302.0     169.0   
2                Color          Sam Mendes                   602.0     148.0   
3                Color   Christopher Nolan                   813.0     164.0   
5                Color      Andrew Stanton                   462.0     132.0   
6                Color           Sam Raimi                   392.0     156.0   
7                Color        Nathan Greno                   324.0     100.0   
8                Color         Joss Whedon                   635.0     141.0   
9                Color         David Yates                   375.0     153.0   
10               Color         Zack Snyder                   673.0     183.0   
11               Color        Bryan Singer                   434.0     169.0   
12               Color        Marc Forster                   403.0     106.0   
13               Color      Gore Verbinski                   313.0     151.0   
14               Color      Gore Verbinski                   450.0     150.0   
15               Color         Zack Snyder                   733.0     143.0   
16               Color      Andrew Adamson                   258.0     150.0   
17               Color         Joss Whedon                   703.0     173.0   
18               Color        Rob Marshall                   448.0     136.0   
19               Color    Barry Sonnenfeld                   451.0     106.0   
20               Color       Peter Jackson                   422.0     164.0   
21               Color           Marc Webb                   599.0     153.0   
22               Color        Ridley Scott                   343.0     156.0   
23               Color       Peter Jackson                   509.0     186.0   
24               Color         Chris Weitz                   251.0     113.0   
25               Color       Peter Jackson                   446.0     201.0   
26               Color       James Cameron                   315.0     194.0   
27               Color       Anthony Russo                   516.0     147.0   
28               Color          Peter Berg                   377.0     131.0   
29               Color     Colin Trevorrow                   644.0     124.0   
30               Color          Sam Mendes                   750.0     143.0   
               ...                 ...                     ...       ...   
5012             Color          David Ayer                   233.0     109.0   
5013             Color          Eric Eason                    28.0      79.0   
5014             Color            Uwe Boll                    58.0      80.0   
5015   Black and White   Richard Linklater                    61.0     100.0   
5016             Color     Joseph Mazzella                     NaN      90.0   
5017             Color        Travis Legge                     1.0      90.0   
5018             Color       Alex Kendrick                     5.0     120.0   
5019             Color       Marcus Nispel                    43.0      91.0   
5020               NaN     Brandon Landers                     NaN     143.0   
5021             Color         Jay Duplass                    51.0      85.0   
5022   Black and White          Jim Chuchu                     6.0      60.0   
5023             Color          Daryl Wein                    22.0      88.0   
5024             Color         Jason Trost                    42.0      78.0   
5025             Color         John Waters                    73.0     108.0   
5026             Color     Olivier Assayas                    81.0     110.0   
5027             Color        Jafar Panahi                    64.0      90.0   
5028   Black and White       Ivan Kavanagh                    12.0      83.0   
5029             Color    Kiyoshi Kurosawa                    78.0     111.0   
5030             Color        Tadeo Garcia                     NaN      84.0   
5031             Color  Thomas L. Phillips                    13.0      82.0   
5032             Color     Ash Baron-Cohen                    10.0      98.0   
5033             Color       Shane Carruth                   143.0      77.0   
5034             Color    Neill Dela Llana                    35.0      80.0   
5035             Color    Robert Rodriguez                    56.0      81.0   
5036             Color     Anthony Vallone                     NaN      84.0   
5037             Color        Edward Burns                    14.0      95.0   
5038             Color         Scott Smith                     1.0      87.0   
5040             Color    Benjamin Roberds                    13.0      76.0   
5041             Color         Daniel Hsia                    14.0     100.0   
5042             Color            Jon Gunn                    43.0      90.0   

      director_facebook_likes  actor_3_facebook_likes          actor_2_name  \
0                         0.0                   855.0      Joel David Moore   
1                       563.0                  1000.0         Orlando Bloom   
2                         0.0                   161.0          Rory Kinnear   
3                     22000.0                 23000.0        Christian Bale   
5                       475.0                   530.0       Samantha Morton   
6                         0.0                  4000.0          James Franco   
7                        15.0                   284.0          Donna Murphy   
8                         0.0                 19000.0     Robert Downey Jr.   
9                       282.0                 10000.0      Daniel Radcliffe   
10                        0.0                  2000.0          Lauren Cohan   
11                        0.0                   903.0         Marlon Brando   
12                      395.0                   393.0       Mathieu Amalric   
13                      563.0                  1000.0         Orlando Bloom   
14                      563.0                  1000.0           Ruth Wilson   
15                        0.0                   748.0    Christopher Meloni   
16                       80.0                   201.0  Pierfrancesco Favino   
17                        0.0                 19000.0     Robert Downey Jr.   
18                      252.0                  1000.0           Sam Claflin   
19                      188.0                   718.0     Michael Stuhlbarg   
20                        0.0                   773.0            Adam Brown   
21                      464.0                   963.0       Andrew Garfield   
22                        0.0                   738.0          William Hurt   
23                        0.0                   773.0            Adam Brown   
24                      129.0                  1000.0             Eva Green   
25                        0.0                    84.0    Thomas Kretschmann   
26                        0.0                   794.0          Kate Winslet   
27                       94.0                 11000.0    Scarlett Johansson   
28                      532.0                   627.0  Alexander SkarsgÃ¥rd   
29                      365.0                  1000.0            Judy Greer   
30                        0.0                   393.0         Helen McCrory   
                      ...                     ...                   ...   
5012                    453.0                   120.0        Martin Donovan   
5013                      3.0                    42.0       Panchito GÃ³mez   
5014                    892.0                   492.0    Katharine Isabelle   
5015                      0.0                     0.0     Richard Linklater   
5016                      0.0                     9.0          Mikaal Bates   
5017                    138.0                   138.0         Suzi Lorraine   
5018                    589.0                     4.0           Lisa Arnold   
5019                    158.0                   265.0       Brittany Curran   
5020                      8.0                     8.0       Alana Kaniewski   
5021                    157.0                    10.0         Katie Aselton   
5022                      0.0                     4.0         Olwenya Maina   
5023                     38.0                   211.0         Heather Burns   
5024                     91.0                    86.0           Jason Trost   
5025                      0.0                   105.0            Mink Stole   
5026                    107.0                    45.0       BÃ©atrice Dalle   
5027                    397.0                     0.0     Nargess Mamizadeh   
5028                     18.0                     0.0         Michael Parle   
5029                     62.0                     6.0         Anna Nakagawa   
5030                      5.0                    12.0        Michael Cortez   
5031                    120.0                    84.0            Joe Coffey   
5032                      3.0                   152.0     Stanley B. Herman   
5033                    291.0                     8.0        David Sullivan   
5034                      0.0                     0.0       Edgar Tancangco   
5035                      0.0                     6.0       Peter Marquardt   
5036                      2.0                     2.0        John Considine   
5037                      0.0                   133.0    Caitlin FitzGerald   
5038                      2.0                   318.0         Daphne Zuniga   
5040                      0.0                     0.0         Maxwell Moody   
5041                      0.0                   489.0         Daniel Henney   
5042                     16.0                    16.0      Brian Herzlinger   

      actor_1_facebook_likes        gross  \
0                     1000.0  760505847.0   
1                    40000.0  309404152.0   
2                    11000.0  200074175.0   
3                    27000.0  448130642.0   
5                      640.0   73058679.0   
6                    24000.0  336530303.0   
7                      799.0  200807262.0   
8                    26000.0  458991599.0   
9                    25000.0  301956980.0   
10                   15000.0  330249062.0   
11                   18000.0  200069408.0   
12                     451.0  168368427.0   
13                   40000.0  423032628.0   
14                   40000.0   89289910.0   
15                   15000.0  291021565.0   
16                   22000.0  141614023.0   
17                   26000.0  623279547.0   
18                   40000.0  241063875.0   
19                   10000.0  179020854.0   
20                    5000.0  255108370.0   
21                   15000.0  262030663.0   
22                     891.0  105219735.0   
23                    5000.0  258355354.0   
24                   16000.0   70083519.0   
25                    6000.0  218051260.0   
26                   29000.0  658672302.0   
27                   21000.0  407197282.0   
28                   14000.0   65173160.0   
29                    3000.0  652177271.0   
30                     883.0  304360277.0   
                     ...          ...   
5012                  1000.0   10499968.0   
5013                    93.0          NaN   
5014                   986.0          NaN   
5015                     5.0    1227508.0   
5016                   313.0          NaN   
5017                   370.0          NaN   
5018                    51.0          NaN   
5019                   630.0          NaN   
5020                   720.0          NaN   
5021                   830.0     192467.0   
5022                   147.0          NaN   
5023                   331.0      76382.0   
5024                   407.0          NaN   
5025                   462.0     180483.0   
5026                   576.0     136007.0   
5027                     5.0     673780.0   
5028                    10.0          NaN   
5029                    89.0      94596.0   
5030                    21.0          NaN   
5031                   785.0          NaN   
5032                   789.0          NaN   
5033                   291.0     424760.0   
5034                     0.0      70071.0   
5035                   121.0    2040920.0   
5036                    45.0          NaN   
5037                   296.0       4584.0   
5038                   637.0          NaN   
5040                     0.0          NaN   
5041                   946.0      10443.0   
5042                    86.0      85222.0   

                                                 genres         ...           \
0                       Action|Adventure|Fantasy|Sci-Fi         ...            
1                              Action|Adventure|Fantasy         ...            
2                             Action|Adventure|Thriller         ...            
3                                       Action|Thriller         ...            
5                               Action|Adventure|Sci-Fi         ...            
6                              Action|Adventure|Romance         ...            
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...            
8                               Action|Adventure|Sci-Fi         ...            
9                      Adventure|Family|Fantasy|Mystery         ...            
10                              Action|Adventure|Sci-Fi         ...            
11                              Action|Adventure|Sci-Fi         ...            
12                                     Action|Adventure         ...            
13                             Action|Adventure|Fantasy         ...            
14                             Action|Adventure|Western         ...            
15                      Action|Adventure|Fantasy|Sci-Fi         ...            
16                      Action|Adventure|Family|Fantasy         ...            
17                              Action|Adventure|Sci-Fi         ...            
18                             Action|Adventure|Fantasy         ...            
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...            
20                                    Adventure|Fantasy         ...            
21                             Action|Adventure|Fantasy         ...            
22                       Action|Adventure|Drama|History         ...            
23                                    Adventure|Fantasy         ...            
24                             Adventure|Family|Fantasy         ...            
25                       Action|Adventure|Drama|Romance         ...            
26                                        Drama|Romance         ...            
27                              Action|Adventure|Sci-Fi         ...            
28                     Action|Adventure|Sci-Fi|Thriller         ...            
29                     Action|Adventure|Sci-Fi|Thriller         ...            
30                            Action|Adventure|Thriller         ...            
                                                ...         ...            
5012                        Action|Crime|Drama|Thriller         ...            
5013                                       Drama|Family         ...            
5014                              Action|Crime|Thriller         ...            
5015                                       Comedy|Drama         ...            
5016                               Crime|Drama|Thriller         ...            
5017                                     Comedy|Romance         ...            
5018                                              Drama         ...            
5019                            Horror|Mystery|Thriller         ...            
5020                              Drama|Horror|Thriller         ...            
5021                               Comedy|Drama|Romance         ...            
5022                                              Drama         ...            
5023                                            Romance         ...            
5024                                    Sci-Fi|Thriller         ...            
5025                                Comedy|Crime|Horror         ...            
5026                                Drama|Music|Romance         ...            
5027                                              Drama         ...            
5028                                             Horror         ...            
5029                      Crime|Horror|Mystery|Thriller         ...            
5030                                              Drama         ...            
5031                             Comedy|Horror|Thriller         ...            
5032                                        Crime|Drama         ...            
5033                              Drama|Sci-Fi|Thriller         ...            
5034                                           Thriller         ...            
5035                Action|Crime|Drama|Romance|Thriller         ...            
5036                                        Crime|Drama         ...            
5037                                       Comedy|Drama         ...            
5038                                       Comedy|Drama         ...            
5040                              Drama|Horror|Thriller         ...            
5041                               Comedy|Drama|Romance         ...            
5042                                        Documentary         ...            

     num_user_for_reviews  language      country  content_rating       budget  \
0                  3054.0   English          USA           PG-13  237000000.0   
1                  1238.0   English          USA           PG-13  300000000.0   
2                   994.0   English           UK           PG-13  245000000.0   
3                  2701.0   English          USA           PG-13  250000000.0   
5                   738.0   English          USA           PG-13  263700000.0   
6                  1902.0   English          USA           PG-13  258000000.0   
7                   387.0   English          USA              PG  260000000.0   
8                  1117.0   English          USA           PG-13  250000000.0   
9                   973.0   English           UK              PG  250000000.0   
10                 3018.0   English          USA           PG-13  250000000.0   
11                 2367.0   English          USA           PG-13  209000000.0   
12                 1243.0   English           UK           PG-13  200000000.0   
13                 1832.0   English          USA           PG-13  225000000.0   
14                  711.0   English          USA           PG-13  215000000.0   
15                 2536.0   English          USA           PG-13  225000000.0   
16                  438.0   English          USA              PG  225000000.0   
17                 1722.0   English          USA           PG-13  220000000.0   
18                  484.0   English          USA           PG-13  250000000.0   
19                  341.0   English          USA           PG-13  225000000.0   
20                  802.0   English  New Zealand           PG-13  250000000.0   
21                 1225.0   English          USA           PG-13  230000000.0   
22                  546.0   English          USA           PG-13  200000000.0   
23                  951.0   English          USA           PG-13  225000000.0   
24                  666.0   English          USA           PG-13  180000000.0   
25                 2618.0   English  New Zealand           PG-13  207000000.0   
26                 2528.0   English          USA           PG-13  200000000.0   
27                 1022.0   English          USA           PG-13  250000000.0   
28                  751.0   English          USA           PG-13  209000000.0   
29                 1290.0   English          USA           PG-13  150000000.0   
30                 1498.0   English           UK           PG-13  200000000.0   
                  ...       ...          ...             ...          ...   
5012                212.0   English          USA               R   35000000.0   
5013                 21.0   English          USA             NaN      24000.0   
5014                129.0   English       Canada               R          NaN   
5015                 80.0   English          USA               R      23000.0   
5016                  2.0   English          USA             NaN      25000.0   
5017                  3.0   English          USA             NaN      22000.0   
5018                 49.0   English          USA             NaN      20000.0   
5019                 33.0   English          USA               R          NaN   
5020                  8.0   English          USA             NaN      17350.0   
5021                 71.0   English          USA               R      15000.0   
5022                  1.0   Swahili        Kenya             NaN      15000.0   
5023                  8.0   English          USA             NaN      15000.0   
5024                 35.0   English          USA         Unrated      20000.0   
5025                183.0   English          USA           NC-17      10000.0   
5026                 39.0    French       France               R       4500.0   
5027                 26.0   Persian         Iran       Not Rated      10000.0   
5028                  1.0   English      Ireland             NaN      10000.0   
5029                 50.0  Japanese        Japan             NaN    1000000.0   
5030                  3.0   English          USA             NaN          NaN   
5031                  8.0   English          USA             NaN     200000.0   
5032                 14.0   English          USA             NaN          NaN   
5033                371.0   English          USA           PG-13       7000.0   
5034                 35.0   English  Philippines       Not Rated       7000.0   
5035                130.0   Spanish          USA               R       7000.0   
5036                  1.0   English          USA           PG-13       3250.0   
5037                 14.0   English          USA       Not Rated       9000.0   
5038                  6.0   English       Canada             NaN          NaN   
5040                  3.0   English          USA             NaN       1400.0   
5041                  9.0   English          USA           PG-13          NaN   
5042                 84.0   English          USA              PG       1100.0   

      title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0         2009.0                  936.0        7.9          1.78   
1         2007.0                 5000.0        7.1          2.35   
2         2015.0                  393.0        6.8          2.35   
3         2012.0                23000.0        8.5          2.35   
5         2012.0                  632.0        6.6          2.35   
6         2007.0                11000.0        6.2          2.35   
7         2010.0                  553.0        7.8          1.85   
8         2015.0                21000.0        7.5          2.35   
9         2009.0                11000.0        7.5          2.35   
10        2016.0                 4000.0        6.9          2.35   
11        2006.0                10000.0        6.1          2.35   
12        2008.0                  412.0        6.7          2.35   
13        2006.0                 5000.0        7.3          2.35   
14        2013.0                 2000.0        6.5          2.35   
15        2013.0                 3000.0        7.2          2.35   
16        2008.0                  216.0        6.6          2.35   
17        2012.0                21000.0        8.1          1.85   
18        2011.0                11000.0        6.7          2.35   
19        2012.0                  816.0        6.8          1.85   
20        2014.0                  972.0        7.5          2.35   
21        2012.0                10000.0        7.0          2.35   
22        2010.0                  882.0        6.7          2.35   
23        2013.0                  972.0        7.9          2.35   
24        2007.0                 6000.0        6.1          2.35   
25        2005.0                  919.0        7.2          2.35   
26        1997.0                14000.0        7.7          2.35   
27        2016.0                19000.0        8.2          2.35   
28        2012.0                10000.0        5.9          2.35   
29        2015.0                 2000.0        7.0          2.00   
30        2012.0                  563.0        7.8          2.35   
         ...                    ...        ...           ...   
5012      2014.0                  206.0        5.7          1.85   
5013      2002.0                   46.0        7.0          1.78   
5014      2009.0                  918.0        6.3          2.35   
5015      1991.0                    0.0        7.1          1.37   
5016      2015.0                   25.0        4.8           NaN   
5017      2013.0                  184.0        3.3          1.78   
5018      2003.0                   49.0        6.9          1.85   
5019      2015.0                  512.0        4.6          1.85   
5020      2011.0                   19.0        3.0           NaN   
5021      2005.0                  224.0        6.6           NaN   
5022      2014.0                   19.0        7.4           NaN   
5023      2009.0                  212.0        6.2          2.35   
5024      2011.0                   91.0        4.0          2.35   
5025      1972.0                  143.0        6.1          1.37   
5026      2004.0                  133.0        6.9          2.35   
5027      2000.0                    0.0        7.5          1.85   
5028      2007.0                    5.0        6.7          1.33   
5029      1997.0                   13.0        7.4          1.85   
5030      2004.0                   20.0        6.1           NaN   
5031      2012.0                   98.0        5.4         16.00   
5032      1995.0                  194.0        6.4           NaN   
5033      2004.0                   45.0        7.0          1.85   
5034      2005.0                    0.0        6.3           NaN   
5035      1992.0                   20.0        6.9          1.37   
5036      2005.0                   44.0        7.8           NaN   
5037      2011.0                  205.0        6.4           NaN   
5038      2013.0                  470.0        7.7           NaN   
5040      2013.0                    0.0        6.3           NaN   
5041      2012.0                  719.0        6.3          2.35   
5042      2004.0                   23.0        6.6          1.85   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
5                   24000  
6                       0  
7                   29000  
8                  118000  
9                   10000  
10                 197000  
11                      0  
12                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
19                  40000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
24                      0  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
30                  80000  
                  ...  
5012                10000  
5013                   61  
5014                    0  
5015                 2000  
5016                   33  
5017                  200  
5018                  725  
5019                    0  
5020                   33  
5021                  297  
5022                   45  
5023                  324  
5024                  835  
5025                    0  
5026                  171  
5027                  697  
5028                  105  
5029                  817  
5030                   22  
5031                  424  
5032                   20  
5033                19000  
5034                   74  
5035                    0  
5036                    4  
5037                  413  
5038                   84  
5040                   16  
5041                  660  
5042                  456  

[4935 rows x 28 columns]

ds1.dropna(axis=1, how='all')
Out[44]: 
                 color       director_name  num_critic_for_reviews  \
0                Color       James Cameron                   723.0   
1                Color      Gore Verbinski                   302.0   
2                Color          Sam Mendes                   602.0   
3                Color   Christopher Nolan                   813.0   
4                  NaN         Doug Walker                     NaN   
5                Color      Andrew Stanton                   462.0   
6                Color           Sam Raimi                   392.0   
7                Color        Nathan Greno                   324.0   
8                Color         Joss Whedon                   635.0   
9                Color         David Yates                   375.0   
10               Color         Zack Snyder                   673.0   
11               Color        Bryan Singer                   434.0   
12               Color        Marc Forster                   403.0   
13               Color      Gore Verbinski                   313.0   
14               Color      Gore Verbinski                   450.0   
15               Color         Zack Snyder                   733.0   
16               Color      Andrew Adamson                   258.0   
17               Color         Joss Whedon                   703.0   
18               Color        Rob Marshall                   448.0   
19               Color    Barry Sonnenfeld                   451.0   
20               Color       Peter Jackson                   422.0   
21               Color           Marc Webb                   599.0   
22               Color        Ridley Scott                   343.0   
23               Color       Peter Jackson                   509.0   
24               Color         Chris Weitz                   251.0   
25               Color       Peter Jackson                   446.0   
26               Color       James Cameron                   315.0   
27               Color       Anthony Russo                   516.0   
28               Color          Peter Berg                   377.0   
29               Color     Colin Trevorrow                   644.0   
               ...                 ...                     ...   
5013             Color          Eric Eason                    28.0   
5014             Color            Uwe Boll                    58.0   
5015   Black and White   Richard Linklater                    61.0   
5016             Color     Joseph Mazzella                     NaN   
5017             Color        Travis Legge                     1.0   
5018             Color       Alex Kendrick                     5.0   
5019             Color       Marcus Nispel                    43.0   
5020               NaN     Brandon Landers                     NaN   
5021             Color         Jay Duplass                    51.0   
5022   Black and White          Jim Chuchu                     6.0   
5023             Color          Daryl Wein                    22.0   
5024             Color         Jason Trost                    42.0   
5025             Color         John Waters                    73.0   
5026             Color     Olivier Assayas                    81.0   
5027             Color        Jafar Panahi                    64.0   
5028   Black and White       Ivan Kavanagh                    12.0   
5029             Color    Kiyoshi Kurosawa                    78.0   
5030             Color        Tadeo Garcia                     NaN   
5031             Color  Thomas L. Phillips                    13.0   
5032             Color     Ash Baron-Cohen                    10.0   
5033             Color       Shane Carruth                   143.0   
5034             Color    Neill Dela Llana                    35.0   
5035             Color    Robert Rodriguez                    56.0   
5036             Color     Anthony Vallone                     NaN   
5037             Color        Edward Burns                    14.0   
5038             Color         Scott Smith                     1.0   
5039             Color                 NaN                    43.0   
5040             Color    Benjamin Roberds                    13.0   
5041             Color         Daniel Hsia                    14.0   
5042             Color            Jon Gunn                    43.0   

        duration  director_facebook_likes  actor_3_facebook_likes  \
0     178.000000                      0.0                   855.0   
1     169.000000                    563.0                  1000.0   
2     148.000000                      0.0                   161.0   
3     164.000000                  22000.0                 23000.0   
4     107.201074                    131.0                     NaN   
5     132.000000                    475.0                   530.0   
6     156.000000                      0.0                  4000.0   
7     100.000000                     15.0                   284.0   
8     141.000000                      0.0                 19000.0   
9     153.000000                    282.0                 10000.0   
10    183.000000                      0.0                  2000.0   
11    169.000000                      0.0                   903.0   
12    106.000000                    395.0                   393.0   
13    151.000000                    563.0                  1000.0   
14    150.000000                    563.0                  1000.0   
15    143.000000                      0.0                   748.0   
16    150.000000                     80.0                   201.0   
17    173.000000                      0.0                 19000.0   
18    136.000000                    252.0                  1000.0   
19    106.000000                    188.0                   718.0   
20    164.000000                      0.0                   773.0   
21    153.000000                    464.0                   963.0   
22    156.000000                      0.0                   738.0   
23    186.000000                      0.0                   773.0   
24    113.000000                    129.0                  1000.0   
25    201.000000                      0.0                    84.0   
26    194.000000                      0.0                   794.0   
27    147.000000                     94.0                 11000.0   
28    131.000000                    532.0                   627.0   
29    124.000000                    365.0                  1000.0   
         ...                      ...                     ...   
5013   79.000000                      3.0                    42.0   
5014   80.000000                    892.0                   492.0   
5015  100.000000                      0.0                     0.0   
5016   90.000000                      0.0                     9.0   
5017   90.000000                    138.0                   138.0   
5018  120.000000                    589.0                     4.0   
5019   91.000000                    158.0                   265.0   
5020  143.000000                      8.0                     8.0   
5021   85.000000                    157.0                    10.0   
5022   60.000000                      0.0                     4.0   
5023   88.000000                     38.0                   211.0   
5024   78.000000                     91.0                    86.0   
5025  108.000000                      0.0                   105.0   
5026  110.000000                    107.0                    45.0   
5027   90.000000                    397.0                     0.0   
5028   83.000000                     18.0                     0.0   
5029  111.000000                     62.0                     6.0   
5030   84.000000                      5.0                    12.0   
5031   82.000000                    120.0                    84.0   
5032   98.000000                      3.0                   152.0   
5033   77.000000                    291.0                     8.0   
5034   80.000000                      0.0                     0.0   
5035   81.000000                      0.0                     6.0   
5036   84.000000                      2.0                     2.0   
5037   95.000000                      0.0                   133.0   
5038   87.000000                      2.0                   318.0   
5039   43.000000                      NaN                   319.0   
5040   76.000000                      0.0                     0.0   
5041  100.000000                      0.0                   489.0   
5042   90.000000                     16.0                    16.0   

              actor_2_name  actor_1_facebook_likes        gross  \
0         Joel David Moore                  1000.0  760505847.0   
1            Orlando Bloom                 40000.0  309404152.0   
2             Rory Kinnear                 11000.0  200074175.0   
3           Christian Bale                 27000.0  448130642.0   
4               Rob Walker                   131.0          NaN   
5          Samantha Morton                   640.0   73058679.0   
6             James Franco                 24000.0  336530303.0   
7             Donna Murphy                   799.0  200807262.0   
8        Robert Downey Jr.                 26000.0  458991599.0   
9         Daniel Radcliffe                 25000.0  301956980.0   
10            Lauren Cohan                 15000.0  330249062.0   
11           Marlon Brando                 18000.0  200069408.0   
12         Mathieu Amalric                   451.0  168368427.0   
13           Orlando Bloom                 40000.0  423032628.0   
14             Ruth Wilson                 40000.0   89289910.0   
15      Christopher Meloni                 15000.0  291021565.0   
16    Pierfrancesco Favino                 22000.0  141614023.0   
17       Robert Downey Jr.                 26000.0  623279547.0   
18             Sam Claflin                 40000.0  241063875.0   
19       Michael Stuhlbarg                 10000.0  179020854.0   
20              Adam Brown                  5000.0  255108370.0   
21         Andrew Garfield                 15000.0  262030663.0   
22            William Hurt                   891.0  105219735.0   
23              Adam Brown                  5000.0  258355354.0   
24               Eva Green                 16000.0   70083519.0   
25      Thomas Kretschmann                  6000.0  218051260.0   
26            Kate Winslet                 29000.0  658672302.0   
27      Scarlett Johansson                 21000.0  407197282.0   
28    Alexander SkarsgÃ¥rd                 14000.0   65173160.0   
29              Judy Greer                  3000.0  652177271.0   
                   ...                     ...          ...   
5013       Panchito GÃ³mez                    93.0          NaN   
5014    Katharine Isabelle                   986.0          NaN   
5015     Richard Linklater                     5.0    1227508.0   
5016          Mikaal Bates                   313.0          NaN   
5017         Suzi Lorraine                   370.0          NaN   
5018           Lisa Arnold                    51.0          NaN   
5019       Brittany Curran                   630.0          NaN   
5020       Alana Kaniewski                   720.0          NaN   
5021         Katie Aselton                   830.0     192467.0   
5022         Olwenya Maina                   147.0          NaN   
5023         Heather Burns                   331.0      76382.0   
5024           Jason Trost                   407.0          NaN   
5025            Mink Stole                   462.0     180483.0   
5026       BÃ©atrice Dalle                   576.0     136007.0   
5027     Nargess Mamizadeh                     5.0     673780.0   
5028         Michael Parle                    10.0          NaN   
5029         Anna Nakagawa                    89.0      94596.0   
5030        Michael Cortez                    21.0          NaN   
5031            Joe Coffey                   785.0          NaN   
5032     Stanley B. Herman                   789.0          NaN   
5033        David Sullivan                   291.0     424760.0   
5034       Edgar Tancangco                     0.0      70071.0   
5035       Peter Marquardt                   121.0    2040920.0   
5036        John Considine                    45.0          NaN   
5037    Caitlin FitzGerald                   296.0       4584.0   
5038         Daphne Zuniga                   637.0          NaN   
5039         Valorie Curry                   841.0          NaN   
5040         Maxwell Moody                     0.0          NaN   
5041         Daniel Henney                   946.0      10443.0   
5042      Brian Herzlinger                    86.0      85222.0   

                                                 genres         ...           \
0                       Action|Adventure|Fantasy|Sci-Fi         ...            
1                              Action|Adventure|Fantasy         ...            
2                             Action|Adventure|Thriller         ...            
3                                       Action|Thriller         ...            
4                                           Documentary         ...            
5                               Action|Adventure|Sci-Fi         ...            
6                              Action|Adventure|Romance         ...            
7     Adventure|Animation|Comedy|Family|Fantasy|Musi...         ...            
8                               Action|Adventure|Sci-Fi         ...            
9                      Adventure|Family|Fantasy|Mystery         ...            
10                              Action|Adventure|Sci-Fi         ...            
11                              Action|Adventure|Sci-Fi         ...            
12                                     Action|Adventure         ...            
13                             Action|Adventure|Fantasy         ...            
14                             Action|Adventure|Western         ...            
15                      Action|Adventure|Fantasy|Sci-Fi         ...            
16                      Action|Adventure|Family|Fantasy         ...            
17                              Action|Adventure|Sci-Fi         ...            
18                             Action|Adventure|Fantasy         ...            
19        Action|Adventure|Comedy|Family|Fantasy|Sci-Fi         ...            
20                                    Adventure|Fantasy         ...            
21                             Action|Adventure|Fantasy         ...            
22                       Action|Adventure|Drama|History         ...            
23                                    Adventure|Fantasy         ...            
24                             Adventure|Family|Fantasy         ...            
25                       Action|Adventure|Drama|Romance         ...            
26                                        Drama|Romance         ...            
27                              Action|Adventure|Sci-Fi         ...            
28                     Action|Adventure|Sci-Fi|Thriller         ...            
29                     Action|Adventure|Sci-Fi|Thriller         ...            
                                                ...         ...            
5013                                       Drama|Family         ...            
5014                              Action|Crime|Thriller         ...            
5015                                       Comedy|Drama         ...            
5016                               Crime|Drama|Thriller         ...            
5017                                     Comedy|Romance         ...            
5018                                              Drama         ...            
5019                            Horror|Mystery|Thriller         ...            
5020                              Drama|Horror|Thriller         ...            
5021                               Comedy|Drama|Romance         ...            
5022                                              Drama         ...            
5023                                            Romance         ...            
5024                                    Sci-Fi|Thriller         ...            
5025                                Comedy|Crime|Horror         ...            
5026                                Drama|Music|Romance         ...            
5027                                              Drama         ...            
5028                                             Horror         ...            
5029                      Crime|Horror|Mystery|Thriller         ...            
5030                                              Drama         ...            
5031                             Comedy|Horror|Thriller         ...            
5032                                        Crime|Drama         ...            
5033                              Drama|Sci-Fi|Thriller         ...            
5034                                           Thriller         ...            
5035                Action|Crime|Drama|Romance|Thriller         ...            
5036                                        Crime|Drama         ...            
5037                                       Comedy|Drama         ...            
5038                                       Comedy|Drama         ...            
5039                       Crime|Drama|Mystery|Thriller         ...            
5040                              Drama|Horror|Thriller         ...            
5041                               Comedy|Drama|Romance         ...            
5042                                        Documentary         ...            

     num_user_for_reviews  language      country  content_rating       budget  \
0                  3054.0   English          USA           PG-13  237000000.0   
1                  1238.0   English          USA           PG-13  300000000.0   
2                   994.0   English           UK           PG-13  245000000.0   
3                  2701.0   English          USA           PG-13  250000000.0   
4                     NaN       NaN                          NaN          NaN   
5                   738.0   English          USA           PG-13  263700000.0   
6                  1902.0   English          USA           PG-13  258000000.0   
7                   387.0   English          USA              PG  260000000.0   
8                  1117.0   English          USA           PG-13  250000000.0   
9                   973.0   English           UK              PG  250000000.0   
10                 3018.0   English          USA           PG-13  250000000.0   
11                 2367.0   English          USA           PG-13  209000000.0   
12                 1243.0   English           UK           PG-13  200000000.0   
13                 1832.0   English          USA           PG-13  225000000.0   
14                  711.0   English          USA           PG-13  215000000.0   
15                 2536.0   English          USA           PG-13  225000000.0   
16                  438.0   English          USA              PG  225000000.0   
17                 1722.0   English          USA           PG-13  220000000.0   
18                  484.0   English          USA           PG-13  250000000.0   
19                  341.0   English          USA           PG-13  225000000.0   
20                  802.0   English  New Zealand           PG-13  250000000.0   
21                 1225.0   English          USA           PG-13  230000000.0   
22                  546.0   English          USA           PG-13  200000000.0   
23                  951.0   English          USA           PG-13  225000000.0   
24                  666.0   English          USA           PG-13  180000000.0   
25                 2618.0   English  New Zealand           PG-13  207000000.0   
26                 2528.0   English          USA           PG-13  200000000.0   
27                 1022.0   English          USA           PG-13  250000000.0   
28                  751.0   English          USA           PG-13  209000000.0   
29                 1290.0   English          USA           PG-13  150000000.0   
                  ...       ...          ...             ...          ...   
5013                 21.0   English          USA             NaN      24000.0   
5014                129.0   English       Canada               R          NaN   
5015                 80.0   English          USA               R      23000.0   
5016                  2.0   English          USA             NaN      25000.0   
5017                  3.0   English          USA             NaN      22000.0   
5018                 49.0   English          USA             NaN      20000.0   
5019                 33.0   English          USA               R          NaN   
5020                  8.0   English          USA             NaN      17350.0   
5021                 71.0   English          USA               R      15000.0   
5022                  1.0   Swahili        Kenya             NaN      15000.0   
5023                  8.0   English          USA             NaN      15000.0   
5024                 35.0   English          USA         Unrated      20000.0   
5025                183.0   English          USA           NC-17      10000.0   
5026                 39.0    French       France               R       4500.0   
5027                 26.0   Persian         Iran       Not Rated      10000.0   
5028                  1.0   English      Ireland             NaN      10000.0   
5029                 50.0  Japanese        Japan             NaN    1000000.0   
5030                  3.0   English          USA             NaN          NaN   
5031                  8.0   English          USA             NaN     200000.0   
5032                 14.0   English          USA             NaN          NaN   
5033                371.0   English          USA           PG-13       7000.0   
5034                 35.0   English  Philippines       Not Rated       7000.0   
5035                130.0   Spanish          USA               R       7000.0   
5036                  1.0   English          USA           PG-13       3250.0   
5037                 14.0   English          USA       Not Rated       9000.0   
5038                  6.0   English       Canada             NaN          NaN   
5039                359.0   English          USA           TV-14          NaN   
5040                  3.0   English          USA             NaN       1400.0   
5041                  9.0   English          USA           PG-13          NaN   
5042                 84.0   English          USA              PG       1100.0   

      title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0         2009.0                  936.0        7.9          1.78   
1         2007.0                 5000.0        7.1          2.35   
2         2015.0                  393.0        6.8          2.35   
3         2012.0                23000.0        8.5          2.35   
4            NaN                   12.0        7.1           NaN   
5         2012.0                  632.0        6.6          2.35   
6         2007.0                11000.0        6.2          2.35   
7         2010.0                  553.0        7.8          1.85   
8         2015.0                21000.0        7.5          2.35   
9         2009.0                11000.0        7.5          2.35   
10        2016.0                 4000.0        6.9          2.35   
11        2006.0                10000.0        6.1          2.35   
12        2008.0                  412.0        6.7          2.35   
13        2006.0                 5000.0        7.3          2.35   
14        2013.0                 2000.0        6.5          2.35   
15        2013.0                 3000.0        7.2          2.35   
16        2008.0                  216.0        6.6          2.35   
17        2012.0                21000.0        8.1          1.85   
18        2011.0                11000.0        6.7          2.35   
19        2012.0                  816.0        6.8          1.85   
20        2014.0                  972.0        7.5          2.35   
21        2012.0                10000.0        7.0          2.35   
22        2010.0                  882.0        6.7          2.35   
23        2013.0                  972.0        7.9          2.35   
24        2007.0                 6000.0        6.1          2.35   
25        2005.0                  919.0        7.2          2.35   
26        1997.0                14000.0        7.7          2.35   
27        2016.0                19000.0        8.2          2.35   
28        2012.0                10000.0        5.9          2.35   
29        2015.0                 2000.0        7.0          2.00   
         ...                    ...        ...           ...   
5013      2002.0                   46.0        7.0          1.78   
5014      2009.0                  918.0        6.3          2.35   
5015      1991.0                    0.0        7.1          1.37   
5016      2015.0                   25.0        4.8           NaN   
5017      2013.0                  184.0        3.3          1.78   
5018      2003.0                   49.0        6.9          1.85   
5019      2015.0                  512.0        4.6          1.85   
5020      2011.0                   19.0        3.0           NaN   
5021      2005.0                  224.0        6.6           NaN   
5022      2014.0                   19.0        7.4           NaN   
5023      2009.0                  212.0        6.2          2.35   
5024      2011.0                   91.0        4.0          2.35   
5025      1972.0                  143.0        6.1          1.37   
5026      2004.0                  133.0        6.9          2.35   
5027      2000.0                    0.0        7.5          1.85   
5028      2007.0                    5.0        6.7          1.33   
5029      1997.0                   13.0        7.4          1.85   
5030      2004.0                   20.0        6.1           NaN   
5031      2012.0                   98.0        5.4         16.00   
5032      1995.0                  194.0        6.4           NaN   
5033      2004.0                   45.0        7.0          1.85   
5034      2005.0                    0.0        6.3           NaN   
5035      1992.0                   20.0        6.9          1.37   
5036      2005.0                   44.0        7.8           NaN   
5037      2011.0                  205.0        6.4           NaN   
5038      2013.0                  470.0        7.7           NaN   
5039         NaN                  593.0        7.5         16.00   
5040      2013.0                    0.0        6.3           NaN   
5041      2012.0                  719.0        6.3          2.35   
5042      2004.0                   23.0        6.6          1.85   

     movie_facebook_likes  
0                   33000  
1                       0  
2                   85000  
3                  164000  
4                       0  
5                   24000  
6                       0  
7                   29000  
8                  118000  
9                   10000  
10                 197000  
11                      0  
12                      0  
13                   5000  
14                  48000  
15                 118000  
16                      0  
17                 123000  
18                  58000  
19                  40000  
20                  65000  
21                  56000  
22                  17000  
23                  83000  
24                      0  
25                      0  
26                  26000  
27                  72000  
28                  44000  
29                 150000  
                  ...  
5013                   61  
5014                    0  
5015                 2000  
5016                   33  
5017                  200  
5018                  725  
5019                    0  
5020                   33  
5021                  297  
5022                   45  
5023                  324  
5024                  835  
5025                    0  
5026                  171  
5027                  697  
5028                  105  
5029                  817  
5030                   22  
5031                  424  
5032                   20  
5033                19000  
5034                   74  
5035                    0  
5036                    4  
5037                  413  
5038                   84  
5039                32000  
5040                   16  
5041                  660  
5042                  456  

[5043 rows x 28 columns]

ds1.dropna(axis=1, how='any')
Out[45]: 
        duration                                             genres  \
0     178.000000                    Action|Adventure|Fantasy|Sci-Fi   
1     169.000000                           Action|Adventure|Fantasy   
2     148.000000                          Action|Adventure|Thriller   
3     164.000000                                    Action|Thriller   
4     107.201074                                        Documentary   
5     132.000000                            Action|Adventure|Sci-Fi   
6     156.000000                           Action|Adventure|Romance   
7     100.000000  Adventure|Animation|Comedy|Family|Fantasy|Musi...   
8     141.000000                            Action|Adventure|Sci-Fi   
9     153.000000                   Adventure|Family|Fantasy|Mystery   
10    183.000000                            Action|Adventure|Sci-Fi   
11    169.000000                            Action|Adventure|Sci-Fi   
12    106.000000                                   Action|Adventure   
13    151.000000                           Action|Adventure|Fantasy   
14    150.000000                           Action|Adventure|Western   
15    143.000000                    Action|Adventure|Fantasy|Sci-Fi   
16    150.000000                    Action|Adventure|Family|Fantasy   
17    173.000000                            Action|Adventure|Sci-Fi   
18    136.000000                           Action|Adventure|Fantasy   
19    106.000000      Action|Adventure|Comedy|Family|Fantasy|Sci-Fi   
20    164.000000                                  Adventure|Fantasy   
21    153.000000                           Action|Adventure|Fantasy   
22    156.000000                     Action|Adventure|Drama|History   
23    186.000000                                  Adventure|Fantasy   
24    113.000000                           Adventure|Family|Fantasy   
25    201.000000                     Action|Adventure|Drama|Romance   
26    194.000000                                      Drama|Romance   
27    147.000000                            Action|Adventure|Sci-Fi   
28    131.000000                   Action|Adventure|Sci-Fi|Thriller   
29    124.000000                   Action|Adventure|Sci-Fi|Thriller   
         ...                                                ...   
5013   79.000000                                       Drama|Family   
5014   80.000000                              Action|Crime|Thriller   
5015  100.000000                                       Comedy|Drama   
5016   90.000000                               Crime|Drama|Thriller   
5017   90.000000                                     Comedy|Romance   
5018  120.000000                                              Drama   
5019   91.000000                            Horror|Mystery|Thriller   
5020  143.000000                              Drama|Horror|Thriller   
5021   85.000000                               Comedy|Drama|Romance   
5022   60.000000                                              Drama   
5023   88.000000                                            Romance   
5024   78.000000                                    Sci-Fi|Thriller   
5025  108.000000                                Comedy|Crime|Horror   
5026  110.000000                                Drama|Music|Romance   
5027   90.000000                                              Drama   
5028   83.000000                                             Horror   
5029  111.000000                      Crime|Horror|Mystery|Thriller   
5030   84.000000                                              Drama   
5031   82.000000                             Comedy|Horror|Thriller   
5032   98.000000                                        Crime|Drama   
5033   77.000000                              Drama|Sci-Fi|Thriller   
5034   80.000000                                           Thriller   
5035   81.000000                Action|Crime|Drama|Romance|Thriller   
5036   84.000000                                        Crime|Drama   
5037   95.000000                                       Comedy|Drama   
5038   87.000000                                       Comedy|Drama   
5039   43.000000                       Crime|Drama|Mystery|Thriller   
5040   76.000000                              Drama|Horror|Thriller   
5041  100.000000                               Comedy|Drama|Romance   
5042   90.000000                                        Documentary   

                                            movie_title  num_voted_users  \
0                                              AvatarÂ            886204   
1            Pirates of the Caribbean: At World's EndÂ            471220   
2                                             SpectreÂ            275868   
3                               The Dark Knight RisesÂ           1144337   
4     Star Wars: Episode VII - The Force AwakensÂ   ...                8   
5                                         John CarterÂ            212204   
6                                        Spider-Man 3Â            383056   
7                                             TangledÂ            294810   
8                             Avengers: Age of UltronÂ            462669   
9              Harry Potter and the Half-Blood PrinceÂ            321795   
10                 Batman v Superman: Dawn of JusticeÂ            371639   
11                                   Superman ReturnsÂ            240396   
12                                  Quantum of SolaceÂ            330784   
13         Pirates of the Caribbean: Dead Man's ChestÂ            522040   
14                                    The Lone RangerÂ            181792   
15                                       Man of SteelÂ            548573   
16           The Chronicles of Narnia: Prince CaspianÂ            149922   
17                                       The AvengersÂ            995415   
18        Pirates of the Caribbean: On Stranger TidesÂ            370704   
19                                     Men in Black 3Â            268154   
20          The Hobbit: The Battle of the Five ArmiesÂ            354228   
21                             The Amazing Spider-ManÂ            451803   
22                                         Robin HoodÂ            211765   
23                The Hobbit: The Desolation of SmaugÂ            483540   
24                                 The Golden CompassÂ            149019   
25                                          King KongÂ            316018   
26                                            TitanicÂ            793059   
27                         Captain America: Civil WarÂ            272670   
28                                         BattleshipÂ            202382   
29                                     Jurassic WorldÂ            418214   
                                                ...              ...   
5013                                           ManitoÂ               493   
5014                                          RampageÂ             15091   
5015                                          SlackerÂ             15103   
5016                                      Dutch KillsÂ                57   
5017                                        Dry SpellÂ               114   
5018                                         FlywheelÂ              2986   
5019                                           ExeterÂ              3836   
5020                                       The RidgesÂ               125   
5021                                  The Puffy ChairÂ              4067   
5022                             Stories of Our LivesÂ                70   
5023                                 Breaking UpwardsÂ              1194   
5024                         All Superheroes Must DieÂ              1771   
5025                                   Pink FlamingosÂ             16792   
5026                                            CleanÂ              3924   
5027                                       The CircleÂ              4555   
5028                                      Tin Can ManÂ                57   
5029                                         The CureÂ              6318   
5030                                   On the DownlowÂ               156   
5031                     Sanctuary; Quite a ConundrumÂ               133   
5032                                             BangÂ               438   
5033                                           PrimerÂ             72639   
5034                                           CaviteÂ               589   
5035                                      El MariachiÂ             52055   
5036                                  The Mongol KingÂ                36   
5037                                        NewlywedsÂ              1338   
5038                          Signed Sealed DeliveredÂ               629   
5039                        The FollowingÂ                         73839   
5040                             A Plague So PleasantÂ                38   
5041                                 Shanghai CallingÂ              1255   
5042                                My Date with DrewÂ              4285   

      cast_total_facebook_likes  \
0                          4834   
1                         48350   
2                         11700   
3                        106759   
4                           143   
5                          1873   
6                         46055   
7                          2036   
8                         92000   
9                         58753   
10                        24450   
11                        29991   
12                         2023   
13                        48486   
14                        45757   
15                        20495   
16                        22697   
17                        87697   
18                        54083   
19                        12572   
20                         9152   
21                        28489   
22                         3244   
23                         9152   
24                        24106   
25                         7123   
26                        45223   
27                        64798   
28                        26679   
29                         8458   
                        ...   
5013                        243   
5014                       3197   
5015                          5   
5016                        366   
5017                        841   
5018                        108   
5019                       2679   
5020                        770   
5021                       1064   
5022                        170   
5023                       1546   
5024                        674   
5025                        760   
5026                        776   
5027                          5   
5028                         15   
5029                        115   
5030                         62   
5031                       1111   
5032                       1186   
5033                        368   
5034                          0   
5035                        147   
5036                         93   
5037                        690   
5038                       2283   
5039                       1753   
5040                          0   
5041                       2386   
5042                        163   

                                        movie_imdb_link      country  \
0     http://www.imdb.com/title/tt0499549/?ref_=fn_t...          USA   
1     http://www.imdb.com/title/tt0449088/?ref_=fn_t...          USA   
2     http://www.imdb.com/title/tt2379713/?ref_=fn_t...           UK   
3     http://www.imdb.com/title/tt1345836/?ref_=fn_t...          USA   
4     http://www.imdb.com/title/tt5289954/?ref_=fn_t...                
5     http://www.imdb.com/title/tt0401729/?ref_=fn_t...          USA   
6     http://www.imdb.com/title/tt0413300/?ref_=fn_t...          USA   
7     http://www.imdb.com/title/tt0398286/?ref_=fn_t...          USA   
8     http://www.imdb.com/title/tt2395427/?ref_=fn_t...          USA   
9     http://www.imdb.com/title/tt0417741/?ref_=fn_t...           UK   
10    http://www.imdb.com/title/tt2975590/?ref_=fn_t...          USA   
11    http://www.imdb.com/title/tt0348150/?ref_=fn_t...          USA   
12    http://www.imdb.com/title/tt0830515/?ref_=fn_t...           UK   
13    http://www.imdb.com/title/tt0383574/?ref_=fn_t...          USA   
14    http://www.imdb.com/title/tt1210819/?ref_=fn_t...          USA   
15    http://www.imdb.com/title/tt0770828/?ref_=fn_t...          USA   
16    http://www.imdb.com/title/tt0499448/?ref_=fn_t...          USA   
17    http://www.imdb.com/title/tt0848228/?ref_=fn_t...          USA   
18    http://www.imdb.com/title/tt1298650/?ref_=fn_t...          USA   
19    http://www.imdb.com/title/tt1409024/?ref_=fn_t...          USA   
20    http://www.imdb.com/title/tt2310332/?ref_=fn_t...  New Zealand   
21    http://www.imdb.com/title/tt0948470/?ref_=fn_t...          USA   
22    http://www.imdb.com/title/tt0955308/?ref_=fn_t...          USA   
23    http://www.imdb.com/title/tt1170358/?ref_=fn_t...          USA   
24    http://www.imdb.com/title/tt0385752/?ref_=fn_t...          USA   
25    http://www.imdb.com/title/tt0360717/?ref_=fn_t...  New Zealand   
26    http://www.imdb.com/title/tt0120338/?ref_=fn_t...          USA   
27    http://www.imdb.com/title/tt3498820/?ref_=fn_t...          USA   
28    http://www.imdb.com/title/tt1440129/?ref_=fn_t...          USA   
29    http://www.imdb.com/title/tt0369610/?ref_=fn_t...          USA   
                                                ...          ...   
5013  http://www.imdb.com/title/tt0298050/?ref_=fn_t...          USA   
5014  http://www.imdb.com/title/tt1337057/?ref_=fn_t...       Canada   
5015  http://www.imdb.com/title/tt0102943/?ref_=fn_t...          USA   
5016  http://www.imdb.com/title/tt2759066/?ref_=fn_t...          USA   
5017  http://www.imdb.com/title/tt2375036/?ref_=fn_t...          USA   
5018  http://www.imdb.com/title/tt0425027/?ref_=fn_t...          USA   
5019  http://www.imdb.com/title/tt1945044/?ref_=fn_t...          USA   
5020  http://www.imdb.com/title/tt1781935/?ref_=fn_t...          USA   
5021  http://www.imdb.com/title/tt0436689/?ref_=fn_t...          USA   
5022  http://www.imdb.com/title/tt3973612/?ref_=fn_t...        Kenya   
5023  http://www.imdb.com/title/tt1247644/?ref_=fn_t...          USA   
5024  http://www.imdb.com/title/tt1836212/?ref_=fn_t...          USA   
5025  http://www.imdb.com/title/tt0069089/?ref_=fn_t...          USA   
5026  http://www.imdb.com/title/tt0388838/?ref_=fn_t...       France   
5027  http://www.imdb.com/title/tt0255094/?ref_=fn_t...         Iran   
5028  http://www.imdb.com/title/tt1235811/?ref_=fn_t...      Ireland   
5029  http://www.imdb.com/title/tt0123948/?ref_=fn_t...        Japan   
5030  http://www.imdb.com/title/tt0390323/?ref_=fn_t...          USA   
5031  http://www.imdb.com/title/tt2049518/?ref_=fn_t...          USA   
5032  http://www.imdb.com/title/tt0109266/?ref_=fn_t...          USA   
5033  http://www.imdb.com/title/tt0390384/?ref_=fn_t...          USA   
5034  http://www.imdb.com/title/tt0428303/?ref_=fn_t...  Philippines   
5035  http://www.imdb.com/title/tt0104815/?ref_=fn_t...          USA   
5036  http://www.imdb.com/title/tt0430371/?ref_=fn_t...          USA   
5037  http://www.imdb.com/title/tt1880418/?ref_=fn_t...          USA   
5038  http://www.imdb.com/title/tt3000844/?ref_=fn_t...       Canada   
5039  http://www.imdb.com/title/tt2071645/?ref_=fn_t...          USA   
5040  http://www.imdb.com/title/tt2107644/?ref_=fn_t...          USA   
5041  http://www.imdb.com/title/tt2070597/?ref_=fn_t...          USA   
5042  http://www.imdb.com/title/tt0378407/?ref_=fn_t...          USA   

      imdb_score  movie_facebook_likes  
0            7.9                 33000  
1            7.1                     0  
2            6.8                 85000  
3            8.5                164000  
4            7.1                     0  
5            6.6                 24000  
6            6.2                     0  
7            7.8                 29000  
8            7.5                118000  
9            7.5                 10000  
10           6.9                197000  
11           6.1                     0  
12           6.7                     0  
13           7.3                  5000  
14           6.5                 48000  
15           7.2                118000  
16           6.6                     0  
17           8.1                123000  
18           6.7                 58000  
19           6.8                 40000  
20           7.5                 65000  
21           7.0                 56000  
22           6.7                 17000  
23           7.9                 83000  
24           6.1                     0  
25           7.2                     0  
26           7.7                 26000  
27           8.2                 72000  
28           5.9                 44000  
29           7.0                150000  
         ...                   ...  
5013         7.0                    61  
5014         6.3                     0  
5015         7.1                  2000  
5016         4.8                    33  
5017         3.3                   200  
5018         6.9                   725  
5019         4.6                     0  
5020         3.0                    33  
5021         6.6                   297  
5022         7.4                    45  
5023         6.2                   324  
5024         4.0                   835  
5025         6.1                     0  
5026         6.9                   171  
5027         7.5                   697  
5028         6.7                   105  
5029         7.4                   817  
5030         6.1                    22  
5031         5.4                   424  
5032         6.4                    20  
5033         7.0                 19000  
5034         6.3                    74  
5035         6.9                     0  
5036         7.8                     4  
5037         6.4                   413  
5038         7.7                    84  
5039         7.5                 32000  
5040         6.3                    16  
5041         6.3                   660  
5042         6.6                   456  

[5043 rows x 9 columns]

ds1.dropna(axis=1, how='any')
Out[46]: 
        duration                                             genres  \
0     178.000000                    Action|Adventure|Fantasy|Sci-Fi   
1     169.000000                           Action|Adventure|Fantasy   
2     148.000000                          Action|Adventure|Thriller   
3     164.000000                                    Action|Thriller   
4     107.201074                                        Documentary   
5     132.000000                            Action|Adventure|Sci-Fi   
6     156.000000                           Action|Adventure|Romance   
7     100.000000  Adventure|Animation|Comedy|Family|Fantasy|Musi...   
8     141.000000                            Action|Adventure|Sci-Fi   
9     153.000000                   Adventure|Family|Fantasy|Mystery   
10    183.000000                            Action|Adventure|Sci-Fi   
11    169.000000                            Action|Adventure|Sci-Fi   
12    106.000000                                   Action|Adventure   
13    151.000000                           Action|Adventure|Fantasy   
14    150.000000                           Action|Adventure|Western   
15    143.000000                    Action|Adventure|Fantasy|Sci-Fi   
16    150.000000                    Action|Adventure|Family|Fantasy   
17    173.000000                            Action|Adventure|Sci-Fi   
18    136.000000                           Action|Adventure|Fantasy   
19    106.000000      Action|Adventure|Comedy|Family|Fantasy|Sci-Fi   
20    164.000000                                  Adventure|Fantasy   
21    153.000000                           Action|Adventure|Fantasy   
22    156.000000                     Action|Adventure|Drama|History   
23    186.000000                                  Adventure|Fantasy   
24    113.000000                           Adventure|Family|Fantasy   
25    201.000000                     Action|Adventure|Drama|Romance   
26    194.000000                                      Drama|Romance   
27    147.000000                            Action|Adventure|Sci-Fi   
28    131.000000                   Action|Adventure|Sci-Fi|Thriller   
29    124.000000                   Action|Adventure|Sci-Fi|Thriller   
         ...                                                ...   
5013   79.000000                                       Drama|Family   
5014   80.000000                              Action|Crime|Thriller   
5015  100.000000                                       Comedy|Drama   
5016   90.000000                               Crime|Drama|Thriller   
5017   90.000000                                     Comedy|Romance   
5018  120.000000                                              Drama   
5019   91.000000                            Horror|Mystery|Thriller   
5020  143.000000                              Drama|Horror|Thriller   
5021   85.000000                               Comedy|Drama|Romance   
5022   60.000000                                              Drama   
5023   88.000000                                            Romance   
5024   78.000000                                    Sci-Fi|Thriller   
5025  108.000000                                Comedy|Crime|Horror   
5026  110.000000                                Drama|Music|Romance   
5027   90.000000                                              Drama   
5028   83.000000                                             Horror   
5029  111.000000                      Crime|Horror|Mystery|Thriller   
5030   84.000000                                              Drama   
5031   82.000000                             Comedy|Horror|Thriller   
5032   98.000000                                        Crime|Drama   
5033   77.000000                              Drama|Sci-Fi|Thriller   
5034   80.000000                                           Thriller   
5035   81.000000                Action|Crime|Drama|Romance|Thriller   
5036   84.000000                                        Crime|Drama   
5037   95.000000                                       Comedy|Drama   
5038   87.000000                                       Comedy|Drama   
5039   43.000000                       Crime|Drama|Mystery|Thriller   
5040   76.000000                              Drama|Horror|Thriller   
5041  100.000000                               Comedy|Drama|Romance   
5042   90.000000                                        Documentary   

                                            movie_title  num_voted_users  \
0                                              AvatarÂ            886204   
1            Pirates of the Caribbean: At World's EndÂ            471220   
2                                             SpectreÂ            275868   
3                               The Dark Knight RisesÂ           1144337   
4     Star Wars: Episode VII - The Force AwakensÂ   ...                8   
5                                         John CarterÂ            212204   
6                                        Spider-Man 3Â            383056   
7                                             TangledÂ            294810   
8                             Avengers: Age of UltronÂ            462669   
9              Harry Potter and the Half-Blood PrinceÂ            321795   
10                 Batman v Superman: Dawn of JusticeÂ            371639   
11                                   Superman ReturnsÂ            240396   
12                                  Quantum of SolaceÂ            330784   
13         Pirates of the Caribbean: Dead Man's ChestÂ            522040   
14                                    The Lone RangerÂ            181792   
15                                       Man of SteelÂ            548573   
16           The Chronicles of Narnia: Prince CaspianÂ            149922   
17                                       The AvengersÂ            995415   
18        Pirates of the Caribbean: On Stranger TidesÂ            370704   
19                                     Men in Black 3Â            268154   
20          The Hobbit: The Battle of the Five ArmiesÂ            354228   
21                             The Amazing Spider-ManÂ            451803   
22                                         Robin HoodÂ            211765   
23                The Hobbit: The Desolation of SmaugÂ            483540   
24                                 The Golden CompassÂ            149019   
25                                          King KongÂ            316018   
26                                            TitanicÂ            793059   
27                         Captain America: Civil WarÂ            272670   
28                                         BattleshipÂ            202382   
29                                     Jurassic WorldÂ            418214   
                                                ...              ...   
5013                                           ManitoÂ               493   
5014                                          RampageÂ             15091   
5015                                          SlackerÂ             15103   
5016                                      Dutch KillsÂ                57   
5017                                        Dry SpellÂ               114   
5018                                         FlywheelÂ              2986   
5019                                           ExeterÂ              3836   
5020                                       The RidgesÂ               125   
5021                                  The Puffy ChairÂ              4067   
5022                             Stories of Our LivesÂ                70   
5023                                 Breaking UpwardsÂ              1194   
5024                         All Superheroes Must DieÂ              1771   
5025                                   Pink FlamingosÂ             16792   
5026                                            CleanÂ              3924   
5027                                       The CircleÂ              4555   
5028                                      Tin Can ManÂ                57   
5029                                         The CureÂ              6318   
5030                                   On the DownlowÂ               156   
5031                     Sanctuary; Quite a ConundrumÂ               133   
5032                                             BangÂ               438   
5033                                           PrimerÂ             72639   
5034                                           CaviteÂ               589   
5035                                      El MariachiÂ             52055   
5036                                  The Mongol KingÂ                36   
5037                                        NewlywedsÂ              1338   
5038                          Signed Sealed DeliveredÂ               629   
5039                        The FollowingÂ                         73839   
5040                             A Plague So PleasantÂ                38   
5041                                 Shanghai CallingÂ              1255   
5042                                My Date with DrewÂ              4285   

      cast_total_facebook_likes  \
0                          4834   
1                         48350   
2                         11700   
3                        106759   
4                           143   
5                          1873   
6                         46055   
7                          2036   
8                         92000   
9                         58753   
10                        24450   
11                        29991   
12                         2023   
13                        48486   
14                        45757   
15                        20495   
16                        22697   
17                        87697   
18                        54083   
19                        12572   
20                         9152   
21                        28489   
22                         3244   
23                         9152   
24                        24106   
25                         7123   
26                        45223   
27                        64798   
28                        26679   
29                         8458   
                        ...   
5013                        243   
5014                       3197   
5015                          5   
5016                        366   
5017                        841   
5018                        108   
5019                       2679   
5020                        770   
5021                       1064   
5022                        170   
5023                       1546   
5024                        674   
5025                        760   
5026                        776   
5027                          5   
5028                         15   
5029                        115   
5030                         62   
5031                       1111   
5032                       1186   
5033                        368   
5034                          0   
5035                        147   
5036                         93   
5037                        690   
5038                       2283   
5039                       1753   
5040                          0   
5041                       2386   
5042                        163   

                                        movie_imdb_link      country  \
0     http://www.imdb.com/title/tt0499549/?ref_=fn_t...          USA   
1     http://www.imdb.com/title/tt0449088/?ref_=fn_t...          USA   
2     http://www.imdb.com/title/tt2379713/?ref_=fn_t...           UK   
3     http://www.imdb.com/title/tt1345836/?ref_=fn_t...          USA   
4     http://www.imdb.com/title/tt5289954/?ref_=fn_t...                
5     http://www.imdb.com/title/tt0401729/?ref_=fn_t...          USA   
6     http://www.imdb.com/title/tt0413300/?ref_=fn_t...          USA   
7     http://www.imdb.com/title/tt0398286/?ref_=fn_t...          USA   
8     http://www.imdb.com/title/tt2395427/?ref_=fn_t...          USA   
9     http://www.imdb.com/title/tt0417741/?ref_=fn_t...           UK   
10    http://www.imdb.com/title/tt2975590/?ref_=fn_t...          USA   
11    http://www.imdb.com/title/tt0348150/?ref_=fn_t...          USA   
12    http://www.imdb.com/title/tt0830515/?ref_=fn_t...           UK   
13    http://www.imdb.com/title/tt0383574/?ref_=fn_t...          USA   
14    http://www.imdb.com/title/tt1210819/?ref_=fn_t...          USA   
15    http://www.imdb.com/title/tt0770828/?ref_=fn_t...          USA   
16    http://www.imdb.com/title/tt0499448/?ref_=fn_t...          USA   
17    http://www.imdb.com/title/tt0848228/?ref_=fn_t...          USA   
18    http://www.imdb.com/title/tt1298650/?ref_=fn_t...          USA   
19    http://www.imdb.com/title/tt1409024/?ref_=fn_t...          USA   
20    http://www.imdb.com/title/tt2310332/?ref_=fn_t...  New Zealand   
21    http://www.imdb.com/title/tt0948470/?ref_=fn_t...          USA   
22    http://www.imdb.com/title/tt0955308/?ref_=fn_t...          USA   
23    http://www.imdb.com/title/tt1170358/?ref_=fn_t...          USA   
24    http://www.imdb.com/title/tt0385752/?ref_=fn_t...          USA   
25    http://www.imdb.com/title/tt0360717/?ref_=fn_t...  New Zealand   
26    http://www.imdb.com/title/tt0120338/?ref_=fn_t...          USA   
27    http://www.imdb.com/title/tt3498820/?ref_=fn_t...          USA   
28    http://www.imdb.com/title/tt1440129/?ref_=fn_t...          USA   
29    http://www.imdb.com/title/tt0369610/?ref_=fn_t...          USA   
                                                ...          ...   
5013  http://www.imdb.com/title/tt0298050/?ref_=fn_t...          USA   
5014  http://www.imdb.com/title/tt1337057/?ref_=fn_t...       Canada   
5015  http://www.imdb.com/title/tt0102943/?ref_=fn_t...          USA   
5016  http://www.imdb.com/title/tt2759066/?ref_=fn_t...          USA   
5017  http://www.imdb.com/title/tt2375036/?ref_=fn_t...          USA   
5018  http://www.imdb.com/title/tt0425027/?ref_=fn_t...          USA   
5019  http://www.imdb.com/title/tt1945044/?ref_=fn_t...          USA   
5020  http://www.imdb.com/title/tt1781935/?ref_=fn_t...          USA   
5021  http://www.imdb.com/title/tt0436689/?ref_=fn_t...          USA   
5022  http://www.imdb.com/title/tt3973612/?ref_=fn_t...        Kenya   
5023  http://www.imdb.com/title/tt1247644/?ref_=fn_t...          USA   
5024  http://www.imdb.com/title/tt1836212/?ref_=fn_t...          USA   
5025  http://www.imdb.com/title/tt0069089/?ref_=fn_t...          USA   
5026  http://www.imdb.com/title/tt0388838/?ref_=fn_t...       France   
5027  http://www.imdb.com/title/tt0255094/?ref_=fn_t...         Iran   
5028  http://www.imdb.com/title/tt1235811/?ref_=fn_t...      Ireland   
5029  http://www.imdb.com/title/tt0123948/?ref_=fn_t...        Japan   
5030  http://www.imdb.com/title/tt0390323/?ref_=fn_t...          USA   
5031  http://www.imdb.com/title/tt2049518/?ref_=fn_t...          USA   
5032  http://www.imdb.com/title/tt0109266/?ref_=fn_t...          USA   
5033  http://www.imdb.com/title/tt0390384/?ref_=fn_t...          USA   
5034  http://www.imdb.com/title/tt0428303/?ref_=fn_t...  Philippines   
5035  http://www.imdb.com/title/tt0104815/?ref_=fn_t...          USA   
5036  http://www.imdb.com/title/tt0430371/?ref_=fn_t...          USA   
5037  http://www.imdb.com/title/tt1880418/?ref_=fn_t...          USA   
5038  http://www.imdb.com/title/tt3000844/?ref_=fn_t...       Canada   
5039  http://www.imdb.com/title/tt2071645/?ref_=fn_t...          USA   
5040  http://www.imdb.com/title/tt2107644/?ref_=fn_t...          USA   
5041  http://www.imdb.com/title/tt2070597/?ref_=fn_t...          USA   
5042  http://www.imdb.com/title/tt0378407/?ref_=fn_t...          USA   

      imdb_score  movie_facebook_likes  
0            7.9                 33000  
1            7.1                     0  
2            6.8                 85000  
3            8.5                164000  
4            7.1                     0  
5            6.6                 24000  
6            6.2                     0  
7            7.8                 29000  
8            7.5                118000  
9            7.5                 10000  
10           6.9                197000  
11           6.1                     0  
12           6.7                     0  
13           7.3                  5000  
14           6.5                 48000  
15           7.2                118000  
16           6.6                     0  
17           8.1                123000  
18           6.7                 58000  
19           6.8                 40000  
20           7.5                 65000  
21           7.0                 56000  
22           6.7                 17000  
23           7.9                 83000  
24           6.1                     0  
25           7.2                     0  
26           7.7                 26000  
27           8.2                 72000  
28           5.9                 44000  
29           7.0                150000  
         ...                   ...  
5013         7.0                    61  
5014         6.3                     0  
5015         7.1                  2000  
5016         4.8                    33  
5017         3.3                   200  
5018         6.9                   725  
5019         4.6                     0  
5020         3.0                    33  
5021         6.6                   297  
5022         7.4                    45  
5023         6.2                   324  
5024         4.0                   835  
5025         6.1                     0  
5026         6.9                   171  
5027         7.5                   697  
5028         6.7                   105  
5029         7.4                   817  
5030         6.1                    22  
5031         5.4                   424  
5032         6.4                    20  
5033         7.0                 19000  
5034         6.3                    74  
5035         6.9                     0  
5036         7.8                     4  
5037         6.4                   413  
5038         7.7                    84  
5039         7.5                 32000  
5040         6.3                    16  
5041         6.3                   660  
5042         6.6                   456  

[5043 rows x 9 columns]

ds1.dropna(axis=2, how='all')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-47-4a5c0e636948> in <module>()
----> 1 ds1.dropna(axis=2, how='all')

/home/unix/.local/share/canopy/edm/envs/User/lib/python3.5/site-packages/pandas/core/frame.py in dropna(self, axis, how, thresh, subset, inplace)
   4274                                        axis=ax)
   4275         else:
-> 4276             axis = self._get_axis_number(axis)
   4277             agg_axis = 1 - axis
   4278 
/home/unix/.local/share/canopy/edm/envs/User/lib/python3.5/site-packages/pandas/core/generic.py in _get_axis_number(self, axis)
    372                 pass
    373         raise ValueError('No axis named {0} for object type {1}'
--> 374                          .format(axis, type(self)))
    375 
    376     def _get_axis_name(self, axis):
ValueError: No axis named 2 for object type <class 'pandas.core.frame.DataFrame'> 

