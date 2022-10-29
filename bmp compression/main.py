import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import numpy as np


def svd_calculator(input_matrix):
  u, s, vh = np.linalg.svd(input_matrix, full_matrices=False)
  return u, s, vh


def reduce_k(u, s, vh, k):
  u = u[:, :k]
  s = s[:k, :k]
  vh = vh[:k]
  return u, s, vh


def recreation(image_loc,k, image):
  img = plt.imread(image_loc)

  # 2
  r = img[:, :, 0]
  g = img[:, :, 1]
  b = img[:, :, 2]

  # 3
  u1, s1, vh1 = svd_calculator(r)
  u2, s2, vh2 = svd_calculator(g)
  u3, s3, vh3 = svd_calculator(b)

  u1, s1, vh1 = reduce_k(u1, np.diag(s1), vh1, k)
  u2, s2, vh2 = reduce_k(u2, np.diag(s2), vh2, k)
  u3, s3, vh3 = reduce_k(u3, np.diag(s3), vh3, k)

  new_r = np.matmul(np.matmul(u1, s1), vh1)
  new_g = np.matmul(np.matmul(u2, s2), vh2)
  new_b = np.matmul(np.matmul(u3, s3), vh3)

  # stack r,g,b in depth
  new_img = np.dstack((new_r, new_g, new_b)).astype(np.uint8)
  plt.imshow(new_img)
  plt.savefig(os.getcwd() + '/new_images/k=' + str(k) + '-' + image.replace('.bmp','.jpg'))


ks = [10, 50, 150, 250]
for image in os.listdir(os.getcwd() + '/images'):
  for k in ks:
    recreation(os.getcwd() + '/images/' + image, k, image)
