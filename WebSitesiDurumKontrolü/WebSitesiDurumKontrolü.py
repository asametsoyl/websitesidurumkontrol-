# -*- coding: iso-8859-9 -*-
import requests

def check_website_status(url):
    try:
        # Kullanıcının girdiği URL'ye GET isteği gönder
        response = requests.get(url, timeout=10)
        # Yanıt kodunu kontrol et
        if response.status_code == 200:
            print(f"{url} çalışıyor.")
        else:
            print(f"{url} siteye ulaşılamıyor. Yanıt kodu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # İstek sırasında oluşabilecek hataları yakala ve kullanıcıya bildir
        print(f"{url} siteye ulaşılamıyor. Hata: {e}")

def main():
    while True:
        # Kullanıcıdan kontrol edilecek web sitesinin URL'sini al
        url = input("Durumunu kontrol etmek istediğiniz web sitesinin URL'sini girin (Çıkmak için 'q' yazın): ").strip()
        if url.lower() == 'q':
            print("Programdan çıkılıyor.")
            break
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        check_website_status(url)

if __name__ == "__main__":
    main()
