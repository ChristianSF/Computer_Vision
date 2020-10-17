from PIL import Image
from utills import in_path, out_file

def escalaCinza(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x, y))
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))

    return img

if __name__ == "__main__":
    leao = Image.open(in_path("Leao.jpg"))
    pb_leao = escalaCinza(leao)
    pb_leao.save(out_file("pb-leao.jpg"))
