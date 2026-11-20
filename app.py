from flask import Flask

#create the flask app
app = Flask(__name__)

#define the homepage
@app.route('/')
def home():
    return "Welcome to MiniForum!"

if __name__ == '__main__':
    app.run(debug=True)