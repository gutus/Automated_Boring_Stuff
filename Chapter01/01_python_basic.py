# Practice Question QUIZ
# 1) Manakah yg operator dan value?
#   * operator
#    "hello" value
#   -88.8 value
#   - operator
#   / operator
#   + operator
#   5 value

# 2) Manakah diantara berikut yg variabel an string
# spam >>> variabel
# "spam" >>> string


# 3) Sebutkan 3 type data
# 1 int, float      2 string        3 boolean

# 4) Expresi terdiri dari apa, dan apa fungsi expressi?
# Terdiri dari value (nilai) dan operator (* / + -) salah satu fungsinya misal untuk melakukan operasi aritmatik, operasi logic, dsj.

# 5) Assign statement spam = 10.  Apa perbedaan antara expression dan statement
# Assign statment terdiri dari nama variabel diikuti = dan value dari variabel yg di-assign
# Expression terdiri dari kombinasi beberapa variabel, operasi diikuti dengan = untuk menghasilkan value atau variabel lain.

# 6) Berapakah nilai variabel berikut
# cireng = 5
# cireng + 1
# Jawaban cireng = 6
# Pembuktian
cireng = 5
print(f"Nilai cireng sebelum ditambah 1 >> {cireng}")
cireng + 1
print(f"Maka nilai cireng saat ini adalah >> {cireng}")

# 7) Bagaimanakah output dari expression berikut:
#   "spam" + "spamspam"
#   "spam" * 3
# Jawaban sama >> spamspamspam
# Pembuktian
satu = "spam" + "spamspam"
print(f"Output pertanyaan 7a >> {satu}")
dua = "spam" * 3
print(f"Output pertanyaan 7b >> {dua}")
# Ini namanya ternery operator, canggih gak? :D Thankyou Mosh Hamedany
print("Tuhkan sama" if satu == dua else "Yeee! beda kali!")

# 8)  Kenapa nama variabel telur valid sedangkan 100 tidak valid?
# dalam konvensi python tidak memperbolehkan penamaan variabel dengan karakter awal angka, akan ada error literral

# 9)  Bagaimana cara mendapatkan versi nilai integer, floating dan string dari sebuah value?
# Gunakan fungsi type data sesuai dengan type yg diinginkan >> int(), float() dan string()

# 10)  Perbaiki expression berikut.
# 'I have eaten ' + 99 + ' burritos.'
# Jawaban 'I have eaten ' + str(99) + ' burritos.'
# Pada jwaban di atas, 99 dirubah ke fungsi type data string, supaya bisa digabung (concatenate) string yg mengapit.
