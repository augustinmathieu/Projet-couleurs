from PIL import Image

canard=Image.open("duck.jpg")
print(canard.size())

pixels=canard.load()
for n in range(2):
    for i in range(328):
        pixels[i,n]=(0,0,0)

canard.show()