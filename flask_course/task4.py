from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/keliamieji", methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        year = int(request.form['year'])
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            year = "Leap year"
        else:
            year = "Is not a leap year"
        return render_template("greetings4.html", year=year)
    else:
        return render_template("login4.html")


if __name__ == "__main__":
    app.run()