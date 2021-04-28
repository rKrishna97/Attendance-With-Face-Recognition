import os
from cv2 import cv2
import shutil


class CollectCroppedFaces:
    def __init__(self):
        self.cropped_image_path = "D:/GitHub/Face_Recognition_Attendance/cropped_images"
        self.image_path = "D:/GitHub/Face_Recognition_Attendance/image_files"
        self.cascade_path = "D:/GitHub/Face_Recognition_Attendance/haar_cascade/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.person_names = [i for i in os.listdir(self.image_path) if os.path.isdir(f"{self.image_path}/{i}")]

    def collect_cropped_faces(self):
        for name in self.person_names:
            folder = f"{self.image_path}/{name}"
            count = 0
            for file in os.listdir(folder):
                path = f"{self.image_path}/{name}/{file}"

                img = cv2.imread(filename=path)
                print(img)
                faces = self.face_cascade.detectMultiScale(img, 1.1, 5)

                for (x, y, w, h) in faces:
                    crop_face = img[y:y + h, x:x + w]
                    save_path = os.path.join(self.cropped_image_path, f"{name}")
                    os.makedirs(save_path, exist_ok=True)
                    print(save_path)
                    cv2.imwrite(filename=os.path.join(save_path, f"{name}_img_{count}.jpg"),
                                img=crop_face)
                count = count + 1


c = CollectCroppedFaces()
c.collect_cropped_faces()
