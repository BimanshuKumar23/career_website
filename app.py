from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $160,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'salary': '$130,000 - $170,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Remote',
        'salary': '$110,000 - $150,000'
    },
    {
        'id': 4,
        'title': 'Frontend Developer',
        'location': 'Austin, TX',
        'salary': '$100,000 - $140,000'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='TechCorp')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
