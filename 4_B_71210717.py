x= int(input("Masukan angka: "))
if (x % 2 ==0) and (x % 3 !=0):
    a = "YA"
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3?, Jawab:", a)
    #ganti code if dengan ini agar bisa mendapatkan hasil test case 2 juga
    #if (x % 10 == 0):
    #    b = "IYA DONG" 
    if (x % 5 !=0)or(x % 10 == 0):
        b = "IYA DONG"
    elif (x % 10 != 0):
        b = "TIDAK"

    print()
    print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab", b)

else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")


