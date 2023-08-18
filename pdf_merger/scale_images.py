import sys, re, glob, os
from PIL import Image


if len(sys.argv) < 3 :
    sys.exit("Usge: python scale_images [scale percentage] [foldername]")

n = int(sys.argv[1])
foldername = sys.argv[2]

#reading image files
files = glob.glob(f"{foldername}/*.jpg")
files = sorted(files, key=lambda x:int(re.findall(r"(\d+)",x)[0]))

op_folder = f"{foldername}_scaled_{n}"
op_path = os.path.join(os.getcwd(), op_folder)

os.mkdir(op_path)
for img_file in files:
    image = Image.open(img_file)
    h, w = image.size
    h, w = int(h*n/100), int(w*n/100)
    image.thumbnail((h, w))
    image.save(os.path.join(op_path, img_file))
    print(img_file)