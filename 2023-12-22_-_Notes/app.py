from flask import Flask, render_template, redirect, url_for, request

app = Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        if "login" in request.form:
            user = request.form.get("user")
            password = request.form.get("password")

            if user == "julian" and password == "*****":
                return redirect(url_for("main"))

    return render_template("login.html")


@app.route("/notizen", methods=["POST", "GET"])
def main():

    if request.method == "POST":
        if "delete" in request.form:
            with open("static/notes.txt", "r") as f:
                lines = f.readlines()
            with open("static/notes.txt", "w") as f:
                for index, line in enumerate(lines, 1):
                    if index != int(request.form.get("id")):
                        f.write(line)

    data = []

    with open("static/notes.txt", "r") as fr:
        for index, line in enumerate(fr.readlines(), 1):
            split = line.strip("\n").split(" | ")

            data.append(
                {
                    "id": "{:02d}".format(index),
                    "date": split[0],
                    "note": split[1]
                }
            )

    return render_template("main.html", data=data)


@app.route("/notizen/neu", methods=["POST", "GET"])
def new():

    if request.method == "POST":
        if "add" in request.form:
            note = request.form.get("note")
            date = request.form.get("date")

            with open("static/notes.txt", "a") as fa:
                fa.write(date + " | " + note + "\n")

            return redirect(url_for("main"))

    return render_template("new.html")



if __name__ == "__main__":
    app.run()
