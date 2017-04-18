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

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/label') 
def label():
	return render_template('label.html') 

@app.route('/band') 
def band():
	return render_template('band.html') 

@app.route('/genre') 
def genre():
	return render_template('genre.html') 
	
#ADD YOUR LABELS, BANDS LINKS/FUNCTIONS HERE
# you also have to change your references to css and images by adding ../static/	


@app.route('/label_ato')
def label_ato():
	return render_template('label-ato.html')

@app.route('/label_columbia')
def label_columbia():
	return render_template('label-columbia.html')

@app.route('/label_defjam')
def label_defjam():
	return render_template('label-defjam.html')

@app.route('/label_emi')
def label_emi():
	return render_template('label-emi.html')

@app.route('/label_motown')
def label_motown():
	return render_template('label-motown.html')

@app.route('/label_nonesuch')
def label_nonesuch():
	return render_template('label-nonesuch.html')

@app.route('/label_sment')
def label_sment():
	return render_template('label-sment.html')




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



@app.route('/band_beatles')
def band_beatles():
	return render_template('band-beatles.html')

@app.route('/band_alabamashakes')
def band_alabamashakes():
	return render_template('band-alabamashakes.html')

@app.route('/band_dixiechicks')
def band_dixiechicks():
	return render_template('band-dixiechicks.html')

@app.route('/band_jackson5')
def band_jackson5():
	return render_template('band-jackson5.html')

@app.route('/band_lakestreetdrive')
def band_lakestreetdrive():
	return render_template('band-lakestreetdrive.html')

@app.route('/band_shinee')
def band_shinee():
	return render_template('band-shinee.html')

@app.route('/band_theroots')
def band_theroots():
	return render_template('band-theroots.html')


	

if __name__ == "__main__":
    app.run()


