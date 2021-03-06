import numpy as np
import matplotlib.pyplot as plt
from feature_matching import *

def make_A_row(corner_1, corner_2):
  u1 = corner_1[0]
  uprime = corner_2[0]
  v1 = corner_1[1]
  vprime = corner_2[1]
  A_row = np.array([
  [0,0,0,-u1,-v1,-1,vprime*u1,vprime*v1,vprime],
  [u1,v1,1,0,0,0,-uprime*u1,-uprime*v1,-uprime]
  ])
  return A_row

def generate_A(corners_1, corners_2, n):
  A = np.zeros((2*n, 9))
  for i in range(0, 2*n, 2):
    A[i:i+2] = make_A_row(corners_1[i/2], corners_2[i/2])
  return A

def generate_homography(corners_1, corners_2, n):
  A = generate_A(corners_1, corners_2, n)
  U,Sigma,Vt = np.linalg.svd(A)
  return np.reshape(Vt[-1], (3, 3))

X = np.array([[0,0,1],
              [1,0,1],
              [1,1,1],
              [0,1,1],
              [0,0,1]])

H = np.random.rand(3,3)
#H/= H[2,2]

Xprime = (H.dot(X.T)).T
Xprime/=Xprime[:,2][:,np.newaxis]

H_gen = generate_homography(X, Xprime, 4)
'''
I_1 = plt.imread('photo_1.jpg')
I_2 = plt.imread('photo_2.jpg')

I_1 = I_1.mean(axis=2)
I_2 = I_2.mean(axis=2)

corners_1 = harris_corner_detection(I_1)
corners_2 = harris_corner_detection(I_2)

descriptors_1 = extract_descriptors(I_1, corners_1, 21)
descriptors_2 = extract_descriptors(I_2, corners_2, 21)

matches = get_min_descriptor_errors(descriptors_1, descriptors_2, .09).astype(int)

matching_corners_1 = corners_1[matches[:,0],:]
matching_corners_2 = corners_2[matches[:,1],:]


H = generate_H(matching_corners_1, matching_corners_2)
'''
