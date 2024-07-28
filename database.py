from flask import jsonify
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

timeout = 10

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

def show_all_users():
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM users")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    print(rows)
    return rows

def load_rank_from_db(id):
    with engine.connect() as conn:
        # Use parameterized query
        result = conn.execute(text(f"CALL GetRanks({id})"))
        result_all = result.all()
        
        if result_all:
            req_rank = dict(result_all[0]._mapping)
            return jsonify(req_rank)
        else:
            return jsonify({"error": "No rank found for the given ID"}), 404

def load_all_ranks_from_db():
  with engine.connect() as conn:
    result = conn.execute(
       text(f"call getallranks")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return row
 
 
# Session = sessionmaker(bind=engine)
# session = Session()
# def add_application_to_db(job_id, data):
#     try:
#         query = text("""
#             INSERT INTO applications (
#                 job_id,
#                 full_name,
#                 email,
#                 linkedin_url,
#                 education,
#                 work_experience,
#                 resume_url
#             ) VALUES (
#                 :job_id,
#                 :full_name,
#                 :email,
#                 :linkedin_url,
#                 :education,
#                 :work_experience,
#                 :resume_url
#             )
#         """)
#         session.execute(query, {
#             'job_id': job_id,
#             'full_name': data['full_name'],
#             'email': data['email'],
#             'linkedin_url': data['linkedin_url'],
#             'education': data['education'],
#             'work_experience': data['work_experience'],  # Corrected key
#             'resume_url': data['resume_url']
#         })
#         session.commit()
#         print("Data committed successfully.")
#     except SQLAlchemyError as e:
#         session.rollback()
#         print(f"An error occurred: {e}")
#     finally:
#         session.close()