class Persegi(BangunRuang):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def info(self):
        return 'hello info menggunakan class'


    def hitung_luas(self):
        return self.a * self.b
