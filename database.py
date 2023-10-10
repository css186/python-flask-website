from sqlalchemy import create_engine, text
import os
from datetime import datetime

# database info
my_secret = os.environ.get('DB_CONNECTION')

# create engine
engine = create_engine(my_secret,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def read_convert_data():
  output_list = []

  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    for row in result.all():
      output_list.append(row._asdict())

  return output_list


def load_jobs_from_db():
  jobs_list = read_convert_data()

  return jobs_list


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
