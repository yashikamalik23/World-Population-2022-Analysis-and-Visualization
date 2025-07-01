Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\Yashika malik\AppData\Local\Programs\Python\Python312\Task2.py
     Rank CCA3  ... Growth Rate World Population Percentage
0      36  AFG  ...      1.0257                        0.52
1     138  ALB  ...      0.9957                        0.04
2      34  DZA  ...      1.0164                        0.56
3     213  ASM  ...      0.9831                        0.00
4     203  AND  ...      1.0100                        0.00
..    ...  ...  ...         ...                         ...
229   226  WLF  ...      0.9953                        0.00
230   172  ESH  ...      1.0184                        0.01
231    46  YEM  ...      1.0217                        0.42
232    63  ZMB  ...      1.0280                        0.25
233    74  ZWE  ...      1.0204                        0.20

[234 rows x 17 columns]
   Rank CCA3  ... Growth Rate World Population Percentage
0    36  AFG  ...      1.0257                        0.52
1   138  ALB  ...      0.9957                        0.04
2    34  DZA  ...      1.0164                        0.56
3   213  ASM  ...      0.9831                        0.00
4   203  AND  ...      1.0100                        0.00

[5 rows x 17 columns]
     Rank CCA3  ... Growth Rate World Population Percentage
229   226  WLF  ...      0.9953                        0.00
230   172  ESH  ...      1.0184                        0.01
231    46  YEM  ...      1.0217                        0.42
232    63  ZMB  ...      1.0280                        0.25
233    74  ZWE  ...      1.0204                        0.20

[5 rows x 17 columns]
Shape of dataset: (234, 17)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 234 entries, 0 to 233
Data columns (total 17 columns):
 #   Column                       Non-Null Count  Dtype  
---  ------                       --------------  -----  
 0   Rank                         234 non-null    int64  
 1   CCA3                         234 non-null    object 
 2   Country/Territory            234 non-null    object 
 3   Capital                      234 non-null    object 
 4   Continent                    234 non-null    object 
 5   2022 Population              234 non-null    int64  
 6   2020 Population              234 non-null    int64  
 7   2015 Population              234 non-null    int64  
 8   2010 Population              234 non-null    int64  
 9   2000 Population              234 non-null    int64  
 10  1990 Population              234 non-null    int64  
 11  1980 Population              234 non-null    int64  
 12  1970 Population              234 non-null    int64  
 13  Area (km²)                   234 non-null    int64  
 14  Density (per km²)            234 non-null    float64
 15  Growth Rate                  234 non-null    float64
 16  World Population Percentage  234 non-null    float64
dtypes: float64(3), int64(10), object(4)
memory usage: 31.2+ KB
None
             Rank  2022 Population  ...  Growth Rate  World Population Percentage
count  234.000000     2.340000e+02  ...   234.000000                   234.000000
mean   117.500000     3.407441e+07  ...     1.009577                     0.427051
std     67.694165     1.367664e+08  ...     0.013385                     1.714977
min      1.000000     5.100000e+02  ...     0.912000                     0.000000
25%     59.250000     4.197385e+05  ...     1.001775                     0.010000
50%    117.500000     5.559944e+06  ...     1.007900                     0.070000
75%    175.750000     2.247650e+07  ...     1.016950                     0.280000
max    234.000000     1.425887e+09  ...     1.069100                    17.880000

[8 rows x 13 columns]
Original Columns: Index(['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent',
       '2022 Population', '2020 Population', '2015 Population',
       '2010 Population', '2000 Population', '1990 Population',
       '1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)',
       'Growth Rate', 'World Population Percentage'],
      dtype='object')
Rank                           0
CCA3                           0
Country/Territory              0
Capital                        0
Continent                      0
2022 Population                0
2020 Population                0
2015 Population                0
2010 Population                0
2000 Population                0
1990 Population                0
1980 Population                0
1970 Population                0
Area (km²)                     0
Density (per km²)              0
Growth Rate                    0
World Population Percentage    0
dtype: int64
     Rank CCA3  ... Growth Rate World Population Percentage
0      36  AFG  ...      1.0257                        0.52
1     138  ALB  ...      0.9957                        0.04
2      34  DZA  ...      1.0164                        0.56
3     213  ASM  ...      0.9831                        0.00
4     203  AND  ...      1.0100                        0.00
..    ...  ...  ...         ...                         ...
229   226  WLF  ...      0.9953                        0.00
230   172  ESH  ...      1.0184                        0.01
231    46  YEM  ...      1.0217                        0.42
232    63  ZMB  ...      1.0280                        0.25
233    74  ZWE  ...      1.0204                        0.20

[234 rows x 17 columns]
