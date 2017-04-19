from flask import Flask # Import Flask package
from flask import request
from copy import deepcopy
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'
app.jinja_env.autoescape = False

bandDict = {}
bandDict['The Beatles'] = 'The Beatles were one of the most influential rock bands of the 60s. Hailing from Liverpool, England, their members included John Lennon, Paul McCartney, Ringo Starr, and George Harrison. They led what is popularly known as the "British Invasion" of bands into the American popular music scene and culture and recognized worldwide.'
bandDict['Jackson 5'] = 'Founded by the elder Jackson brothers, Jackie, Tito, and Jermaine, and joined by their younger brothers, Marlon and Michael, The Jackson 5 gained tremendous popularity in the 70s and 80s. They were subsequently inducted into the Rock and Roll Hall of Fame in 1997. Today, their success in the popular music industry is attributed as inspiration for boy bands, such as N*SYNC, the Backstreet Boys, and One Direction.'
bandDict['The Roots'] = 'The roots is a hip hop band founded in 1987 and have been active since then. They are known for a more jazzy version of hip hop often featuring live musical instruments. Their band has had many members past and present but it was founded by Tariq Trotter and Ahmir Thompson in Philadelphia. Their band really became widely known after the release of "Things Fall Apart".'
bandDict['Alabama Shakes'] = 'Alabama Shakes is relatively known blues rock band that was founded in 2009. The Alabama-based have only released 2 albums since their formation. They have been nominated for a total 8 times for Grammy Awards, including Album of the Year, and eventually picking up 3 awards in less than 10 years. The band gain recognition with the release of their first album that highlighted the power and soul in the voice of lead singer, Brittney Howard.'
bandDict['Dixie Chicks'] = 'The Dixie Chicks is one of the most controversial acts in country music. The Dallas based band started in 1989 and consisted of4 women specializing in bluegrass music and country music. Six years, a new repertoire, and a new lead singer led to commercial success. The band played the festival circuits and small venues before attracting the attention of major record labels.'
bandDict['Lake Street Dive'] = 'Lake Street Dive is a multi-genre band based in Boston, Massachusetts. The band consists of former classmates of the New England Conservatory of Music. The band was named after a street in the hometown of Mike Olson, the guitarist, with many dive bars in Minneapolis, Minnesota. Each member of the band plays at least one instruments. Some have received classical music training or had musician parents.'

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
    global bandDict
    return render_template('index.html', bandDict = bandDict, editable = False) # located in templates/

@app.route('/about')
def about():
	return render_template('about.html', count = getCount())

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

@app.route('/band_lakestreetdive')
def band_lakestreetdive():
	return render_template('band-lakestreetdive.html')

@app.route('/band_shinee')
def band_shinee():
	return render_template('band-shinee.html')

@app.route('/band_theroots')
def band_theroots():
	return render_template('band-theroots.html')

@app.route('/indexedit', methods=['GET', 'POST'])
def indexedit():
    global bandDict
    return render_template('index.html', bandDict = bandDict, editable = True)

@app.route('/textupdated', methods=['GET', 'POST'])
def textupdated():
    global bandDict
    bandDict = deepcopy(request.form)
    return render_template('index.html', bandDict = bandDict, editable = False)

if __name__ == "__main__":
    app.run()
    #app.run('107.170.29.54', '80')


