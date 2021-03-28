import requests
r = requests.get('https://www.themealdb.com/api/json/v1/1/random.php/get')

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('request.html', meal=r)
if __name__ == '__main__':
    app.run(debug=True)