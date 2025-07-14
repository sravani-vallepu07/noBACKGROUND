from rembg import remove
from PIL import Image
input_path="anna.jpg"
output_path="anna_no_bg.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print(f"Background removed and saved to {output_path}")