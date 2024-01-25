# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных,
# а пароль должен быть зашифрован.


from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from models import db, User
from flask_bcrypt import Bcrypt


from forms import RegistrationForm


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = b'fe03e9136de8b8096c0759a36231c83bd58bb3549af01d6df62c43944a37e778'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_hw3.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('base1.html')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(email, password)
        user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)




