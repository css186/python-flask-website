from sqlalchemy import create_engine, text
import os
# database info
my_secret = os.environ["DB_CONNECTION_STRING"]

# create engine
engine = create_engine(my_secret,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# with engine.connect() as conn:
#   result = conn.execute(text("SELECT * FROM jobs"))

#   jobs_dict = []

#   for row in result.all():
#     jobs_dict.append(row._mapping)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []

    for row in result.all():
      jobs.append(row._mapping)

    return jobs
