#membuat pengecekan password
#ketika yang di input kurang dari 8, = karakter kurang
#ketika yang di input sama/lebih dari 8, = karakter cukup

# Input password
password = input("masukkan password: ")
# pengecekan password 
if len(password) < 8:
    print("Karakteer kurang");
else:
    print("Karakter cukup");