from geometry.Persegi import Persegi
from geometry.PersegiPanjang import PersegiPanjang

print('sample menggunakan oop')

p1 = Persegi(30, 2)
print(p1.info())

print('-------')

print(p1.hitung_luas())

print('------')
p2 = PersegiPanjang(20, 5)
print(p2.hitung_luas())
