# kalkulator sederhana

print("="*20, "\n")

angkaSatu = (int(input(f"masukkan angka = ")))
operator = (input("masukkan operator = "))
angkaDua = (int(input(f"masukkan angka = ")))



if operator == "+":
    operatorTambah = angkaSatu + angkaDua
    print(f"hasil = {operatorTambah}")

elif operator == "-":
    operatorKurang = angkaSatu - angkaDua
    print(f"hasil = {operatorKurang}")

elif operator == "x":
    operatorKali = angkaSatu * angkaDua
    print(f"hasil = {operatorKali}")

elif operator == "/":
    operatorBagi = angkaSatu / angkaDua
    print(f"hasil = {operatorBagi}")

print("\n", "="*5, "akhir dari program", "="*5)




