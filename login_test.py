
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user = db.Column(db.String(100), unique=True)
    password =db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    user = form.login.data
    password = form.password.data
    if form.validate_on_submit():
       # check if the user actually exists
        user = User.query.filter_by(user=user).first()
        if user:
            if check_password_hash(user.password,password):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for("index"))
            else:
                flash("login or password invalid")
                return render_template('login.html', login_form=form)
        else:
            flash("User not found")
            return render_template('login.html', login_form=form)
    return render_template('login.html', login_form=form)
#@app.route('/signup', methods=['POST', 'GET'])
#@login_required
#def signup_post():
#    signup = forms.SignForm()
#    name = signup.login.data
#    password = signup.password.data
#    if signup.validate_on_submit():
#        user = User.query.filter_by(user=name).first() # if this returns a user, then the email already exists in database
#        if user: # if a user is found, we want to redirect back to signup page so user can try again
#            return redirect(url_for('/signup'))
         # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#        new_user = User(user=name, password=generate_password_hash(password, method='sha256'))
        # add the new user to the database
#        db.session.add(new_user)
#        db.session.commit()
#        flash('Done')
#    return render_template('signup.html', signup=signup)
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("login"))