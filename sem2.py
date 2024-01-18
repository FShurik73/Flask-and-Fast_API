from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base1.html")

@app.get('/about/')
def about():
    return render_template("about.html")


@app.post('/about/')
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
    return "Файл отправлен"


if __name__ == '__main__':
    app.run(debug=True)