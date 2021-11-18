Num1= float(input("Masukan bilangan pertama: "))
Num2= float(input("Masukan bilangan kedua: "))
Sen= input("Masukan kalimat: ")

if "kali" in Sen:
    a= Num1 * Num2
    print("Hasil perkalian ", Num1, "dengan ", Num2, "adalah ", a)
elif "bagi" in Sen:
    a= Num1 / Num2
    print("Hasil pembagian ", Num1, "dengan ", Num2, "adalah ", a)
elif "tambah" in Sen:
    a= Num1 + Num2
    print("Hasil penjumlahan ", Num1, "dengan ", Num2, "adalah ", a)
elif "kurang" in Sen:
    a= Num1 - Num2
    print("Hasil pengurangan ", Num1, "dengan ", Num2, "adalah ", a)
else:
    print()
