import datetime

from flask import Flask, jsonify, request
from sqlalchemy import (
    Column,
    INTEGER,
    String,
    DATE,
    FLOAT,
    BOOLEAN,
    DATETIME,
    create_engine,
    and_,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///hw.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
app = Flask(__name__)


class Books(Base):
    __tablename__ = "books"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(INTEGER, default=1)
    release_date = Column(DATE, nullable=False)
    author_id = Column(INTEGER, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = "authors"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Students(Base):
    __tablename__ = "students"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(FLOAT, nullable=False)
    scholarship = Column(BOOLEAN, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_students_by_score_higher_then(cls, score):
        return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBooks(Base):
    __tablename__ = "receiving_books"
    id = Column(INTEGER, primary_key=True)
    book_id = Column(INTEGER, nullable=False)
    student_id = Column(INTEGER, nullable=False)
    date_of_issue = Column(DATETIME, nullable=False)
    date_of_return = Column(DATETIME)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days, "Книга в библиотеке"
        else:
            return (
                datetime.datetime.now() - self.date_of_issue
            ).days, "Книга у читателя"


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route("/get_books", methods=["GET"])
def get_books():
    books_list = []
    for book in session.query(Books).all():
        books_list.append(book.to_json())

    return jsonify(books_list=books_list), 200


@app.route("/get_books_by_name/<string:name>", methods=["GET"])
def get_books_by_name(name):
    books_list = []
    for book in session.query(Books).filter(Books.name.like(f"%{name}%")).all():
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200


@app.route("/get_debtors", methods=["GET"])
def get_debtors():
    debtors_list = []
    for receiving_book in (
        session.query(ReceivingBooks)
        .filter(ReceivingBooks.date_of_return == None)
        .all()
    ):
        if receiving_book.count_date_with_book[0] > 14:
            debtors_list.append(receiving_book.to_json())

    return jsonify(debtors_list=debtors_list), 200


@app.route("/issue_book", methods=["POST"])
def issue_book():
    book_id = request.form.get("book_id")
    student_id = request.form.get("student_id")
    session.add(
        ReceivingBooks(
            book_id=book_id,
            student_id=student_id,
            date_of_issue=datetime.datetime.now(),
        )
    )
    book = session.query(Books).get(book_id)
    book.count = book.count - 1
    session.commit()

    return f"Книга {book_id} выдана студенту {student_id}"


@app.route("/pass_book", methods=["POST"])
def pass_book():
    book_id = request.form.get("book_id")
    student_id = request.form.get("student_id")
    receiving_book = (
        session.query(ReceivingBooks)
        .filter(
            and_(
                ReceivingBooks.student_id == student_id,
                ReceivingBooks.book_id == book_id,
                ReceivingBooks.date_of_return == None,
            )
        )
        .one_or_none()
    )
    if receiving_book:
        receiving_book.date_of_return = datetime.datetime.now()
        book = session.query(Books).get(book_id)
        book.count = book.count + 1
        session.commit()
        return f"Книга {book_id} сдана"
    else:
        return f"Связка книги({book_id}) и студента({student_id})не найдена"


if __name__ == "__main__":
    app.run(debug=True)
