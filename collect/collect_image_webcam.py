import cv2
import os


class CollectFromWebCam:
    def __init__(self, person_name):
        self.cascade_path = "D:/GitHub/Face_Recognition_Attendance/haar_cascade/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.person_name = person_name.replace(" ", "_")
        self.cropped_image_path = "D:/GitHub/Face_Recognition_Attendance/cropped_images"
        self.person_path = os.path.join(self.cropped_image_path, self.person_name)
        os.makedirs(self.person_path, exist_ok=True)

    def capture_face(self):
        cap = cv2.VideoCapture(0)
        count = 0
        while count < 50:
            ret, img = cap.read()
            # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(img, 1.2, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                crop_face = img[y:y + h, x:x + w]
                cv2.imwrite(filename=os.path.join(self.person_path, f"{self.person_name}_img_{count}.jpg"),
                            img=crop_face)
                count = count + 1
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img=img, text=f"{count}", org=org, fontFace=font, fontScale=fontScale, color=color,
                        thickness=thickness)

            cv2.imshow(f"{self.person_name.replace('_', ' ')}", img)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


