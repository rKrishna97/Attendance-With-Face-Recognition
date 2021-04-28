########## IN PROGRESS

import cv2
import os
import face_recognition
from PIL import Image


class CollectFromVideo:
    def __init__(self):
        # self.video_path = "D:\GitHub\Face_Recognition_Attendance\videos\Robert_Downey_Jr.mp4"
        self.video_path = r"D:\GitHub\Face_Recognition_Attendance\videos"
        self.video_files = [os.path.join(self.video_path, i) for i in os.listdir(self.video_path)]
        self.cropped_image_path = r"D:\GitHub\Face_Recognition_Attendance\cropped_images"
        os.makedirs(self.cropped_image_path, exist_ok=True)

    def temp(self):
        for i in self.video_files:
            print(i)
            print(os.path.basename(i))
            print(os.path.splitext(os.path.basename(i))[0])

    def capture_face(self):
        for video in self.video_files:
            cap = cv2.VideoCapture(video)
            person_name = os.path.splitext(os.path.basename(video))[0]
            image_number = 0
            while image_number < 1000:
                ret, img = cap.read()
                img = cv2.resize(img, (480, 270))
                # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                try:
                    face_encodings_for_dict = face_recognition.face_encodings(img)
                    # face_locations = face_recognition.face_locations(img)
                    face_encoding_dict = {}
                    for i, encoding in enumerate(face_encodings_for_dict):
                        face_encoding_dict[i] = encoding

                    face_encoding = face_recognition.face_encodings(img)
                    face_location = face_recognition.face_locations(img)
                    encoding_location = zip(face_encoding, face_location)

                    for encodings, face_location in encoding_location:

                        for encode in encodings:
                            person_number_ls = []
                            for i, dict_encode in enumerate(list(face_encoding_dict.values())):
                                if face_recognition.compare_faces(encode, dict_encode):
                                    person_number_ls.append(i)

                            person_number = person_number_ls[0]

                            for i, location in enumerate(face_location):
                                top, right, bottom, left = location

                                cropped_image = img[top:bottom, left:right]
                                image_number = image_number + 1
                                # cv2.putText()
                                path = os.path.join(self.cropped_image_path, f"{person_name}")
                                os.makedirs(path, exist_ok=True)
                                filename = os.path.join(path, f"{person_number}_person_img_{image_number}.jpg")
                                cv2.imwrite(filename=filename, img=cropped_image)
                                cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 255), 2)
                except:
                    print("Face not detected")

                cv2.imshow('frame', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

            #         for i, face_location in enumerate(face_locations):
            #             top, right, bottom, left = face_location
            #
            #             cropped_image = img[top:bottom, left:right]
            #             image_number = image_number + 1
            #             # cv2.putText()
            #             path = os.path.join(self.cropped_image_path, f"{person_name}")
            #             os.makedirs(path, exist_ok=True)
            #             filename = os.path.join(path, f"{i}_person_img_{image_number}.jpg")
            #             cv2.imwrite(filename=filename, img=cropped_image)
            #             cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 255), 2)
            #     except:
            #         print("Face not detected")
            #
            #     cv2.imshow('frame', img)
            #     if cv2.waitKey(1) & 0xFF == ord('q'):
            #         break
            #
            # cap.release()
            # cv2.destroyAllWindows()


c = CollectFromVideo()
c.capture_face()
