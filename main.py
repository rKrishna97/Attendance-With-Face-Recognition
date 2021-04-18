from flask import Flask, request, render_template
from collect.collect_image_file import collect_image_files


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/collect_images", methods=["GET"])
def collect_images():
    try:
        collect = collect_image_files("images")
        names = collect.get_names()

        personFaceEncode = collect.get_face_encode(names)
    
    except Exception as e:
        print(e)
    
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
        

