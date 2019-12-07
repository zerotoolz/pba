import argparse
from PIL import Image
def decode(filename1, filename2): 
    first = Image.open("PATH to share1.png Listing 4 result, line 36")
    f_pixels = first.load()
    first.convert("1")  
    second = Image.open("PATH to share2.png Listing 4 result, line 37")
    second.convert("1")
    s_pixels = second.load()   
    third = Image.new("1", (first.size[0], int(first.size[1]/2)))
    t_pixels = third.load()
    for i in range(third.size[0]):
        for j in range(third.size[1]):
            if f_pixels[i, j * 2] + s_pixels[i, j * 2] == 0 or f_pixels[i, j * 2 + 1] + s_pixels[i, j * 2 + 1] == 0:
            	t_pixels[i,j] = 1
            else:
                t_pixels[i,j] = 0         
    third.save("PATH to save reconstructed IBV after VC result *.png")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--IMAGE1", help="The image to discrypt - 1")
    parser.add_argument("--IMAGE2", help="The image to discrypt - 2")
    args = parser.parse_args()
    decode(args.IMAGE1, args.IMAGE2)
