import pandas as pd
import numpy as np

# region Intro Pandas

# dictionary = {
#     'A': 1, 
#     'B': 2, 
#     'C': 3,
#     'D': 4,
#     'E': 5,
#     'F': 6
#     }

# pd_series = pd.Series(dictionary)
# print(pd_series)

# print(pd_series[:2]) #ilk iki elemanı gösterir

# print(pd_series.shape) #boyutunu gösterir

# print(pd_series.dtype) #data tipini gösterir

# print(pd_series.ndim) #kaç boyutlu olduğunu gösterir

# print(pd_series.describe()) #istatistiksel bilgileri gösterir

# print(pd_series.head(2)) #ilk iki elemanı gösterir

# print(pd_series.tail(2)) #son iki elemanı gösterir

# print(pd_series >=2) #2 den büyük olanları gösterir

# print(pd_series %2 ==0) #çift olanları gösterir


# dodge_2025 = pd.Series(data=[10, 20], index=['TRX 1500', 'RAW2500'])
# dodge_2024 = pd.Series(data=[5, 15], index=['TRX 1500', 'RAW2500'])

# toplam = dodge_2024 + dodge_2025
# print(toplam)


# #****DataFrame**** 
# df = pd.DataFrame(
#     data=np.random.rand(3, 5), # 3 satır, 5 sütun olacak şekilde rastgele sayılarla doldur
#     index = ['A', 'B', 'C'],
#     columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
# )
# print(df)

# #****Veri seçme****
# print(df['Column2']) # Column2'yi seç
# print(type(df['Column2'])) #Float

# print(df[['Column2']])
# print(type(df[['Column2']])) #DataFrame

# print(df.loc['B']) # B satırını döndürdü
# print(df.loc['C', 'Column3']) # C satırının Column3 sütununu döndürür. nokta atışı yapar
# print(df.loc[:, ['Column1', 'Column2']]) # Tüm satırların Column1 ve Column2 sütunlarını döndürür
# print(
#     df.loc[
#         ['A', 'B'],
#         ['Column1', 'Column2']
#     ]
# ) # A ve B satırlarının Column1 ve Column2 sütunlarını döndürür
# endregion

#region IMDB - Select - Filter
#df = pd.read_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/netflix.csv')

# print(df.head().to_string())

# print(df.shape)

# print(df.describe())

# # Movie_Title ilk 20 satırı listeleyin. 3 farklı yol ile yapıldı.
# print("-------------------------------------------------------------------------------")
# # Path 1 /head
# print(df[['Movie_Title']].head(20))
# print("-------------------------------------------------------------------------------")
# # Path 2  /Slicing
# print(df[['Movie_Title']][0:20])
# print("-------------------------------------------------------------------------------")
# # Path 3 /lock
# print(df.loc[:20, 'Movie_Title'])
# print("-------------------------------------------------------------------------------")

# Duration 50 den büyük olan filmlerin
# select --> Movie_Title, Duration, YR_Released
# 20 ile 50 arasındaki filmler gelsin
# sort edelim

# print(
#     df[df['Duration'] > 50]
#     [['Movie_Title', 'Duration', 'YR_Released']]
#     [20:50].sort_values(by='Duration', ascending=False)
# )
# print("-------------------------------------------------------------------------------")

# # YR_Released 2014 ile 2016 arasında olan
# # Movie_Title, Duration, YR_Released
# print(
#     df[
#         (df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2016)
#     ]
#     [['Movie_Title', 'Duration', 'YR_Released']]
# )
# print("-------------------------------------------------------------------------------")

# print(
#     df[
#         df['YR_Released'].between(2014, 2016)
#     ]
#     [['Movie_Title', 'Duration', 'YR_Released']]
# )
# print("-------------------------------------------------------------------------------")
#endregion

# region NBA - Group By- Select - Filter
# df = pd.read_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/nba.csv')

# print(df.head(20).to_string())
# print(df.shape)
# print("-------------------------------------------------------------------------------")

# # En kilolu oyuncuyu bulalım
# print(
#     df[
#         df['Weight'] == df['Weight'].max()
#     ]
#     [['Name', 'College', 'Height', 'Weight']]
# )
# print("-------------------------------------------------------------------------------")
# # group by
# print(
#     df.groupby(by='College')['Weight'].sum()
# )
# print("-------------------------------------------------------------------------------")

# # Kaç farklı takım var
# print(df['College'].nunique())
# print("-------------------------------------------------------------------------------")

# #
# print(df.groupby(by='College')['Weight'].mean())
# print("-------------------------------------------------------------------------------")


# # # Custom Function
# def str_find(name: str):
#     if name.__contains__('Abdul'):
#         return True
#     else:
#         return False

# print(df['Name'].apply(str_find))
# endregion

#region Youtube
# df = pd.read_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/youtube.csv')

# print(df.head().to_string())
# print(df.shape)
# print(df.columns)

# # # en çok görüntülenme alan il 10 videonun adını, view
# print(
#     df.groupby('title')[['views']].sum().sort_values(by='views', ascending=False).head(10)
# )
# print("-------------------------------------------------------------------------------")

# # title sütununa göre grouplayalım like sayısını saptayalım
# print(
#     df.groupby('title')[['likes']].sum().sort_values(by='likes', ascending=False).head(10)
# )
# print("-------------------------------------------------------------------------------")


# # hangi title' ın  views/likes oranı en yüksek
# print(
#     df.groupby('title')[['commentCount']].sum().sort_values(by='commentCount', ascending=False).head(10)
# )
# print("-------------------------------------------------------------------------------")


# def like_view_ratio(data_set: pd.DataFrame) -> list:
#     like_list = list(data_set['likes'])
#     view_list = list(data_set['views'])

#     comb_list = list(zip(like_list, view_list))
#     avg_like = list()
#     for like, view in comb_list:
#         if like == 0:
#             avg_like.append(0)
#         if view == 0:
#             avg_like.append(0)    
#         else:
#             avg_like.append(like / view)

#     return avg_like

# df['like_view_ratio'] = like_view_ratio(data_set=df)

# print(
#     df.loc[:, ['title', 'likes', 'views', 'like_view_ratio']].sort_values(by='like_view_ratio', ascending=False).head(10)
# )
# endregion

#region Automobil - Handling Missing Values - Data Standardization - Data Normalization - Dummy Variable
# df = pd.read_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/auto.csv')

# df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
#               "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
#               "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
#               "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# print(df.head().to_string())
# print(df.shape)

# # Handling Missing Values
# # Step I
# # Eksik verilerin saptanması
# df.replace(
#     to_replace='?',
#     value=np.nan,
#     inplace=True # Değişiklikleri kaydet
# )
# print("-------------------------------------------------------------------------------")

# missing_values_df = df.isnull() # Eksik verileri saptar. Eksik veri varsa False yazar eksik veri yoksa True yazar
# print(missing_values_df.head().to_string())
# print("-------------------------------------------------------------------------------")

# print(missing_values_df.columns.values.tolist())
# print("-------------------------------------------------------------------------------")

# for item in missing_values_df.columns.values.tolist():
#     print(f'Column Name: {item}\nMissing Values Count: {missing_values_df[item].value_counts()}')
# print("-------------------------------------------------------------------------------")

# # Missing Values Handle
# # 1. Ortalama Değer saptayıp eksik veriler yerine yazdırma
# df['normalized-losses'] = df['normalized-losses'].replace(to_replace=np.nan, value=df['normalized-losses'].astype(float).mean())
# print(df['normalized-losses'])

# # 2. Frekans aralığını saptayarak eksik verilerin yerine yazdırma
# df['num-of-doors'] = df['num-of-doors'].replace(to_replace=np.nan, value=df['num-of-doors'].value_counts().idxmax())
# print(df['num-of-doors'])
# print("-------------------------------------------------------------------------------")

# # Veri Standardizasyonu
# df['city_l/km'] = 235 / df['city-mpg']
# df['highway_l/km'] = 235 / df['highway-mpg']
# print(df[['city_l/km', 'highway_l/km']])
# print("-------------------------------------------------------------------------------")

# # Normalizasyon
# df['length'] = df['length'] / df['length'].max()
# df['width'] = df['width'] / df['width'].max()
# df['height'] = df['height'] / df['height'].max()

# print(df[['length', 'width', 'height']])
# print("-------------------------------------------------------------------------------")

# # Dummy Variable
# dummy_variable_df = pd.get_dummies(df['fuel-type'], dtype=float)
# print(dummy_variable_df)
# print("-------------------------------------------------------------------------------")

# df.to_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/auto_clean_data.csv')
# endregion

# region Canada - Data Visualization - Matplotlib - Openpyxl (Veri Stei Yok)
# import openpyxl
# import matplotlib.pyplot as plt

# df_can = pd.read_excel(
#     io='data/Canada.xlsx',
#     sheet_name='Canada by Citizenship',
#     skiprows=range(20),
#     skipfooter=2
# )

# print(df_can.head().to_string())

# Sütun isimlerini değiştirme
# df_can.rename(
#     columns={
#         'OdName': 'Country',
#         'AreaName': 'Continent',
#         'RegName': 'Region'
#     },
#     inplace=True
# )
# print(df_can.head().to_string())

# çalışmada ihtiyaç duyulmayan gereksiz sütunlarda kurtulalım
# df_can.drop(
#     columns=['Type', 'Coverage', 'AREA', 'REG', 'DEV', 'DevName'],
#     axis=1,  # 1 sütunu, 0 satırı temsil eder
#     inplace=True
# )
# print(df_can.head().to_string())

# sütun başlıklarının tipine
# for column in df_can.columns:
#     print(type(column))

# göçmen sayılarını tutan sütunların başlıklarının tipini int to str yapalım
# df_can.columns = list(map(str, df_can.columns))

# for column in df_can.columns:
#     print(type(column))

# veri setindeki country sütunu index olarak ayarlayalım ki nokta atışı bir ülkenin verisini çekebilellim
# df_can.set_index(keys='Country', inplace=True)
# print(df_can.head().to_string())

# yıl yıl göçmen sayılarını toplayarak total isimli sütun yaratıp içine yazalım
# df_can['Total'] = df_can.sum(axis=1, numeric_only=True)
# print(df_can.head().to_string())

# veri setinde ki yıllar ile bire bir aynı değerlere sahip bir liste oluşturalım
# years = list(map(str, range(1980, 2014)))

# en çok göç vermiş top 5 country saptayalım area grafiğinde gösterelim
# df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
# df_top_5_country = df_can.head()
# print(df_top_5_country.to_string())

# df_top_5_country = df_top_5_country[years].transpose()
# print(df_top_5_country.to_string())

# df_top_5_country.plot(
#     kind='area',
#     figsize=(10, 7),
#     stacked=True,
# )

# plt.title(label='Immigrant of Top 5 Countries', color='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.ylabel(ylabel='Number of Immigrant', c='r')
# plt.grid()
# plt.show()

# histogram grafiği yapalım
# 2013 yılında göçmen vemiş ülkeler

# count, bin_edges = np.histogram(df_can['2013'])
# print(count)
# print(bin_edges)

# df_can['2013'].plot(
#     kind='hist',
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color='b'
# )

# plt.title(label='Immigrant to 2013', color='r')
# plt.xlabel(xlabel='Number of Immigrant', c='r')
# plt.ylabel(ylabel='Number of Country', c='r')
# plt.grid()
# plt.show()

# baltık ülkelerinin 1980 - 2014
# df_baltic_countries = df_can.loc[['Denmark','Norway', 'Sweden'], years].transpose()
# print(df_baltic_countries.head().to_string())

# count, bin_edges = np.histogram(df_baltic_countries, bins=15)
# print(count)
# print(bin_edges)

# df_baltic_countries.plot(
#     kind='hist',
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color=['coral', 'darkblue', 'green'],
#     stacked=False,
#     alpha=0.25
# )

# plt.title(label='Immigrant to 2013', color='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.ylabel(ylabel='Number of Country', c='r')
# plt.grid()
# plt.show()

# Iceland göçmen harketliliğini çubuk grafikte göserelim
# df_iceland = df_can.loc['Iceland', years]

# df_iceland.plot(
#     kind='bar',
#     figsize=(10, 7)
# )

# plt.title(label='Iceland Immigrant from 1980 to 2014', color='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.ylabel(ylabel='Number of Immigrant', c='r')
# plt.grid()
# plt.annotate('',                      # s: str. will leave it blank for no text
#               xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
#               xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
#               xycoords='data',         # will use the coordinate system of the object being annotated
#               arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
#              )

# # # Annotate Text
# plt.annotate('2008 - 2011 Financial Crisis', # text to display
#               xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
#               rotation=72.5,                  # based on trial and error to match the arrow
#               va='bottom',                    # want the text to be vertically 'bottom' aligned
#               ha='left',                      # want the text to be horizontally 'left' algned.
#              )

# plt.show()

# df_continets = df_can.groupby(by='Continent').sum()

# df_continets['Total'].plot(
#     kind='pie',
#     figsize=(10, 7),
#     startangle=90,
#     autopct = '%1.1f%%',
#     labels=None,
#     shadow=True,
#     pctdistance=1.1,
#     explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# )
# plt.axis('equal')
# plt.legend(
#     labels=df_continets.index,
#     prop={
#         'size': 8
#     }
# )
# plt.show()
# endregion
