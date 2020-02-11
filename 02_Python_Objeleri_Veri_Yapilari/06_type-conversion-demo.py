'''

    Dairenin alanı : πr²
    Dairenin çevresi : 2πr

    * Yarı çapı verilen bir dairenin alan ve cevresini hesaplayınız. (π : 3.14) 

'''


r = input("Yarı çapı : ")
pi = 3.14

daireAlan = pi * float(r)**2
daireCevre = 2 * pi * float(r)

print("Dairenin Alanı : ", daireAlan)
print("Dairenin Cevre : ", daireCevre)
print("Alan : " + str(daireAlan) + " Çevre : " + str(daireCevre))

