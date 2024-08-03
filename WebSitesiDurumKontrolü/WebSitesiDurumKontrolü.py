# -*- coding: iso-8859-9 -*-
import requests

def check_website_status(url):
    try:
        # Kullan�c�n�n girdi�i URL'ye GET iste�i g�nder
        response = requests.get(url, timeout=10)
        # Yan�t kodunu kontrol et
        if response.status_code == 200:
            print(f"{url} �al���yor.")
        else:
            print(f"{url} siteye ula��lam�yor. Yan�t kodu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # �stek s�ras�nda olu�abilecek hatalar� yakala ve kullan�c�ya bildir
        print(f"{url} siteye ula��lam�yor. Hata: {e}")

def main():
    while True:
        # Kullan�c�dan kontrol edilecek web sitesinin URL'sini al
        url = input("Durumunu kontrol etmek istedi�iniz web sitesinin URL'sini girin (��kmak i�in 'q' yaz�n): ").strip()
        if url.lower() == 'q':
            print("Programdan ��k�l�yor.")
            break
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        check_website_status(url)

if __name__ == "__main__":
    main()
