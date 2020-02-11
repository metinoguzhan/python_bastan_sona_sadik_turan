#error => hata

# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError




#error handling => hata yönetimi

# try:
#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x/y)
# # except ZeroDivisionError:
# #     print('y için sıfır girilemez..')
# # except ValueError:
# #     print('x ve y için sayısal değer girmelisiniz')
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz..')
#     print(e)


# try:
#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz..')


# try:
#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz..')
# else:
#     print('herşey yolunda')

while True:
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz..',ex)
   
    else:
        break
    finally:
        print('try except sonlandı')
    