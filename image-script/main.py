# from translate import Translator
# translate = Translator(to_lang='hi')

# print(translate.translate('Hello'))

from PIL import Image, ImageFilter

horse_img = Image.open('./images/horse.jpg')
blured_img = horse_img.filter(ImageFilter.BLUR)
smooth_img = horse_img.filter(ImageFilter.SMOOTH)

blured_img.save('./images/horseBlur.png', 'png')
smooth_img.save('./images/horseSmooth.png', 'png')

pikachu_img = Image.open('./images/pikachu.jpg')
pikachu_blur = pikachu_img.filter(ImageFilter.BLUR)
pikachu_smooth = pikachu_img.filter(ImageFilter.SMOOTH)
pikachu_bw = pikachu_img.convert("L")

pikachu_blur.save('./images/pikachuBlur.png' , 'png')
pikachu_smooth.save('./images/pikachuSmooth.png', 'png')
pikachu_bw.save('./images/pikachuBw.png', 'png')

pikachu_blur_smooth = Image.open('./images/pikachuBlur.png')
pikachu_blur_smooth.filter(ImageFilter.SMOOTH).save('./images/pikachu_blur_smooth.png', 'png')