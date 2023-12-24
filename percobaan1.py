from PIL import Image, ImageDraw, ImageFont 
 
# TODO 1: Lakukan load image pada variabel berikut 
# hint: kalian bisa gunakan fungsi open() 
gambarku = Image.open(r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\ml.jpg")  # Ganti path sesuai lokasi gambar 
 
# TODO 2: Ubah gambar menjadi hitam-putih 
# hint: kalian bisa gunakan fungsi convert() 
gambarBW = gambarku.convert("L") 
 
# TODO 3: Tambahkan text sesuai kriteria. 
draw = ImageDraw.Draw(gambarBW) 
direktoriFont = r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\font\arial.ttf"  # Ganti path sesuai lokasi font 
font_size = 24 
font = ImageFont.truetype(direktoriFont, font_size) 
text = "Nama: Syahbian Diaz Hamzah\nNIM: 202110370311381" 
text_x = 100 
text_y = 100
draw.text((text_x, text_y), text, font=font, fill=300) 
 
# TODO 4: Simpan gambar hasil edit menggunakan fungsi save() 
  # Ganti path sesuai lokasi penyimpanan 
gambarBW.save("percobaan1.jpg") 
 
# TODO 5: Tampilkan hasil akhir gambar 
gambarBW.show()