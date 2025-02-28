# News API CRUD Operations

Bu proje Genç Başarı Eğitim Vakfı'nın İş Yaşamında Eşit Fırsatlar Programı kapsamında verilen Yapay Zeka (Python) eğitimlerinin 2. haftasının ödevidir.  

Bu proje, News API kullanarak haber makalelerini yönetmek için basit bir CRUD (Create, Read, Update, Delete) uygulamasıdır.

## Özellikler

- News API'den güncel iş haberlerini çekme
- Yeni haber makalesi oluşturma
- Var olan makaleleri yazara göre okuma
- Tüm makaleleri listeleme
- Yazara göre makale güncelleme
- Yazara göre makale silme
- Hata yönetimi

## Gereksinimler

```bash
pip install requests
```

## Kullanım

Programı çalıştırmak için:

```bash
python odev2.py
```

### Mevcut Komutlar

1. `create`: Yeni bir haber makalesi oluştur
2. `list`: Tüm makaleleri görüntüle
3. `read`: Belirli bir yazarın makalesini oku
4. `update`: Bir yazarın makalesini güncelle
5. `delete`: Bir yazarın makalesini sil
6. `0`: Programdan çık

### Örnek Kullanım

```bash
Type a process name: create
Please enter source_name: TechNews
Please enter Author name: John Doe
Please enter the title: AI Developments
Please enter the Description: New AI breakthrough
Please enter the date: 2024-03-15
Please enter content: Exciting developments in AI...
```

## Proje Yapısı

- `fetch_news()`: News API'den verileri çeker
- `create_data()`: Yeni makale oluşturur
- `read_data()`: Yazara göre makale okur
- `read_all_data()`: Tüm makaleleri listeler
- `update_data()`: Makale günceller
- `delete_data()`: Makale siler

## Hata Yönetimi

Program, aşağıdaki durumlarda hata yönetimi sağlar:
- API çağrısı başarısız olduğunda
- Veri oluşturma/okuma/güncelleme/silme işlemlerinde
- Kullanıcı girişi hatalarında

## API Anahtarı

Program varsayılan olarak bir API anahtarı ile gelir. Kendi API anahtarınızı kullanmak için:
1. [News API](https://newsapi.org/) üzerinden ücretsiz bir hesap oluşturun
2. API anahtarınızı alın
3. `fetch_news()` fonksiyonundaki `api_key` parametresini güncelleyin

## Notlar

- Program, veriler bellekte tutulur (kalıcı depolama yoktur)
- Çıkış yapmak için '0' komutunu kullanın
- Her işlemden sonra sonuçları görmek için 'list' komutunu kullanabilirsiniz 