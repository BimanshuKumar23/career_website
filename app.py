from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = []

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)
  

@app.route("/add-job", methods=['GET', 'POST'])
def add_job():
    """
    Handles the addition of new job postings.

    On GET requests, it renders the 'add-job.html' template, displaying a form for job details.
    On POST requests, it retrieves job details from the form, creates a job dictionary,
    appends it to the JOBS list, and redirects the user to the home page.
    """
    if request.method == 'POST':
        # Retrieve job details from the form
        job = {
            'title': request.form.get('title'),
            'company': request.form.get('company'),
            'location': request.form.get('location'),
            'salary': request.form.get('salary'),
            'description': request.form.get('description'),
            'responsibilities': request.form.get('responsibilities'),
            'qualifications': request.form.get('qualifications'),
            'date_posted': request.form.get('date_posted'),
            'is_active': request.form.get('is_active') == 'True'
        }
        JOBS.append(job)
        return redirect(url_for('home'))
    return render_template("add-job.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
