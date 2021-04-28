import cv2
import face_recognition
from database.mongodb import MongoDB
from take_attendance.attendance import UpdateAttendance


class TakeAttendance:
    def __init__(self):
        # self.camera = cv2.VideoCapture(0)
        self.student_db = MongoDB(data_base="Student", collection="face_encode")
        self.update_attendance = UpdateAttendance()

    def take_attendance(self):
        while True:
            camera = cv2.VideoCapture(0)
            ret, img = camera.read()
            image = cv2.flip(img, 1)
            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            try:
                encodeFace = face_recognition.face_encodings(img)[0]
                faceLoc = face_recognition.face_locations(img)[0]
                cv2.rectangle(
                    image,
                    (faceLoc[3], faceLoc[0]),
                    (faceLoc[1], faceLoc[2]),
                    (255, 0, 255),
                    2
                )

                dpe, person_name = self.student_db.does_person_exist(encodeFace=encodeFace)

                if dpe:
                    attend_true = self.update_attendance.update_attendance(person_name)

                    if attend_true:
                        person_name = person_name.replace("_", " ")
                        cv2.putText(
                            image,
                            f"{person_name}: Attendance Taken",
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 0, 255),
                            2
                        )

            except Exception:
                print("Get in the frame\nOr\nPerson not in Database\n")

            cv2.imshow("Frame", image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()
