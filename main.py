from flask import Flask, render_template
from collect.collect_image_webcam import CollectFromWebCam
from take_attendance.attendance_webcam import TakeAttendance

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/collect_face_webcam", methods=["GET"])
def collect_face_webcam():
    try:
        person_name = str(input("Enter the name: "))
        get_face = CollectFromWebCam(person_name=person_name)
        _ = get_face.capture_face()


    except Exception as e:
        print(e)

    return render_template("index.html")


@app.route("/collect_face_video", methods=["GET"])
def collect_face_video():
    try:
        person_name = str(input("Enter the name: "))
        get_face = CollectFromWebCam(person_name=person_name)
        _ = get_face.capture_face()


    except Exception as e:
        print(e)

    return render_template("index.html")


@app.route("/take_attendance", methods=["GET"])
def takeattendance():
    attendance_class = TakeAttendance()
    _ = attendance_class.take_attendance()


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
