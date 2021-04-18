import pymongo

from app_logger.logger import AppLogger


class MongoDB:
    def __init__(self, data_base, collection):
        self.default_connection_url = "mongodb://localhost:27017/"
        self.client = pymongo.MongoClient(self.default_connection_url)
        self.db = self.client[data_base]
        self.collection = self.db[collection]
        self.log_file = open("logs/insert_face_encode.txt", "+a")
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
