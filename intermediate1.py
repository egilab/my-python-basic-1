from geometry.segitiga import hitung_luas_segitiga, info as infosegitiga

alas = 6
tinggi = 10
luas_segitiga = alas * tinggi / 2

print(f'luas segitigas adalah : {luas_segitiga}')

print('----------')


def hitung_luas(a, t):
    luas = a * t / 2
    return luas


print(hitung_luas(5, 8))

print('--------')
print(infosegitiga())
print(f'Luas segitiga menggunakan package {hitung_luas_segitiga(9, 10)}')
