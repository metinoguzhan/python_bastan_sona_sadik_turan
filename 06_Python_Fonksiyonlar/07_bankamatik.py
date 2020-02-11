# Bankamatik Uygulaması
sadikHesap = {
    'ad' : 'Sadık Turan',
    'hesapNo' : '13245678',
    'bakiye' : 3000,
    'ekHesap' : 2000
}


metinHesap = {
    'ad' : 'Metin Oğuzhan',
    'hesapNo' : '12345678',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye']>= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam>=miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı ? (e/h)')
            if ekHesapKullanimi == 'e':
                ekHesapKullacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz is {hesap['ekHesap']} TL bulunmaktadır.")


paraCek(sadikHesap,3000)

print('**********************')


paraCek(sadikHesap,1900)
