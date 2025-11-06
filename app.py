from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = []

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)

@app.route("/add-job", methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        job = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'location': request.form.get('location'),
            'company': request.form.get('company'),
            'salary': 'Competitive'
        }
        JOBS.append(job)
        return redirect(url_for('home'))
    return render_template("add-job.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
