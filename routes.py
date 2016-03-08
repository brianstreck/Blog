from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/danceman')
def danceman():
    return render_template('danceman.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run()
