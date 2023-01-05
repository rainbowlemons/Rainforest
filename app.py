from flask import Flask, jsonify, request, session
from flask_smorest import abort
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager
from dotenv import load_dotenv
import bcyrpt

from models.books import Book
from models.authors import Author
from models.publishers import Publisher
from models.tags import Tag

engine = create_engine("postgresql://postgres:postgres@db/postgres")
session = sessionmaker(bind=engine)()

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

load_env()
SECRET_KEY = os.getenv('SECRET_KEY')

app.secret_key = SECRET_KEY

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def hello():
    return "Hello welcome to my book store"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    if session.query(User.username).filter_by(username=username).first() is not None:
        return abort(400, message="This username is already in use!")
    
    email = request.form['email']
    if session.query(User.email).filter_by(email=email).first() is not None:
        return abort(400, message="This email is already in use!")

    salt = bcyrpt.gensalt()
    password = request.form['password']
    hash = bcrypt.hashpw(password, salt)

    user = User(username=username, email=email, password=hash)
    session.add(user)
    session.commit()

@app.route('/login')
def login():
     # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.rout('/logout')
@login_required
def logout():
    logout_user()
    return "User has been logged out"

@app.route('/books')
def get_books():
    if request.args.get('tag'):
        books = session.query(Book).filter(Book.tags.any(name=request.args.get('tag'))).all()
    else:
        books = session.query(Book).all()
    return jsonify(books)

@app.route('/book', methods=['GET'])
def get_book():
    book = session.query(Book).filter_by(id=request.args.get('id')).one()
    tags = book.tags
    book = book.__dict__
    book.pop('_sa_instance_state')
    #app.logger.info(tags)
    return jsonify(book)

@app.route('/authors')
def get_authors():
    authors = session.query(Author).all()
    return jsonify(authors)

@app.route('/publishers')
def get_publishers():
    publishers = session.query(Publisher).all()
    return jsonify(publishers)

@app.route('/book', methods=['POST'])
def create_book():
    book = Book(name=request.form['name'], 
                author_id=request.form["author_id"],
                publisher_id=request.form["publisher_id"])
    try:
        session.add(book)
        session.commit()
    except SQLAlchemyError as err:
        app.logger.info(err)
        abort(500, message="An error occured while inserting a book")
    return book.name

@app.route('/author', methods=['POST'])
def create_author():
    author = Author(name=request.form['name'])
    session.add(author)
    session.commit()
    return jsonify(author.id)

@app.route('/publisher', methods=['POST'])
def create_publisher():
    publisher = Publisher(name=request.form['name'])
    session.add(publisher)
    session.commit()
    return publisher.name

@app.route('/tag', methods=['POST'])
def create_tag():
    tag = Tag(name=request.form['name'])
    session.add(tag)
    session.commit()
    return tag.name

@app.route('/bookaddtag', methods=['POST'])
def book_add_tag():
    book = session.query(Book).filter_by(id=request.form['book_id']).one()
    tag = session.query(Tag).filter_by(id=request.form['tag_id']).one()
    book.tags.append(tag)
    session.add(book)
    session.add(tag)
    session.commit()
    return "okay"

@app.route('/book', methods=['DELETE'])
def book_deletion():
    book = session.query(Book).filter_by(id=request.args.get('id')).one()
    session.delete(book)
    session.commit()
    return "Deleted a book"

# @app.route('/cart')
# @login_required
# def get_cart():
#     return "This is your cart"

# @app.route('/checkout')
# @login_required
# def get_checkout():
#     return "WOW YOU JUST BOUGHT: BLUH"

# @app.route('/order')
# @login_required
# def get_order():
#     return "Your order here:"
