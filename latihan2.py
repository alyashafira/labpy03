print("program untuk menampilkan bilangan terbesar dari n bilangan yang diinputkan")

max = 0
while True:
    a=int(input("Masukan Bilangan :"))
    if max < int (a):
        max = int(a)
    if a == 0:
        break
print("Bilangan Terbesar adalah = :",max)
