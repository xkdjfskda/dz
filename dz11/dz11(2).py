import cv2
from PIL import Image

image_path = 'cat.jpeg'
human_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
human_face = human_face_cascade.detectMultiScale(image)
human = Image.open(image_path)
glasses = Image.open('glasses1.png')
human = human.convert('RGBA')
glasses = glasses.convert('RGBA')
for (x, y, w, h) in human_face:
    glasses = glasses.resize((w, h // 3))
    human.paste(glasses, (x, y + h // 4), glasses)
    human.save('human_with_glasses.png')
