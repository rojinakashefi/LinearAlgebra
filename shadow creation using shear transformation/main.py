from PIL import Image
import os

# first step
# convert an image to matrix
def load_image(image_loc):
  init_image = Image.open(image_loc)
  return init_image.load(), init_image.size[0], init_image.size[1]

# second & third step
# create a new matrix with more columns (x) for shadow
def create_shadow(pixels, x, y, transformation):
  # RED GREEN BLUE ALPHA
  # make x axis to expand because the shadow may get out of border
  shadow_image = Image.new('RGBA', size=(int(x * 1.3), y), color=(255, 255, 255, 255))
  shadow_pix = shadow_image.load()
  for i in range(x):
    for j in range(y):
      try:
        # some pictures has a (transparancy as well) (4 dimensions)
        r, g, b, a = pixels[i, j]
      except:
        r, g, b = pixels[i, j]
      # if the pixel have color
      if r < 255 or g < 255 or b < 255:
        # make it to gray as a shadow
        if transformation:
          # third step
          # shear transformation of shadow matrix
          shadow_pix[i + (i * 0.2), j] = pixels[i, j]
        else:
          # create a shadow matrix with out any transformation
          shadow_pix[i, j] = (70, 70, 70, 255)
  if transformation:
    shadow_image.save('shadow_transformation.png')
  else:
    shadow_image.save("shadow.png")
  return shadow_pix

# forth step
# if non white pixel exists get it from original metrix
# if white pixel look at transformed shadow matrix
# if gray pixel look at transoformet shadow matrix
def final_image(shadow_transformation,pixels,x,y):
  sec_image = Image.new('RGB', (int(x * 1.3), y), (255, 255, 255, 255))
  fin_image = sec_image.load()
  for i in range(int(x * 1.3)):
    for j in range(y):
      if i >= x or j >= y:
        # expanded section
        # put transformation in expanded section
        fin_image[i, j] = shadow_transformation[i, j]
      else:
        try:
          r, g, b, a = pixels[i, j]
        except:
          r, g, b = pixels[i, j]
        # if its white put shadow transformed matrix
        if r >= 250 and g >= 250 and b >= 250:
          fin_image[i, j] = shadow_transformation[i, j]
        else:
        # if it isnt white and we have color put input image pixel
          fin_image[i, j] = r, g, b
  return sec_image

image_loc = os.getcwd() + '/image.png'
# first step
pixels, x, y = load_image(image_loc)
# second step
shadow_pixels = create_shadow(pixels, x, y, False)
# third step
shadow_transformation = create_shadow(shadow_pixels,x,y,True)
# fourth step
final_img = final_image(shadow_transformation,pixels,x,y)
final_img.save('image_with_shadow.png')


