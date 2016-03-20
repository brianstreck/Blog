from flask import *
app = Flask(__name__)

@app.route('/')
def homebr():
    return render_template('homebr.html')

@app.route('/welcomebr')
def welcomebr():
    return render_template('welcomebr.html')

@app.route('/dancemanbr')
def dancemanbr():
    return render_template('dancemanbr.html')

@app.route('/recipebr')
def recipebr():
    return render_template('recipebr.html')

@app.route('/hellobr')
def hellobr():
    return render_template('hellobr.html')

@app.route('/logbr', methods=['GET', 'POST'])
def logbr():
    error = None
    usrnm = 'admin'
    pswrd = 'admin'
    if request.method == 'POST':
        if request.form['username'] != usrnm or request.form['password'] != pswrd:
            error = 'Invalid Credentials.'
        else:
            return redirect(url_for('hellobr'))
    return render_template('logbr.html', error = error)

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0')
    #app.run()
