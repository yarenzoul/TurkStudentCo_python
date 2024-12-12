
                                # HAVA DURUMU TAKİP SİSTEMİ
class Sehir:
    def __init__(Self, sehirAdi, sicaklik):
        Self.sehirAdi = sehirAdi  
        Self.sicaklik = sicaklik  
        
        
class HavaDurumu:
    def __init__(Self):
        Self.sehir = []  

    def sehirEkle(Self, sehirAdi, sicaklik):
        yeniSehir = Sehir(sehirAdi, sicaklik)
        Self.sehir.append(yeniSehir) 
        print(f"{sehirAdi} şehri {sicaklik}°C sıcaklığı ile eklenmiştir.")

    def sicaklikGuncelle(Self, sehirAdi, yeniSicaklik):
        for sehir in Self.sehir:  
            if sehir.sehirAdi.lower() == sehirAdi.lower():
                sehir.sicaklik = yeniSicaklik
                print(f"{sehirAdi} şehrinin sıcaklığı {yeniSicaklik}°C olarak güncellendi.")
                return
        print(f"{sehirAdi} şehri bulunamadı.")

    def tavsiye(Self, sehirAdi):
        for sehir in Self.sehir:  
            if sehir.sehirAdi.lower() == sehirAdi.lower():
                sicaklik = sehir.sicaklik
                if sicaklik < 0:
                    print(f"{sehirAdi}: Soğuk, sıkı giyinin.")
                elif 0 <= sicaklik < 15:
                    print(f"{sehirAdi}: Serin, mont almayı unutmayın.")
                else:
                    print(f"{sehirAdi}: Hava güzel, rahat giyin.")
                return
        print(f"{sehirAdi} şehri bulunamadı.")

    def sehirleri_listele(Self):
        print("\nKayıtlı Şehirler ve Sıcaklıkları:")
        for sehir in Self.sehir:  
            print(f"{sehir.sehirAdi}: {sehir.sicaklik}°C")


# ÖRNEK
hava_durumu = HavaDurumu()

hava_durumu.sehirEkle("Balıkesir", 10)
hava_durumu.sehirEkle("Denizli", 13)
hava_durumu.sehirEkle("İzmir", 16)
hava_durumu.sehirEkle("Bolu", 3)
hava_durumu.sicaklikGuncelle("Bolu", -3)


hava_durumu.sehirleri_listele()

hava_durumu.tavsiye("Balıkesir")
hava_durumu.tavsiye("Denizli")
hava_durumu.tavsiye("İzmir")
hava_durumu.tavsiye("Bolu")



                                # FİLM YÖNETİM SİSTEMİ
                                
class Film:
    def __init__(Self, filmAdi, yonetmen, yil, fTur):
        Self.filmAdi = filmAdi
        Self.yonetmen = yonetmen
        Self.yil = int(yil)  
        Self.fTur = fTur

class FilmYoneticisi:
    def __init__(Self):
        Self.film = []
        
    def filmEkle(Self, filmAdi, yonetmen, yil, fTur):
        yeniFilm = Film(filmAdi, yonetmen, yil, fTur)
        Self.film.append(yeniFilm)
        print(f"{filmAdi} - {yonetmen} - {yil} - {fTur} filmi eklenmiştir.")
        
    def filmListele(Self): 
        Self.film.sort(key=lambda x: x.yil)
        print("\nFilmler:")  
        for film in Self.film:
            print(f"{film.filmAdi} - {film.yonetmen} - {film.yil} - {film.fTur}")
            
    def filmSil(Self, filmAdi, yonetmen, yil, fTur):
        yil = int(yil)
        for film in Self.film:
            if (film.filmAdi.lower().strip() == filmAdi.lower().strip() and
                film.yonetmen.lower().strip() == yonetmen.lower().strip() and
                film.yil == yil and
                film.fTur.lower().strip() == fTur.lower().strip()):
                
                Self.film.remove(film)
                print(f"{filmAdi} filmi silindi.")
                return  
        
        
        print(f"{filmAdi} filmi bulunamadı.")
               
## ÖRNEK
film_takibi = FilmYoneticisi()

film_takibi.filmEkle("Indiana Jones and the Last Crusade", "Steven Spielberg", "1989", "Macera/Aksiyon") 
film_takibi.filmEkle("Indiana Jones and the Kingdom of the Crystal Skull", "Steven Spielberg", "2008", "Macera/Aksiyon")
film_takibi.filmEkle("Ruhlar Bölgesi: Son Anahtar", "Adam Robitel", "2018", "Korku")
film_takibi.filmEkle("Ejderhanı Nasıl Eğitirsin", "Chris Sanders, Dean DeBlois", "2010", "Animasyon") 
film_takibi.filmEkle("Red Notice", "Rawson Marshall Thurber", "2021", "Aksiyon/Komedi") 
film_takibi.filmEkle("Yüzüklerin Efendisi Kralın Dönüşü", "Peter Jackson", "2003", "Macera/Fantastik")
film_takibi.filmEkle("Fantastik Canavarlar: Dumbledore'un Sırları", "David Yates", "2022", "Macera/Fantastik")
film_takibi.filmEkle("Fantastik Canavarlar: Dumbledore'un Sırları", "David Yates", "2022", "Macera/Fantastik") 

film_takibi.filmListele() 

# Silme işlemi
film_takibi.filmSil("Fantastik Canavarlar: Dumbledore'un Sırları", "David Yates", "2022", "Macera/Fantastik")

film_takibi.filmListele()               

               

            
           
        
    
                               





















