from flask import Flask, render_template

app = Flask(__name__)


html = """
<h1>"Моя первая страница"</h1>
<p>"Привет мир!"</p> 
<table>
</table>
"""


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'about!'


@app.route('/contact/')
def contact():
    return 'contact!'


@app.route('/sum/<int:a>/<int:b>/')
def sum_num(a, b):
    return f"{a}+{b}={a+b}"


@app.route('/str/<string:my_str>/')
def len_str(my_str):
    return f"{len(my_str)}"


@app.route('/html/')
def get_first_html():
    stud_list = ({'firstname': 'Иван', 'lastname': 'Иванов', 'age': '20', 'score': '4.5'},
                 {'firstname': 'Петр', 'lastname': 'Петров', 'age': '21', 'score': '3.2'},
                 {'firstname': 'Сидор', 'lastname': 'Сидоров', 'age': '22', 'score': '1.2'},
                 )
    return render_template('stud.html', stud_list=stud_list)


@app.route('/news/<int:num>/')
def get_news(num):
    base = [{'title':'title1', 'name': 'name1', 'date_pub': '2022'},
            {'title':'title2', 'name': 'name2', 'date_pub': '2023'},
            {'title':'title3', 'name': 'name3', 'date_pub': '2024'}
            ]
    context = base[num-1]
    print(context)
    return render_template('news.html', news=context)

if __name__ == '__main__':
    app.run(debug=True)
