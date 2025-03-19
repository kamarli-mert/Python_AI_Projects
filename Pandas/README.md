# Agrofood CO2 Emission Analysis

Bu proje, tarım ve gıda sektöründen kaynaklanan karbon emisyonlarını analiz etmek için geliştirilmiştir. Proje, farklı kıtalar ve yıllar bazında karbon emisyonlarını inceleyerek, orman yangınları ve diğer emisyon kaynaklarının etkilerini görselleştirmeyi amaçlamaktadır.

## Proje İçeriği

### 1. Veri Seti
Kullanılan veri seti, tarım ve gıda sektöründen kaynaklanan karbon emisyonlarını içermektedir. Veri setinde aşağıdaki bilgiler bulunmaktadır:
- **Area**: Ülke adı
- **Year**: Yıl
- **Savanna fires**, **Forest fires**: Yangınlardan kaynaklanan emisyonlar
- **Food Transport**, **Food Processing**, **Fertilizers Manufacturing**: Gıda üretimi ve taşımacılığından kaynaklanan emisyonlar
- **total_emission**: Toplam karbon emisyonu
- **Average Temperature °C**: Ortalama sıcaklık

### 2. Yapılan İşlemler
Projede aşağıdaki işlemler gerçekleştirilmiştir:
1. **Gereksiz Sütunların Kaldırılması**: Analiz için gerekli olmayan sütunlar veri setinden çıkarılmıştır.
2. **Eksik Verilerin Doldurulması**: Eksik değerler uygun şekilde doldurulmuştur.
3. **Kıta Bilgisinin Eklenmesi**: Ülkeler kıtalarla eşleştirilerek veri setine kıta bilgisi eklenmiştir.
4. **Kıtalara Göre Toplam Emisyon Analizi**: Her kıtanın toplam karbon emisyonu hesaplanmıştır.
5. **Orman Yangınlarının Analizi**: Orman yangınlarından kaynaklanan emisyonlar kıtalar bazında incelenmiştir.
6. **Yıllara Göre Emisyon Trendleri**: Yıllara göre toplam karbon emisyonu trendleri analiz edilmiştir.
7. **Kıtalara Göre Yıllık Emisyon Trendleri**: Her kıtanın yıllık karbon emisyon trendleri görselleştirilmiştir.

### 3. Görselleştirmeler
Projede aşağıdaki grafikler oluşturulmuştur:
- **Bar Chart**: Kıtalara göre toplam karbon emisyonları
- **Pie Chart**: Kıtalara göre orman yangınlarından kaynaklanan emisyonların yüzdesel dağılımı
- **Line Chart**: Yıllara göre toplam karbon emisyon trendleri
- **Multi-Line Chart**: Kıtalara göre yıllık karbon emisyon trendleri

## Kullanılan Teknolojiler
- **Python**: Veri analizi ve görselleştirme
- **Pandas**: Veri işleme ve analiz
- **Matplotlib**: Grafik oluşturma
- **Seaborn**: Gelişmiş görselleştirme

## Projeyi Çalıştırma
Projeyi çalıştırmak için aşağıdaki adımları izleyin:
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas matplotlib seaborn