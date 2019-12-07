import argparse
import random
from PIL import Image
def encrypt(filename):
    original = Image.open("PATH to original user image after Listing 1 *.png")
    original = original.convert("1")
    o_pixels = original.load()
    first = Image.new("1", (original.size[0], original.size[1] * 2))
    f_pixels = first.load()
    second = Image.new("1", (original.size[0], original.size[1] * 2))
    s_pixels = second.load()
    for i in range(original.size[0]):
        for j in range(original.size[1]):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0    
    first.save("PATH to save  1/1 IBV share1.png")
    second.save("PATH to save 1/2 IBV share2.png")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--IMAGE", help="The image to encrypt")
    args = parser.parse_args()
    encrypt(args.IMAGE)