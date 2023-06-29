from PIL import Image
import stepic as stp

im_decode = Image.open('Candida1_encoded.bmp')
steg_Image = stp.decode(im_decode)
print(steg_Image)