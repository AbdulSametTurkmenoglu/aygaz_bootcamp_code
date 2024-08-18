import random

def oyun_kurallari():
    print("MERHABA TAS - KAGIT - MAKAS OYUNUNA HOŞGELDİNİZ")
    print("--------------------------------------------------")
    print("Oyunun kuralları basit ve nettir:")
    print("1. Taş, makası yener ve kağıda yenilir.")
    print("2. Makas, kağıdı yener ve taşa yenilir.")
    print("3. Kağıt, taşı yener ve makasa yenilir.")
    print("Başarılar dilerim, iyi oyunlar!")

def karsilastirma(secim, secim1):
    kurallar = {
        "tas": "makas",  # Taş makası yener
        "kagıt": "tas",  # Kağıt taşı yener
        "makas": "kagıt"  # Makas kağıdı yener
    }

    if secim == secim1:
        return "Berabere!"
    elif kurallar[secim] == secim1:
        return "Tebrikler, kazandınız!"
    else:
        return "Bilgisayar kazandı, tekrar deneyin."

def oyun_baslat():
    # Geçerli seçimler listesi
    gecerli_secimler = ["tas", "kagıt", "makas"]

    # Oyun skorları
    sizin_sayiniz = 0
    bilgisayarin_sayisi = 0

    # Oynanan oyun ve tur sayıları
    toplam_tur = 3

    oyun_kurallari()

    # Bilgisayarın oyuna katılmak isteyip istemediğini sor
    bilgisayar_oyuna_katilmak = input("Bilgisayar oyuna katılmak istiyor mu? (evet/hayır): ").strip().lower()
    if bilgisayar_oyuna_katilmak not in ["evet", "hayır"]:
        print("Geçersiz giriş! Bilgisayar oyuna katılmak istiyor mu? (evet/hayır) şeklinde yanıt veriniz.")
        return

    for tur in range(toplam_tur):
        print(f"\nTur {tur + 1} Başlıyor!")

        # Her turun başında skorları sıfırla
        tur_sizin_sayiniz = 0
        tur_bilgisayarin_sayisi = 0

        while tur_sizin_sayiniz < 2 and tur_bilgisayarin_sayisi < 2:
            # Kullanıcıdan seçim al
            secim = input("Lütfen seçiminizi giriniz (tas, kagıt, makas): ").lower()

            # Kullanıcıdan doğru seçim yapmasını sağla
            while secim not in gecerli_secimler:
                secim = input("Geçersiz seçim! Lütfen 'tas', 'kagıt' veya 'makas' seçiniz: ").lower()

            print("Seçiminiz:", secim)

            if bilgisayar_oyuna_katilmak == "evet":
                # Bilgisayarın rastgele seçimi
                secim1 = random.choice(gecerli_secimler)
                print("Bilgisayarın seçimi:", secim1)

                # Sonucu belirle ve yazdır
                sonuc = karsilastirma(secim, secim1)

                # Tur skorlarını güncelle
                if sonuc == "Tebrikler, kazandınız!":
                    tur_sizin_sayiniz += 1
                elif sonuc == "Bilgisayar kazandı, tekrar deneyin.":
                    tur_bilgisayarin_sayisi += 1

            else:
                # Bilgisayar oyuna katılmıyorsa, kullanıcı her oyunu kazanır
                print("Bilgisayar oyuna katılmıyor. Siz kazandınız!")
                tur_sizin_sayiniz += 1

            print(f"Bu turda Skor: Siz: {tur_sizin_sayiniz} - Bilgisayar: {tur_bilgisayarin_sayisi}")

        if tur_sizin_sayiniz == 2:
            print("Tebrikler! Siz iki oyunu kazandınız ve bu turu kazandınız!")
            sizin_sayiniz += 1
        elif tur_bilgisayarin_sayisi == 2:
            print("Bilgisayar iki oyunu kazandı ve bu turu kazandı!")
            bilgisayarin_sayisi += 1

    print("\nOyun Sonuçları:")
    print(f"Toplam Oynanan Turlar: {toplam_tur}")
    print(f"Toplam Skor: Siz: {sizin_sayiniz} - Bilgisayar: {bilgisayarin_sayisi}")

    if sizin_sayiniz > bilgisayarin_sayisi:
        print("Tebrikler! Oyunu kazandınız!")
    elif sizin_sayiniz < bilgisayarin_sayisi:
        print("Bilgisayar oyunu kazandı!")
    else:
        print("Oyun berabere!")

if __name__ == "__main__":
    oyun_baslat()

