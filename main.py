from flask import Flask, request, render_template
from collect.collect_image_file import CollectImageFiles
from database.mongodb import MongoDB

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/collect_images", methods=["GET"])
def collect_images():
    try:
        collect = CollectImageFiles("image_files")
        names = collect.get_names()
        db = MongoDB(data_base="Student", collection="face_encode")
        personFaceEncode = collect.get_face_encode(names)
        _ = db.insert_face_encode(face_encode_dict=personFaceEncode)


    except Exception as e:
        print(e)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
