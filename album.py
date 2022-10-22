import os
import cv2

path = "C:/26JinDaniel/Pictures/Camera Roll"

images = []
for file in os.listdir(path):
    name,ext = os.splittext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        image = path + "/" + file
        images.append(image)

count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)

out = cv2.VideoWriter('album.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frame = cv2.imread(image)
    out.write(images[i])
out.release()