from tkinter import *
from PIL import Image, ImageTk
root=Tk()

def rsize(image):
    if image.size[1] > image.size[0]:  # 최소 이미지 사이즈를 400으로 맞춤.
        hSize = int((400 * image.size[0] / image.size[1]))
        vSize = 400
    else:
        hSize = 400
        vSize = int((400 * image.size[1] / image.size[0]))
    image = image.resize((hSize, vSize), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image
frame=Frame(root) #frame객체 생성
image = Image.open('/Users/NohTaeHyun/PycharmProjects/Tkinter/이미지 선택.png')
image = rsize(image)
imagelabel = Label(root, image=image)
imagelabel.pack()

root.mainloop()