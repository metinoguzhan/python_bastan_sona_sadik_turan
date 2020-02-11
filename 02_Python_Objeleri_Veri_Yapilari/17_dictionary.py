sehirler = ['kocaeli','istanbul']
plakalar = [41, 34]

print(plakalar[sehirler.index('istanbul')])



plakalar = {
    'kocaeli' : 41,
    'istanbul' : 34
}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])


plakalar['ankara'] = 6
print(plakalar)


plakalar['kocaeli'] = 'new value'
print(plakalar)


users = {
    'sadikturan' : {
        'age' : 36,
        'roles' : ['user'],
        'email' : 'sadikturan@gmail.com',
        'address' : 'kocaeli',
        'phone' : '1231231'
    },
    'cinarturan' : {
        'age' : 2,
        'roles' : ['admin','user'],
        'email' : 'cinarturan@gmail.com',
        'address' : 'istanbul',
        'phone' : '99999'
    }
}

print(users)
print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])
print(users['cinarturan']['roles'])
print(users['cinarturan']['roles'][0])
print(users['cinarturan']['roles'][1])
