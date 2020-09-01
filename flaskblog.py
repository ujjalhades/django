from flask import Flask,render_template,url_for
app = Flask(__name__)

posts=[
	{
		'author':'ujjal bhowal',
		'title':'blog post 1',
		'content':'first post content',
		'date_posted':'august 29,2020'

	},
	{
		'author':'ratul',
		'title':'blog post 2',
		'content':'second post content',
		'date_posted':'august 30,2020'
	}
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title='home')


 
@app.route('/about')
def about():
    return render_template('about.html',title='About')
 

 