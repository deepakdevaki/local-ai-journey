from skimage import data, io
import os
os.makedirs("sample_images", exist_ok=True)
io.imsave("sample_images/cat.jpg", data.chelsea())
io.imsave("sample_images/coins.png", data.coins())
print("✅ Sample images saved in 'sample_images/'")