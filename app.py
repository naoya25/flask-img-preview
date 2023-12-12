from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "":
        return redirect(request.url)

    file_path = os.path.join("static/images", file.filename)
    file.save(file_path)

    return render_template("index.html", file_path=file_path)


if __name__ == "__main__":
    app.run(debug=True)
