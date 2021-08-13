from random import choice


def password_generator():
    a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    b = 'qwertyuiopasdfghjklzxcvbnm'
    c = '1234567890'

    p = ''
    for i in range(3):
        p += choice(a)
        p += choice(b)
        p += choice(c)

    return p
