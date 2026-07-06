from PIL import Image
import os

# Datei laden
spritesheet = Image.open("explosion_spritesheet.png").convert("RGBA")

# Größe des gesamten Bildes
sheet_width, sheet_height = spritesheet.size

# Anzahl Frames
cols = 6
rows = 6

# Framegröße
frame_width = sheet_width // cols
frame_height = sheet_height // rows

# Ausgabeordner
output_folder = "explosion_frames"
os.makedirs(output_folder, exist_ok=True)

frame_number = 0

for row in range(rows):
    for col in range(cols):
        x = col * frame_width
        y = row * frame_height

        frame = spritesheet.crop((
            x,
            y,
            x + frame_width,
            y + frame_height
        ))

        frame.save(f"{output_folder}/explosion_{frame_number}.png")
        frame_number += 1

print("Fertig! Frames wurden gespeichert.")