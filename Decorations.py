import time

#decoration ornek1

def main(funk):
    def main2():
        print("1")
        funk()
        print("3")
    return main2


@main
def alt():
    print("2")

alt()

#decoration ornek2

def sure_olc(fonksiyon):
    def sure_olc2(*args):

        baslangic = time.time()
        print(f"Baslangic   {baslangic}")

        fonksiyon(*args)

        son = time.time()
        print(f"Son   {son}")

        print(son-baslangic)

    return sure_olc2

@sure_olc
def fac_calculate(value):  
    toplam = 1  

    while value > 1:

        toplam = toplam * value
        value = value - 1

    print(toplam)

fac_calculate(1000)
