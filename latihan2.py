print ("Program untuk menampilkan ilangan terbesar dari ilangan yang diinputkan")
print ("mohon masukan angka 0 untuk berhenti")


a = 1
max = 0
while a !=0:
    if a > max:
        max = a
        a = int(input("masukan bilangan:"))
        if a == 0:
            break
        print("bilangan terbesar adalah:",max)
        
