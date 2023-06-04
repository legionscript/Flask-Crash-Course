from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, World!'

@app.route('/user/<username>')
def profile(username):
	return f'Hello, {username}'

@app.route('/user/<first_name>/<last_name>')
def test_template(first_name, last_name):
	return render_template('test_user.html', first_name=first_name, last_name=last_name)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if request.method == 'POST':
# 		username = request.form['username']
# 		password = request.form['password']

# 		# handle user input here
# 		print(username, password)
# 		return render_template('login.html')
# 	else:
# 		return render_template('login.html')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Log In')

app.config['SECRET_KEY'] = 'secret_key'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		# handle user input here
# 		print(form)
# 		print(form.username)
# 		pass
# 	return render_template('new_login.html', form=form)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# db = SQLAlchemy(app)

# # 1. Create Models
# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String, unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=True)

# 	def __repr__(self):
# 		return '<User %r' % self.username

# # 2. Migrate Models to DB
# with app.app_context():
# 	db.create_all()

# 	# 3. Add Data
# 	user1 = User(username='testuser', email='testuser@test.com')
# 	user2 = User(username='testuser2')
# 	db.session.add(user1)
# 	db.session.add(user2)
# 	db.session.commit()

# 	# 4. Query Data
# 	users = User.query.all()
# 	testuser = User.query.filter_by(username='testuser').first()
# 	print(users)
# 	print(testuser)
# 	print(testuser.email)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

# Static Files
# 1. Set up static directory
# 2. url_for() - get the path for a static file