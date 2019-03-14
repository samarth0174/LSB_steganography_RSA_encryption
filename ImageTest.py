import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("2.png")
img2 = cv2.imread("enc_2.png")

length = 10

rows1, col1, _ = img1.shape
rows2, col2, _ = img2.shape
	
lst1 = []
lst2 = []

l = 0

for r in range(rows1):
    for c in range(col1):
        if(l<=length):
            lst1.append(img1[r,c][2])
            #print(img1[r,c][2])
        else:
            l = 0
            break
        l+=1

    if l==0:
        break

for r in range(rows2):
    for c in range(col2):
        if(l<=length):
            lst2.append(img2[r,c][2])
            #print(img2[r,c][2])
        else:
            l = 0
            break
        l+=1

    if l==0:
        break
        

plt.scatter(lst1, lst2)
plt.xlim(0, 20)
plt.ylim(0, 255)
plt.xlabel("Original Image Pixel Red Channel Value")
plt.ylabel("Encoded Image Pixel Red Channel Value")

b1, g1, r1 = cv2.split(img1)
b2, g2, r2 = cv2.split(img2)

print("Original Image Pixel Red Channel Values")
print(r1[0, : 10], "\n")
print("Encoded Image Pixel Red Channel Values")
print(r2[0, : 10], "\n")

rr1, cc1 = r1.shape
rr2, cc2 = r2.shape

euclid = np.sqrt(r1**2 - r2**2)
mean = np.mean(euclid)
std = np.std(euclid)

print("Mean of the Distace between original and encoded : ", mean)
print("Standard Deviation of the Distace between original and encoded : ", std, "\n")


euclid = np.sqrt(r1**2 - r1**2)
mean = np.mean(euclid)
std = np.std(euclid)
        

print("Mean of the Distace between original and original : ", mean)
print("Standard Deviation of the Distace between original and original : ", std)

plt.show()
