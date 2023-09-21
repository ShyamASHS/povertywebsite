
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK with your service account key
cred = credentials.Certificate("/Users/Shyam/Downloads/ContactFrom_v1 2/cs-assessment-firebase-adminsdk-hxa7f-38bf62319a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Add the submitted data to the "submissions" collection
        db.collection('submissions').add({
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        })
        
        return redirect('/')
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

# Define routes for other pages similarly

if __name__ == '__main__':
    app.run(debug=True)
