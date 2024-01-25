# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from random import randint, choice

import pandas as pd
from flask import Flask
from models import db, Student, Marks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw3.db'
db.init_app(app)


tables = [Student, Marks]

def chek_tables():
    try:
        for table in tables:
            table.query.first()
        return True
    except Exception as e:
        print(e)
        return False

@app.cli.command("init-db")
@app.route('/db/init/')
def init_db():
    db.create_all()
    print('OK')
    return 'Созданы таблицы'


@app.cli.command("fill-db")
@app.route('/db/fill/')
def fill_db():
    for student in range(1, 6):
        new_student = Student(firstname=f'Имя {student}',
                          lastname=f'Фамилия {student}',
                          group=f'Группа {student}',
                          email=f'Email {student}')
        db.session.add(new_student)
    db.session.commit()


    for mark in range(1, 6):
        new_mark = Marks(student_id=randint(1, 5),
                          subject=f'Предмет {mark}',
                          mark=randint(1, 5))
        db.session.add(new_mark)
    db.session.commit()
    return 'Заполнены таблицы'


@app.cli.command("del-db")
@app.route('/db/del/')
def del_db():
    db.drop_all()
    return 'Удалены таблицы'


@app.route('/', methods=['GET', 'POST'])
def index():
    if not chek_tables():
        return 'Нет таблиц'
    students = [{'id': student.id,
            "firstname": student.firstname,
            "lastname": student.lastname,
            "group": student.group,
            "email": student.email,
            "marks": ", ".join([mark.subject + ': ' + str(mark.mark)
                                for mark in student.marks])}
    for student in Student.query.all()]
    if not students:
        return 'Таблица студентов пуста'
    html_table = pd.DataFrame(students).to_html(index=False)
    return html_table


if __name__ == '__main__':
    app.run(debug=True)



