import re

# result = dir(re)
# print(result)



# regular expression
# re module

cumle = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#re.findall()
# result = re.findall('Python',cumle)
# print(result)
# print(len(result))

# result = re.split(' ',cumle)
# print(result)

# result = re.sub(' ','-',cumle)
# print(result)

# result = re.sub('\s','-',cumle)
# print(result)


# result = re.search("Python",cumle)
# print(result)


# result = result.span()
# print(result)


# result = result.start()
# print(result)

# result = result.end()
# print(result)

# result = result.group()
# print(result)

# result = result.string
# print(result)


"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.
         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""
# result = re.findall('[abc]',cumle)
# print(result)

# result = re.findall('[sat]',cumle)
# print(result)

# result = re.findall('[a-e]',cumle)
# print(result)

# result = re.findall('[a-z]',cumle)
# print(result)

# result = re.findall('[0-5]',cumle)
# print(result)


# result = re.findall('[^abc]',cumle)
# print(result)


# result = re.findall('[^0-9]',cumle)
# print(result)

"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches
    
"""

# result = re.findall('...',cumle)
# print(result)

# result = re.findall('Py..on',cumle)
# print(result)


"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""

# result = re.findall('^P',cumle)
# print(result)


"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""

# result = re.findall('t$',cumle)
# print(result)

# result = re.findall('saat$',cumle)
# print(result)

# result = re.findall('saatt$',cumle)
# print(result)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""


# result = re.findall('sa*t',cumle)
# print(result)


"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

# result = re.findall('sa+t',cumle)
# print(result)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma?n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

# result = re.findall('sa?t',cumle)
# print(result)

"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

# result = re.findall("a{2}",cumle)
# print(result)

# result = re.findall("[0-9]{2}",cumle)
# print(result)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""



"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?
    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""


result = re.findall('\APython',cumle)
print(result)


result = re.findall('saat\Z',cumle)
print(result)