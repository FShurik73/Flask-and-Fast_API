# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about_us():
    return render_template("store.html")

@app.route('/contacts/')
def contacts():
    contacts_list = ({'department': 'Техническая поддержка', 'number': '+7 800 500 00 00', 'email': 'hotline@my_shop.ru'},
                     {'department': 'Пункт выдачи заказов', 'number': '+7 555 333 77 77', 'email': 'punkt@my_shop.ru'},
                     {'department': 'Отдел по сотрудничеств', 'number': '+7 555 222 77 22', 'email': 'сooperation@my_shop.ru'},
                     )
    return render_template("contacts.html", contacts_list=contacts_list)


@app.route('/company/')
def company():
    return render_template("company.html")


@app.route('/clothes/')
def clothes():
    return render_template("clothes.html")

@app.route('/shoes/')
def shoes():
    return render_template("shoes.html")

@app.route('/clothes/jacket/')
def jacket():
    return render_template("jacket.html")

if __name__ == '__main__':
    app.run(debug=True)