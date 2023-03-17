from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


# Конфигурация
DEBUG = True
SEKRET_KEY = 'dsfcdy7f76dvydf67b65f56csd6vdf7bdf7vdf78b67fd56csd5'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title



@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', title='Онлайн магазин', data=items)


@app.route('/about')
def about():
    return render_template('about.html', title='Про магазин')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']

        item = Item(title=title, price=price)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Ошибка отправления'

    else:
        return render_template('create.html', title='Добавление товара')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)