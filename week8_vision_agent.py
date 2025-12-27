from skimage import data, io
import matplotlib.pyplot as plt
import os

os.makedirs("sample_images", exist_ok=True)
io.imsave("sample_images/cat.jpg", data.chelsea())
print("👁️ Week 8: Vision Agent\nSaved sample image: sample_images/cat.jpg")
plt.imshow(data.chelsea()); plt.axis('off'); plt.title("Sample Image"); plt.show()