# Fantasy Battle - Basit Savaş Oyunu (OOP Python)

## Proje Açıklaması
**Fantasy Battle**, Fantasy Battle, Python'da nesne yönelimli programlama (OOP) ilkeleri kullanılarak geliştirilmiş basit bir savaş oyunudur.  Oyunda bir **Savaşçı (Warrior)** olarak **Okçu (Archer)** ve **Büyücü (Mage)** gibi düşmanlarla mücadele edersiniz. Oyunda farklı karakter sınıfları bulunur ve her karakter kendine özgü saldırı ve özel yeteneklere sahiptir.

## Kullanılan OOP Kavramları
Bu projede aşağıdaki nesne yönelimli programlama (OOP) kavramları uygulanmıştır:

### 1. **Class (Sınıf)**
Her karakter türü (Warrior, Archer, Mage) bir sınıf olarak tanımlanmıştır. Ana sınıf `Character`, diğer karakterlerin temel özelliklerini ve metodlarını içeren bir soyut sınıftır.

### 2. **Inheritance (Kalıtım)**
`Character` sınıfı, `Warrior`, `Archer` ve `Mage` sınıfları tarafından miras alınmıştır. Bu sayede ortak özellikler tekrar yazılmadan her karaktere aktarılmıştır.

### 3. **Polymorphism (Çok Biçimlilik)**
Her karakterin `attack` ve `special_ability` metodları farklı şekilde uygulanmıştır. `Character` sınıfında soyut metot olarak tanımlanmış ve her alt sınıfta kendine özgü olarak yeniden yazılmıştır.

### 4. **Encapsulation (Kapsülleme)**
Karakterlerin adı, sağlığı, gücü gibi özellikleri `_name`, `_health`, `_strength` gibi değişkenlerle saklanmış ve dışarıdan doğrudan erişim yerine `@property` kullanılarak kontrollü erişim sağlanmıştır.

### 5. **Method Overriding (Metot Geçersiz Kılma)**
`Character` sınıfında tanımlanan `attack` ve `special_ability` metodları, alt sınıflarda farklı şekilde uygulanarak değiştirilmiştir.

### 6. **Abstraction (Soyutlama)**
`Character` sınıfı, `ABC` (Abstract Base Class) modülü ile soyut sınıf olarak tanımlanmıştır. Bu sayede doğrudan nesne oluşturulamaz ve tüm alt sınıfların `attack` ve `special_ability` metodlarını uygulaması zorunlu hale getirilmiştir.

### 7. **`__init__` Metodu**
Her karakter sınıfında, nesne oluşturulurken kullanılacak başlangıç değerleri `__init__` metodu içinde tanımlanmıştır. Böylece her sınıf kendi özel başlangıç değerlerine sahip olmuştur.

## Oyunun Kuralları ve Mekanikleri
- Oyuncu **Savaşçı (Warrior)** karakterini kontrol eder.
- Oyuncu her turda **saldırı** veya **özel yetenek** kullanabilir.
- Düşmanlar rastgele saldırır veya özel yetenek kullanır.
- Oyun, oyuncunun veya tüm düşmanların ölmesiyle sona erer.

## Karakterler ve Özellikleri
| Karakter | Can (HP) | Güç (Strength) | Özel Yetenek |
|----------|---------|---------------|--------------|
| **Savaşçı (Warrior)** | 150 | 15 | Öfke Patlaması: Güçlü saldırı yapar |
| **Okçu (Archer)** | 100 | 12 | 5 yeni ok kazanır |
| **Büyücü (Mage)** | 80 | 10 | Meditasyon ile kendini iyileştirir |

## Kurulum ve Çalıştırma
Projeyi çalıştırmak için aşağıdaki adımları takip edin:

### 1. Python Kurulumu
Eğer sisteminizde Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/) Python 3.x sürümünü indirip kurun.

### 2. Projeyi Çalıştırma
Terminal veya komut satırında aşağıdaki komutları kullanarak oyunu başlatabilirsiniz:
```bash
python fantasy_battle.py
```

## Nasıl Oynanır?
1. Oyun başladığında karakterler ve can durumları ekrana yazdırılır.
2. Oyuncu sırası geldiğinde **saldırı (1)** veya **özel yetenek (2)** seçimi yapar.
3. Saldırılar ve özel yetenekler karakterin durumuna göre değişir.
4. Düşmanlar rastgele saldırır veya özel yetenek kullanır.
5. Oyuncunun veya düşmanların tümü ölürse oyun sona erer.

## Örnek Oyun Çıktısı
```
=== FANTASY BATTLE ===
Karakterler:
Kahraman Savaşçı [Hayatta] - HP: 150/150, Güç: 15
Goblin Okçu [Hayatta] - HP: 100/100, Güç: 12
Kötü Büyücü [Hayatta] - HP: 80/80, Güç: 10

=== TUR 1 ===
Sıra sizde!
1. Saldır
2. Özel yetenek kullan
Seçiminiz (1-2): 1
Kahraman Savaşçı kılıcıyla Goblin Okçu'ya saldırıyor!
Goblin Okçu 18 hasar aldı! Kalan can: 82
Goblin Okçu yayıyla Kahraman Savaşçı'ya saldırıyor!
Kahraman Savaşçı 14 hasar aldı! Kalan can: 136
...
...
...
=== OYUN SONU ===
Tebrikler, kazandınız!
```

## Katkıda Bulunma
Projeye katkıda bulunmak için:
1. Bu repoyu fork'layın.
2. Yeni bir özellik ekleyin veya hataları düzeltin.
3. Pull Request gönderin!

## Lisans
Bu proje, açık kaynak olarak geliştirilmiştir ve dilediğiniz gibi kullanılabilir.






