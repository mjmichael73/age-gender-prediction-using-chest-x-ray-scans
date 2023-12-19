import os
from flask import Flask, render_template, request
from model import image_pre, predict

application = Flask(__name__)

UPLOAD_FOLDER = "./static"
ALLOWED_EXTENSIONS = {"png"}
application.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

GENDER_MALE = 1
GENDER_FEMALE = 0


@application.route('/')
def hello():
    return render_template("index.html")


@application.route("/", methods=["GET", "POST"])
def upload_file():
    result = ""
    if request.method in ["POST"]:
        if "image_file" not in request.files:
            return "There is not any image_file in the form."
        image_file = request.files["image_file"]
        path = os.path.join(application.config["UPLOAD_FOLDER"], "input.png")
        image_file.save(path)
        data = image_pre(path)
        age, gender = predict(data)
        if gender in [GENDER_MALE]:
            result = f"Predicted age is {str(age)} and the person is a Male."
        else:
            result = f"Predicted age is {str(age)} and the person is a Male."
    return render_template("index.html", result=result)


if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        debug=True
    )
