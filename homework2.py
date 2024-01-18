# Создать страницу, на которой будет форма для ввода двух чисел
# и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата
# выбранной операции и переход на страницу с результатом.


from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = b'fe03e9136de8b8096c0759a36231c83bd58bb3549af01d6df62c43944a37e778'


@app.route('/')
def index():
    return render_template('base1.html')


@app.route('/calculate/', methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        return f'{num1} {operation} {num2} = {result}'
    return render_template('calculate.html')

# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


@app.route('/age_verifi/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= 18:
            return "Проверка пройдена"
        return "Проверка не пройдена"
    return render_template('age_verification.html')

# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('square.html')


# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
# где будет выведено "Привет, {имя}!".

@app.route('/flas/', methods=['GET', 'POST'])
def flas():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flas'))
    return render_template('flas.html')


# Создать страницу, на которой будет форма для ввода имени и электронной почты.
# При отправке которой, будет создан cookie файл с данными # пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными # пользователя и произведено перенаправление
# на страницу# ввода имени и электронной почты.


@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        if not request.form['username']:
            flash('Ошибка, вы забыли ввести имя !', 'danger')
            return redirect(url_for('log'))
        if not request.form['mail']:
            flash('Ошибка, вы забыли ввести почту !', 'danger')
            return redirect(url_for('log'))
        session['username'] = request.form.get('username')
        session['mail'] = request.form.get('mail')
        response = make_response(render_template('index.html', username=session['username'], mail=session['mail']))
        response.set_cookie('username', session['username'])
        response.set_cookie('mail', session['mail'])
        return response
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('mail', None)
    print(f'(Exit) username: {request.cookies.get("username")}')
    print(f'mail: {request.cookies.get("mail")}')
    response = make_response(render_template('log.html'))
    response.delete_cookie('username')
    response.delete_cookie('mail')
    return response


if __name__ == '__main__':
    app.run(debug=True)