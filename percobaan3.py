from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
gambar = Image.open(r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\ml.jpg")  # Ganti dengan path gambar yang ingin Anda edit

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer_brightness = ImageEnhance.Brightness(gambar)
brightened_image = enhancer_brightness.enhance(5)

enhancer_contrast = ImageEnhance.Contrast(brightened_image)
final_image = enhancer_contrast.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("Percobaan3.jpg")

# TODO 4: Tampilkan
final_image.show()