# labpy03 :octocat:


# LATIHAN 1

** Code program **

             import random
       jumlah = int(input("Masukan Nilai N :"))

       for i in range(jumlah):
            i=random.uniform(0.0,0.5)
            print("Data ke =: =>",i)

       print("SELESAI")
   
Hasil dari screenshot program yang telah dijalankan
![lat1](https://user-images.githubusercontent.com/56963083/68419799-846ed180-01cd-11ea-87aa-700ae87bf30c.PNG)


# ALUR ALGORITMA LATIHAN 1

      A. Input
      Import Random
        >>>import fungsi lanjut yang dipanggil oleh statment import,
        sedangkan random untuk pilihan. yang berarti menentukan suatu pilihan yang berarti menggabungkan dua operasi.

      B. Proses
      Jumlah = int(input("Masukan Jumlah N:) ) 
        >>>Merupakan fungsi untuk menghasilkan integer. 
      For i in range(jumlah) :
        >>>Merupakan fungsi yang menghasilkan list. Fungsi yang menciptakan sebuah list baru
      i=random.uniform(0.0, 0.5) 
        >>>Digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.
      
      C. Output 
      print("Data ke =: =>",i)
        >>>Untuk Menampilkan Hasil dari sebuah proses yaitu dengan menampilkan i
      print("SELESAI")
        >>>Berfungsi untuk mencetak teks "Selesai" yang bertanda bahwa program sudah berakhir
    

# LATIHAN 2
** Code Program **

     print("program untuk menampilkan bilangan terbesar dari n bilangan yang diinputkan")

     max = 0
     while True:
          a=int(input("Masukan Bilangan :"))
          if max < int (a):
          max = int(a)
          if a == 0:
              break
     print("Bilangan Terbesar adalah = :",max)


Hasil dari screenshot program yang telah dijalankan
![lat2](https://user-images.githubusercontent.com/56963083/68419990-eaf3ef80-01cd-11ea-809c-d5133cce6f14.PNG)


# ALUR ALGORITMA LATIHAN 2
      A. Input
      print("program untuk menampilkan bilangan terbesar dari n bilangan yang diinputkan")
        >>> Berfungsi untuk mencetak teks "program untuk menampilkan bilangan terbesar n bilangan yang diinput kan") 
      max = 0
        >>> Berfungsi bulid-in untuk mencari nilai tertinggi.Fungsi ini dapat diberikan sebuah parameter berupa angka.
      B. Proses
      while True:
        a=int(input("Masukan bilangan :"))
        if max < int(a):
          max = int(a)
        if a == 0:
          break
           
           ## "while"	: disebut uncounted loop (perulangan yang tak terhitung),
           ## "int"	     =berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).
           ## "if"	     = Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan.
           ## "break"	: fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.
       
      C. Output
      print("Bilangan Terbesar Adalah: ",max)
          >>>Untuk menampilkan Hasil dengan mencetak bilangan terbesar yaitu max
      


# PROGRAM
** Code Program **
      
           a = 100000000
     for x in range (1,9):
           if(x>=1 and x<=2):
               b=a*0
               print("Laba Bulan Ke-",x," :",b)
           if(x>=3 and x<=4):
               c=a*0.1
               print("Laba Bulan Ke-",x," :",c)
           if(x>=5 and x<=7):
               d=a*0.5
               print("Laba Bulan Ke-",x," :",d)
           if(x==8):
               e=a*0.2
               print("Laba Bulan Ke-",x," :",e)
      total = b+b+c+c+d+d+d+e
      print("\nTotal : ", total) 


Hasil dari screenshot program yang telah ditelah dijalankan
![program](https://user-images.githubusercontent.com/56963083/68420200-6b1a5500-01ce-11ea-8cd4-a4a0c6c0dc94.PNG)


# ALUR ALGORITMA PROGRAM

      A. Input 
        a = 100000000
            ##"print"	= Fungsi "print()" berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (Layar).
            ##"a" = adalah variable dimana 100000000 adalah modal awalnya.,
      B. Proses
      for x in range(1,9):
      if(x>=1 and x<=2):
        b=a*0
        print("Laba Bulan Ke-",x," :",b)
      if(x>=3 and x<=4):
        c=a*0.1
        print("Laba Bulan Ke-",x," :",c)
      if(x>=5 and x<=7):
        d=a*0.5
        print("Laba Bulan Ke-",x," :",d)
      if(x==8):
        e=a*0.2
        print("Laba Bulan Ke-",x," :",e)
      
        ##"for x in range" = "for" perulangan yang terhitung, dan "range" mengembalikan deret integer berurut pada range yang                       ditentukan dari start sampai stop.
        ##"if"= Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu                  perintah dalam kondisi tertentu. 
        ##"for"	= Perulangan yang terhitung.
        ##"range" = Mengembalikan deret integer berurut pada range yang ditentukan dari start sampai stop.
      C.Output
      total = b+b+c+c+d+d+d+e
        print("\nTotal : ", total)
          ##"\nTotal" = Membuat garis baru, dan menampilkan total hasil dari apa yang kita diinginkan



 

