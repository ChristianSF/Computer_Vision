from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def triangulo(size):
    white = (255, 255, 255)
    black = (0, 0, 0)
    image = Image.new("RGB", (size, size), white)

    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x, y), black)
    return image

def bandeira_franca(altura):

    largura = 3*altura//2

    azul = (0, 85, 164)
    branco = (255,255,255)
    vermelho = (239, 65, 53)

    image = Image.new("RGB", (largura, altura), branco)

    offset = largura//3
    for x in range(offset):
        for y in range(altura):
            image.putpixel((x, y), azul)
            image.putpixel((x + 2*offset, y), vermelho)
    return image

def bandeira_japao(altura):
    largura = 3*altura//2

    vermelho = (173, 35, 51)
    branco = (255,255,255)

    r = 3*altura//10
    c = (largura//2, altura//2)

    image = Image.new("RGB", (largura, altura), branco)

    for x in range(c[0]-r, c[0]+r):
        for y in range(c[1]-r, c[1]+r):
           if (x-c[0])**2 + (y-c[1])**2 <= r**2:
               image.putpixel((x, y), vermelho)

    return image

if __name__ == "__main__":
    #t = triangulo(700)
    #bandeira = bandeira_franca(700)
    bandeira = bandeira_japao(500)
    bandeira.show()
