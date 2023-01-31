from flask import Flask, render_template, request
from api import generate_joke
from api import categories


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html', title='Home Page', categories=categories)


@app.route('/random_joke', methods = ['POST'])
def read_random_joke():
    
    chosen_category = request.form.get('chosen-categ')
    generated_joke = generate_joke(chosen_category)
    
    return render_template('results.html', title='Joke', joke=generated_joke, categories=categories)




@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    name = request.form['name']
    surname = request.form['surname']

    return render_template('submit.html', name=name, surname=surname)

if __name__=='__main__':
    app.run(debug=True)