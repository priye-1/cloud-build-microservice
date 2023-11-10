from flask import Flask

app = Flask('hello')


@app.route('/')
def hello():
    return "Hello World! I'm testing CI/CD ops\n"


if __name__ == '__main__':
    app.run()
