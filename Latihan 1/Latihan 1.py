txt = 'Hello World'

#Hitung jumlah karakter
Jumlah_karakter = len(txt)
print (f"Jumlah {Jumlah_karakter} karakter")

#Ambil karakter terakhir
karakter_terakhir = txt[-1]
print (f"karakter_terakhir : {karakter_terakhir}")

#Ambil karakter indeks ke-2 sampai index ke-4 (iio)
substring = txt[2:5]
print(f"karakter_indeks 2-4: {substring}")

#Hilangkan spasi pada text tersebut (Helloo Word)
tanpa_spasi = txt.replace(" ", "")
print (f"Tanpa_spasi : {tanpa_spasi}")

#Ubah text menjadi huruf besar
huruf_besar = txt.upper()
print (f"Huruf_besar : {huruf_besar}")

#Ubah text menjadi kecil
huruf_kecil = txt.lower()
print (f"Huruf_kecil : {huruf_kecil}")