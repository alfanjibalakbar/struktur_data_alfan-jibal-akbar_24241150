print("program menghitung luas")
print("====== menu ====== \n 1. menghitung persegi \n 2. menghitung segitiga \n ==============")

userinput = int(input("pilih menu: "))
if userinput == 1:
    print ("menghitung persegi")
    inputpanjang = int(input("masukan panjag = "))
    inputlebar = int(input("masukan lebar = "))
    luas = inputpanjang * inputlebar
    print(f"hasildari {inputpanjang} x {inputlebar} = {luas}")
elif userinput == 2:
    print("menghitung segitiga")
    inputalas = int(input("masukan alas = "))
    inputtinggi = int(input("masukam tinggi = "  ))
    hasil = 0.5 * inputalas * inputtinggi 
    print( f"hasil dari {inputalas} x {inputtinggi} = {hasil}")
else:
    print("input tidak valid")
