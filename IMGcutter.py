import cv2

#only for 1280 * 720 images (HD images)

img_file = "./images/SlidegameImages/IMGcut"                         # put where you want to save
cut_file = "./images/SlidegameImages/numpuz/puz-ferrari/ferrari.jpg" # put the file that you want to cut
img_name = "/cuttedimage"                                           # put the name of cut files

image = cv2.imread(cut_file, cv2.IMREAD_COLOR)
imgcpy = image.copy()

cv2.line(imgcpy, (0, 319), (401, 319), (0, 0, 0), 6)
cv2.line(imgcpy, (401, 319), (401, 720), (0, 0, 0), 6)
path = img_file + img_name + "Original.jpg"
cv2.imwrite(path, imgcpy)

#1
imgcpy = image[320:420, 100:200]
path = img_file+img_name+"1.jpg"
cv2.imwrite(path, imgcpy)
#2
imgcpy = image[320:420, 200:300]
path = img_file+img_name+"2.jpg"
cv2.imwrite( path, imgcpy )
#3
imgcpy = image[320:420, 300:400]
path = img_file+img_name+"3.jpg"
cv2.imwrite( path, imgcpy )


#4
imgcpy = image[420:520, 0:100]
path = img_file+img_name+"4.jpg"
cv2.imwrite( path, imgcpy )
#5
imgcpy = image[420:520, 100:200]
path = img_file+img_name+"5.jpg"
cv2.imwrite( path, imgcpy )
#6
imgcpy = image[420:520, 200:300]
path = img_file+img_name+"6.jpg"
cv2.imwrite( path, imgcpy )
#7
imgcpy = image[420:520, 300:400]
path = img_file+img_name+"7.jpg"
cv2.imwrite( path, imgcpy )


#8
imgcpy = image[520:620, 0:100]
path = img_file+img_name+"8.jpg"
cv2.imwrite( path, imgcpy )
#9
imgcpy = image[520:620, 100:200]
path = img_file+img_name+"9.jpg"
cv2.imwrite( path, imgcpy )
#10
imgcpy = image[520:620, 200:300]
path = img_file+img_name+"10.jpg"
cv2.imwrite( path, imgcpy )
#11
imgcpy = image[520:620, 300:400]
path = img_file+img_name+"11.jpg"
cv2.imwrite( path, imgcpy )


#12
imgcpy = image[620:720, 0:100]
path = img_file+img_name+"12.jpg"
cv2.imwrite(path, imgcpy)
#13
imgcpy = image[620:720, 100:200]
path = img_file+img_name+"13.jpg"
cv2.imwrite( path, imgcpy )
#14
imgcpy = image[620:720, 200:300]
path = img_file+img_name+"14.jpg"
cv2.imwrite( path, imgcpy )
#15
imgcpy = image[620:720, 300:400]
path = img_file+img_name+"15.jpg"
cv2.imwrite( path, imgcpy )

print("Cutting Clear")