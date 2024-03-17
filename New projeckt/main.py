from PIL import Image, ImageFilter


with Image.open("rabstol_net_fast_and_furious_18_1920x1200.jpg") as original:
    pic_gray = original.convert('L')
    pic_gray.save('bw_pic.jpg')
    pic_gray.show()
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_blur.save('blur_pic.jpg')
    pic_blur.show()
    pic_up = original.transpose(Image.ROTATE_90)
    pic_up.save('rabstol_net_fast_and_furious_18_1920x1200.jpg')
    pic_up.show()
    
