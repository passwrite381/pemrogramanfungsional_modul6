from PIL import Image

# TODO 0 : Import beberapa library lain yang dibutuhkan
# (Tidak ada library tambahan yang diperlukan untuk contoh ini)

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open(r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\ml.jpg")
overlay_image = Image.open(r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\smurf.png")

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA")

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# (Contoh: Perkecil gambar overlay menjadi setengah dari ukuran aslinya)
overlay_image = overlay_image.resize((overlay_image.width // 4, overlay_image.height // 4))  # Mengurangi ukuran overlay menjadi seperempat dari aslinya

# Tentukan koordinat untuk menempatkan overlay di pojok kanan atas
x_corner = background_image.width - overlay_image.width
y_corner = 0

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_corner, y_corner), overlay_image)

# TODO 5 : Simpan gambar hasil edit
background_image.save("Percobaan2.jpg")

# TODO 6 : Tampilkan
background_image.show()