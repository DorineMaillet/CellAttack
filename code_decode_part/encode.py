from PIL import Image
import stepic as stp
import glob as go

indent = 1

for filename in go.glob('dataset/candida/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Candida')
    im_encode.save('dataset_encoded/candida/Candida_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/chlamydia/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Chlamydia')
    im_encode.save('dataset_encoded/chlamydia/Chlamydia_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/gonorrhea/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Gonorrhea')
    im_encode.save('dataset_encoded/gonorrhea/Gonorrhea_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/hepatitis/b/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'HepatitisB')
    im_encode.save('dataset_encoded/hepatitis/b/HepatitisB_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/hepatitis/c/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'HepatitisC')
    im_encode.save('dataset_encoded/hepatitis/c/HepatitisC_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/hiv/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Hiv')
    im_encode.save('dataset_encoded/hiv/Hiv_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/papillomavirus/*.bmp'):
    print(filename)
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Papillomavirus')
    im_encode.save('dataset_encoded/Papillomavirus/Papillomavirus_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1

indent = 1

for filename in go.glob('dataset/syphilis/*.bmp'):
    im = Image.open(filename)
    im_encode = stp.encode(im, b'Syphilis')
    im_encode.save('dataset_encoded/syphilis/Syphilis_encoded' + str(indent) + '.bmp', 'BMP')
    indent += 1