import random

def gen_pass():
    source = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password_length = 10
    password = ""

    for i in range(password_length):
        password += random.choice(source)

    return password

def flip_coins():
    coins = random.randint(1, 2)
    if coins == 1:
        return 'koin bagian normal'
    else:
        return 'koin bagian wajah pahlawan'

sampah_organik = ['daun', 'makanan sisa', 'kotoran',
                  'ranting kayu', 'cangkang telur', 'sisa sayuran',
                  'buah busuk', 'tulang']

sampah_anorganik = ['plastik/kresek', 'kertas', 'ban/karet', 'kaca',
                    'melamin', 'kaleng', 'botol plastik', 'baterai', 
                    'kardus']