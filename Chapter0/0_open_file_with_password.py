passwordFile = open("0_password_rahasia.txt")
isiTextRahasia = open("0_text_rahasia.txt", "r")
secretPassword = passwordFile.read()
print("Masukkan password anda. ")
passwordDiketik = input()
if passwordDiketik == secretPassword:
    print("Password anda benar")
    # Semua baris dibaca dan disimpan ke dalam memory dengan variable rahasia.
    rahasia = isiTextRahasia.readlines()
    print(rahasia)
    print("---EOL---")
else:
    print("Akses ditolak, silakan periksa password anda.")
