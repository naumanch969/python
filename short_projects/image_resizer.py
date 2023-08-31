from PIL import Image

def resize_image(width,height):
    image = Image.open('test.png')
    print(f'Current Size: {image.size}')
    resized_image = image.resize((width,height))
    resized_image.save('resized.png')

width = int(input('Enter width: '))
height = int(input('Enter height: '))
resize_image(width,height)