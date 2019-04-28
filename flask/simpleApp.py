from flask import Flask

PORT = 5000

app = Flask(__name__)

@app.route('/')
def homePage():
	return "Hello, welcome to the home page"


app.run(port=PORT)

