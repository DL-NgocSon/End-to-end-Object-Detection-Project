import os
import cv2
import time
import uuid

IMAGE_PATH = "Collected_Images"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'Love', 'Please']

number_of_images = 5
for label in labels:
    img_path =os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    # open camera
    cap = cv2.VideoCapture(0)
    print(f'Collecting image for {label}')
    time.sleep(3)

    for img_num in range(number_of_images):
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        else:
            ret, frame = cap.read()
            img_name = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(img_name, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)
    cap.release()