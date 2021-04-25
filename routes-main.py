from flask import render_template, request, Blueprint
from Flask_Blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")

#We can create multiple 'routes' for our web mainlication that contain functions
#or refrences to templates, this results in multiple pages for a website

@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts, title='Ontario Covid-19 Q&A Forum')

@main.route("/about")
def about():
	return render_template('about.html', title='About')

@main.route("/FAQ1", methods=['GET', 'POST'])
def FAQ1():
		
	return render_template('FAQ1.html', title = 'How to Protect Yourself')

@main.route("/FAQ2", methods=['GET', 'POST'])
def FAQ2():
		
	return render_template('FAQ2.html', title = 'What is Physical Distancing?')

@main.route("/FAQ3", methods=['GET', 'POST'])
def FAQ3():
		
	return render_template('FAQ3.html', title = 'mRNA Vaccines')

@main.route("/FAQ4", methods=['GET', 'POST'])
def FAQ4():
		
	return render_template('FAQ4.html', title = 'How to Self-Isolate')



