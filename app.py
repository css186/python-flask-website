from flask import Flask, jsonify, render_template
from sqlalchemy import text
from database import load_job_from_db, load_jobs_from_db

app = Flask(__name__)

# JOBS = [{
#     "id": 1,
#     "title": "Data Analyst",
#     "location": "test",
#     "salary": "xxxx"
# }, {
#     "id": 2,
#     "title": "Data Scientist",
#     "location": "test2",
#     "salary": "1000"
# }, {
#     "id": 3,
#     "title": "Backend Engineer",
#     "location": "Taipei, Taiwan",
#     "salary": "3000"
# }, {
#     "id": 4,
#     "title": "Frontend Engineer",
#     "location": "test4",
#     "salary": "4000"
# }]


@app.route("/")
def index():
  current_jobs = load_jobs_from_db()
  return render_template("home.html", jobs=current_jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job=job)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
