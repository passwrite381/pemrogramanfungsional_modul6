from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

# TODO 0: Import library lain yang dibutuhkan

# TODO 1: Buka kedua gambar menggunakan Pillow
background_image_path = r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\bgumm.jpeg"  # Ganti path sesuai lokasi gambar background
overlay_image_path = r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\assets\logo_umm.png"  # Ganti path sesuai lokasi gambar overlay

background_image = Image.open(background_image_path)
overlay_image = Image.open(overlay_image_path)

overlay_image = overlay_image.convert("RGBA")

# TODO 2: Ubah gambar background
background_image = background_image.convert('L')  # Grayscale
background_image = background_image.rotate(30)  # Rotasi 30 derajat
background_image = background_image.filter(ImageFilter.BLUR)  # Blur

# TODO 3: Ubah tingkat kecerahan dan kontras gambar overlay
brightness_factor = 1.62  # Ganti dengan 2 digit NIM bagian belakang
contrast_factor = 1.62  # Ganti dengan 2 digit NIM bagian belakang

brightness_enhancer = ImageEnhance.Brightness(overlay_image)
brightened_overlay = brightness_enhancer.enhance(brightness_factor)

contrast_enhancer = ImageEnhance.Contrast(brightened_overlay)
final_overlay = contrast_enhancer.enhance(contrast_factor)

# Resize sesuai kebutuhan
result_image = Image.new("RGBA", background_image.size, (0, 0, 0, 0))

# TODO 4: Sisipkan gambar overlay ke dalam gambar background
position = (550, 100)
result_image.paste(background_image, (0, 0))
result_image.paste(final_overlay, position, final_overlay)

# TODO 5: Tambahkan teks pada gambar overlay
draw = ImageDraw.Draw(result_image)
font_path = r"c:\WINDOWS\Fonts\ARIALN.TTF"
font = ImageFont.truetype(font_path, size=24)
text = "Informatika JOSSS!"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_x = (result_image.width - text_bbox[2]) // 2
text_y = (result_image.height - text_bbox[3]) // 1.4
draw.text((text_x, text_y), text, font=font, fill="white")

# TODO 6: Simpan gambar hasil edit
save_path = r"C:\Users\diazh\OneDrive\Documents\Tugas S5\Pemrograman Fungsional\Praktikum\Modul 6\savegambarmodul6\hasil_edit_demo.png"
result_image.save(save_path)
result_image.show()