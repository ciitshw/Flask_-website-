from project_files.init import app, db
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    #form = RegistrationForm()
    '''
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    '''
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)