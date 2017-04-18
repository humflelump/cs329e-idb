from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''


@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
#ADD YOUR LABELS, BANDS LINKS/FUNCTIONS HERE
# you also have to change your references to css and images by adding ../static/	
@app.route('/label_defjam')
def label_defjam():
	return render_template('label-defjam.html')

@app.route('/Blues')
def Blues():
	return render_template('Blues.html')

@app.route('/Country')
def Country():
	return render_template('Country.html')

@app.route('/HipHop')
def HipHop():
	return render_template('HipHop.html')

@app.route('/Jazz')
def Jazz():
	return render_template('Jazz.html')

@app.route('/Pop')
def Pop():
	return render_template('Pop.html')

@app.route('/Rock')
def Rock():
	return render_template('Rock.html')
	
@app.route('/kPop')
def kPop():
	return render_template('kPop.html')
	
@app.route('/Genre')
def Genre():
	return render_template('genre.html')


	

if __name__ == "__main__":
    app.run()


