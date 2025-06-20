#variable disimpan sebagai string
number = "1,2,3,4,5,6,7,8,9,0"

#menampilkan data trakhir
print("data trakhir:", number[-1])

#menampilkan data pertama
print("data pertama:", number[0])

#menampilkan data ke-3 sampai ke-6 (indeks 2 sampai 5)
print("data ke-3 sampai ke-6:", number[3:7])

nama_domain = input("masukkan nama dommain anda")
index = nama_domain.index(".")
nama = nama_domain[:index]
domain = nama_domain[index:]

print(f"nama anda adalah = {nama}")
print(f"domain anda adalah = {domain}")