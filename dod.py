from PIL import Image, ImageFilter, ImageOps

img = Image.open('D:\\项目\\测试数据\\一寸照片.jpg')

def dodge(a, b, alpha):
    return min(int(a*255/(255-b*alpha)), 255)
def draw(img, blur = 25, alpha= 1.0):
    img1 = img.convert('L')  # 图片转换为灰色
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)
    for i in range(blur):   # 模糊度
        img2 = img2.filter(ImageFilter.BLUR)
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha))
    img1.show()
    img1.save('E:\\2.jpg')
    print('OK!')
draw(img)