import os
import re
import face_recognition
from cv2 import cv2
import shutil

class collect_image_files:
    def __init__(self, image_path):
        self.image_path = image_path

    # Getting names of those who are not present in the database
    def get_names(self):
        self.all_names = [i for i in os.listdir(self.image_path)]

        # # if space is present in the name, replacing it with underscore
        # for i,name in enumerate(self.all_names):
        #     if bool(re.search(r"\s", name)):
        #         self.all_names[i] = name.replace(" ", "_")

        self.student_list = [] # create a function to get student_list()
        self.names = [i for i in self.all_names if i not in self.student_list]
        return self.names

    def get_face_encode(self, names):
        person_dict = {}
        for name in names:
            lis = []
            for root, dirs, files in os.walk(f"images/{name}", topdown=False):
                for i in files:
                    lis.append(os.path.join(root, i))
            person_dict[name] = lis
        

        person_dict_encode = {}
        for name in names:
            print(f"Getting Face Encodings\n")
            print(f"Name: {name}\n")
            lisEncode = []
            for f in person_dict[name]:
                print(f"File: {f}")
                try:
                    # Loading image
                    img = face_recognition.load_image_file(f)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    # getting face encode
                    faceLoc = face_recognition.face_locations(img)[0]
                    faceEncode = face_recognition.face_encodings(img)[0]

                    lisEncode.append(faceEncode)
                    print(f"Done")
                    print()
                
                except:
                    print("Fail to detect face. Moving file to bad_file folder")
                    junk_file = os.path.basename(f)
                    print(f"{junk_file}")

                    if not os.path.exists(f"./bad_files/{name}"):
                        os.makedirs(f"./bad_files/{name}")
                    shutil.move(
                        f"./images/{name}/{junk_file}", f"./bad_files/{name}/{junk_file}"
                    )
                    print()
                    pass
            print()
            print(f"Done : {name}")
            print("="*100)
            person_dict_encode[name] = lisEncode
        return person_dict_encode

                

                    

# get names
# print(collect_image_files("images").get_face_encode())