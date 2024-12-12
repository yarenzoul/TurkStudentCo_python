# TurkStudentCo PYTHON
# Film Yönetimi Projesi

Bu projede, film verilerini yönetmek ve düzenlemek için bir Python uygulaması geliştirdim. Uygulama, kullanıcılara film ekleme, listeleme ve silme gibi işlemleri yapabilme imkanı tanır. 

## Kullanılan Sınıflar ve İşlevler

### `Film` Sınıfı
Bu sınıf, film verilerini temsil eder. Her film için aşağıdaki bilgileri saklar:
- `filmAdi`: Filmin adı.
- `yonetmen`: Filmin yönetmeni.
- `yil`: Filmin vizyon yılı.
- `fTur`: Filmin türü.

#### `__init__(self, filmAdi, yonetmen, yil, fTur)`
Yapıcı metod, film bilgilerini alır ve film nesnesini oluşturur.

---

### `FilmYoneticisi` Sınıfı
Bu sınıf, film koleksiyonunu yönetir. Film ekleyebilir, listeleyebilir ve silebilir.

#### `filmEkle(self, filmAdi, yonetmen, yil, fTur)`
Bu metod, yeni bir film ekler ve başarı mesajı yazdırır.

#### `filmListele(self)`
Bu metod, eklenen tüm filmleri vizyon yılına göre sıralayarak liste halinde gösterir.

#### `filmSil(self, filmAdi, yonetmen, yil, fTur)`
Bu metod, belirtilen film bilgilerini arar ve bulursa siler, aksi takdirde film bulunamadığına dair mesaj verir.

![Ekran görüntüsü 2024-12-12 190422](https://github.com/user-attachments/assets/bc00bfc5-dc00-4c69-9e52-34c998e623e4)

Silme işlemimizden sonra listemizin son hali

![Ekran görüntüsü 2024-12-12 190557](https://github.com/user-attachments/assets/c9db8a11-bbc3-42a9-8ec9-84693f18c110)

# Hava Durumu Takip Sistemi

Bu Python programı, kullanıcıların şehirlerin hava durumunu takip etmelerini sağlar. Program, şehirlerin adı ve o şehirdeki sıcaklık bilgilerini kaydederek, şehirlerin hava durumu hakkında önerilerde bulunur.

## Kullanılan Sınıflar ve İşlevler

### Sehir Sınıfı
Bu sınıf, bir şehri ve o şehirdeki sıcaklık bilgisini tutar.
sehirAdi: Şehir adı (String)
sicaklik: Şehirdeki sıcaklık (Integer)

### `HavaDurumu` Sınıfı
`HavaDurumu` sınıfı, belirli bir şehir için hava durumu verilerini almak ve görüntülemek için kullanılır.

#### Metodlar:
`sehirEkle(sehirAdi, sicaklik):` Yeni bir şehir ve sıcaklık ekler.

`sicaklikGuncelle(sehirAdi, yeniSicaklik):` Belirtilen şehirdeki sıcaklık bilgisini günceller.

`tavsiye(sehirAdi):` Belirtilen şehir için hava durumuna uygun giyim tavsiyesi verir.

`sehirleri_listele():` Tüm şehirleri ve sıcaklıklarını listeler.

![Ekran görüntüsü 2024-12-12 192336](https://github.com/user-attachments/assets/73cfb6d4-2f07-459e-934b-0296a2e77a14)




---
