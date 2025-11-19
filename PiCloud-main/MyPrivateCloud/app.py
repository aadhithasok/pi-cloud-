from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Make sure this is a secret key for session management
UPLOAD_FOLDER = os.path.expanduser("~/PrivCloud")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user authentication
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    if current_user.is_authenticated:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('index.html', files=files)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace with real authentication
        if username == "admin" and password == "password":
            user = User(id=username)
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.", "success")
    return redirect(url_for('login'))

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('File successfully uploaded!', 'success')
        return redirect(url_for('home'))

@app.route('/download/<filename>')
@login_required
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    # Ensure file exists and then delete it
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash('File successfully deleted!', 'success')
    else:
        flash('Error: File not found.', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
