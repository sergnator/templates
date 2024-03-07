from flask import Flask
from data import db_session
from data.ExampleClass import Example

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # change this


def main():
    db_session.global_init("db/example.db")  # change this
    # example values for table
    # start
    example = Example()
    example.id = 1
    example.name = 'example'
    example.value = 2
    session = db_session.create_session()
    session.add(example)
    session.commit()
    # end
    app.run()


if __name__ == '__main__':
    main()
