import face_recognition
import pymongo

from app_logger.logger import AppLogger


class MongoDB:
    def __init__(self, data_base, collection):
        self.default_connection_url = "mongodb://localhost:27017/"
        self.client = pymongo.MongoClient(self.default_connection_url)
        self.db = self.client[data_base]
        self.collection = self.db[collection]
        self.log_file = open("../logs/insert_face_encode.txt", "+a")
        self.log_writer = AppLogger()

    def insert_face_encode(self, face_encode_dict):
        print("Inserting face encode started\n")
        self.log_writer.log(self.log_file, "Inserting face encode started")

        for key in face_encode_dict.keys():
            print(f"Name : {key} >>> Inserting face encode to database\n")
            self.log_writer.log(self.log_file, f"Name : {key} >>> Inserting face encode to database")
            encodings = []
            for i in range(0, len(face_encode_dict[key])):
                encode = face_encode_dict[key][i].tolist()
                encodings.append(encode)

            _ = self.collection.insert_one({"name": key, "encode": encodings})
            print("Done")
        print("Inserting Face Encode Complete")
        self.log_writer.log(self.log_file, "Inserting Face Encode")
        return "Done"

    def get_student_list(self):
        cursor = self.collection.find({})
        name_list = []
        for document in cursor:
            name_list.append(document["name"])
        cursor.close()
        return name_list

    def does_person_exist(self, encodeFace):
        cursor = self.collection.find({}, {"_id": 0})
        face_encode_list = []
        for document in cursor:
            face_encode_list.append(document)
        cursor.close()
        face_exist = []
        for i in face_encode_list:
            name, encode = i.items()
            name = name[1]
            face_encode = encode[1]
            result = []
            face_encode_match = face_recognition.compare_faces(face_encode, encodeFace)
            print(max(face_encode_match))
            face_exist.append(max(face_encode_match))

            if max(face_encode_match):
                person_name = name
        print(max(face_exist))
        return max(face_exist), person_name

    def check_if_student_present_in_attendance(self, student_name):
        cursor = self.collection.find({})
        name_list = []
        for document in cursor:
            name_list.append(document["name"])
        cursor.close()
        return student_name in name_list
