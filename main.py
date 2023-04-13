from PIL import Image
'''img = Image.open("kitty.jpg")
img.show()
s1 = img.size[0]
s2 = img.size[1]
m = img.mode
f = img.format
print("ширина: ", s1)
print("высота: ", s1)
print("цветовая модель", m)
print("формат", f)'''

def z2():
    img = Image.open("kitty.jpg")
    copy1 = img.resize((220, 220))
    copy2 = img.transpose(Image.FLIP_TOP_BOTTOM)
    copy3 = img.transpose(Image.FLIP_LEFT_RIGHT)
    copy1.save("copy1.jpg")
    copy2.save("copy2.jpg")
    copy3.save("copy3.jpg")


from PIL import ImageFilter
def z3():
        spisok = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
        for i in spisok:
            img = Image.open(i)
            img = img.filter(ImageFilter.EMBOSS)
            img.show()
            img.save("new" + i)

def z4():
    spisok = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    vznak = Image.open("vz.png")

    vznak = vznak.filter(ImageFilter.CONTOUR)
    vznak = vznak.point(lambda x: 0 if x == 255 else 255)  # изменили пиксели со значением 255 и присвоили им значение 0, преобразовав их из белых в черные пиксели
    vznak = vznak.resize((vznak.width // 4, vznak.height // 4))
    #print(vznak.size)
    vznak = vznak.crop((1, 1, 244, 244))
    for i in spisok:
        img = Image.open(i)
        img.paste(vznak,(300, 160), vznak)
        img.show()


#z2()
#z3()
z4()