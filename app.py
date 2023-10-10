from flask import Flask, jsonify, render_template
from sqlalchemy import text
from database import load_jobs_from_db

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


@app.route("/api/jobs")
def list_jobs():
  current_jobs = load_jobs_from_db()
  return jsonify(str(current_jobs))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
