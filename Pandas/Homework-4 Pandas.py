# Gerekli kütüphaneleri içe aktaralım
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleyelim
df = pd.read_csv('c:/Users/LENOVO/Desktop/YZ_Python/Pandas/datas/agrofood_co2_emission.csv')

# Gereksiz sütunları kaldır
columns_to_drop = ['Crop Residues', 'Rice Cultivation', 'Drained organic soils (CO2)', 
                   'Pesticides Manufacturing', 'On-farm Electricity Use']
df = df.drop(columns=columns_to_drop)

# Veri setindeki sütun başlıklarını kontrol edelim
print("Veri Setinin İlk 5 Satırı:")
print(df.head().to_string())

# Forest fires sütununun varlığını kontrol edelim
if "Forest fires" not in df.columns:
    raise ValueError("Veri setinde 'Forest fires' sütunu bulunamadı!")

# Forest fires sütunundaki eksik değerleri kontrol edelim
if df["Forest fires"].isnull().any():
    print("Uyarı: 'Forest fires' sütununda eksik değerler bulunuyor. Eksik değerler 0 ile doldurulacak.")
    df["Forest fires"].fillna(0, inplace=True)

# Ülkeleri kıtalarla eşleştirmek için bir kıta haritası oluşturalım
continent_map = {
    "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic",
               "Chad", "Comoros", "Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
               "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya",
               "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria",
               "Republic of the Congo", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa",
               "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    
    "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia",
             "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon",
             "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines",
             "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand", "Timor-Leste", "Turkey",
             "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    
    "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czechia", "Denmark",
               "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein",
               "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
               "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
               "Ukraine", "United Kingdom", "Vatican City"],
    
    "North America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic",
                      "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
                      "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"],
    "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    
    "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea",
                "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
}

# Kıtalar için ters harita (Ülke -> Kıta)
country_to_continent = {country: continent for continent, countries in continent_map.items() for country in countries}

# Veri setine kıta bilgisi ekleyelim
df["Continent"] = df["Area"].map(country_to_continent)

# Kıtalar bazında toplam emisyon değerlerini hesaplayalım
continent_emissions = df.groupby("Continent")["total_emission"].sum().reset_index()

# Sonuçları görelim
print("\nKıtalara Göre Toplam Emisyon Değerleri:")
print(continent_emissions)

# Kıta bazında toplam karbon emisyonları (ton cinsinden)
continents = continent_emissions["Continent"]
emissions = continent_emissions["total_emission"]

# Bar chart oluşturma
plt.figure(figsize=(10, 6))
plt.bar(continents, emissions, color=["#0077b6", "#00b4d8", "#90e0ef", "#b5e48c", "#fdfcdc", "#9c6644"])
plt.title("Kıtalara Göre Toplam Karbon Emisyonları", fontsize=14, color='r')
plt.xlabel("Kıtalar", fontsize=12)
plt.ylabel("Toplam Emisyon (ton)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# Orman yangınları verisini analiz edelim
forest_fires_by_continent = df.groupby("Continent")["Forest fires"].sum().reset_index()

# Dilimleri birbirinden ayırmak için explode parametresi
explode = [0.1 if continent in ["Oceania", "North America"] else 0 for continent in forest_fires_by_continent["Continent"]]

# Pie chart oluşturma
plt.figure(figsize=(12, 12))  # Grafik boyutunu büyütüyoruz
wedges, texts, autotexts = plt.pie(
    forest_fires_by_continent["Forest fires"], 
    labels=forest_fires_by_continent["Continent"], 
    autopct='%1.1f%%',  # Tüm yüzdelik değerlerini göster
    startangle=140, 
    colors=["#0077b6", "#00b4d8", "#90e0ef", "#b5e48c", "#fdfcdc", "#9c6644"],
    pctdistance=0.8,  # Yüzdeliklerin konumunu ayarlamak
    labeldistance=1.05,  # Etiketlerin konumunu ayarlamak
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},  # Dilimlere siyah kenarlık eklemek
    textprops={'fontsize': 12, 'color': 'black'},  # Yazı boyutunu ve rengini ayarlamak
    explode=explode  # Küçük dilimleri birbirinden ayır
)

# Yüzdeliklerin daha okunaklı olması için yazı boyutlarını ayarlayalım
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color("black")

# Etiketlerin daha okunaklı olması için yazı boyutlarını ayarlayalım
for text in texts:
    text.set_fontsize(12)

# Grafik başlığı
plt.title("Kıtalara Göre Orman Yangınlarından Kaynaklanan Emisyonlar", fontsize=16, color='b', pad=20)

# Grafik gösterimi
plt.tight_layout()  # Grafik öğelerinin birbirine girmesini önlemek için
plt.show()

# Ek Analiz: Yıllara Göre Emisyon Trendleri
yearly_emissions = df.groupby("Year")["total_emission"].sum().reset_index()

# Yıllara göre emisyon trendlerini çizelim
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_emissions, x="Year", y="total_emission", marker="o", color="b")
plt.title("Yıllara Göre Toplam Karbon Emisyon Trendleri", fontsize=14, color='r')
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("Toplam Emisyon (ton)", fontsize=12)
plt.grid(linestyle='--', alpha=0.5)
plt.show()

# Ek Analiz: Kıtalara Göre Yıllık Emisyon Trendleri
continent_yearly_emissions = df.groupby(["Continent", "Year"])["total_emission"].sum().reset_index()

# Kıtalara göre yıllık emisyon trendlerini çizelim
plt.figure(figsize=(14, 8))
sns.lineplot(data=continent_yearly_emissions, x="Year", y="total_emission", hue="Continent", style="Continent", markers=True, dashes=False)
plt.title("Kıtalara Göre Yıllık Karbon Emisyon Trendleri", fontsize=14, color='r')
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("Toplam Emisyon (ton)", fontsize=12)
plt.grid(linestyle='--', alpha=0.5)
plt.legend(title="Kıta", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()