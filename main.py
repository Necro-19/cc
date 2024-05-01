from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My first Google App Engine app!'

if __name__ == '__main__':
    app.run(debug=True)  # Remove this line for deployment
