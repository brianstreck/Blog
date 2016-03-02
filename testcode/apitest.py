from flask import Flask
app = Flask(__name__)

@app.route('http://jsonplaceholder.typicode.com', methods=['GET', 'POST'])
app.debug = True
app.run()
