import csv
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

# initialize Cloud SQL Connector
connector = Connector()

def getconn():
    conn = connector.connect(
        "paraphrasing-attacks:europe-west4:paraphraseluca", # Cloud SQL Instance Connection Name
        "pymysql",
        user="paraphraseluca",
        password="papihugh",
        db="demo"
        #ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
    )
    return conn

# create SQLAlchemy connection pool
# username:password@host:port/database
# mysql+pymysql://paraphraseluca:papihugh@34.13.217.210:3306/demo
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


Header = ["id","pid","motivation_scale","difficulty_scale","strategies","feedback"]

table_name = "feedback_table_production"

def query(pool,table_name):
    with pool.connect() as db_conn:
        # query and fetch ratings table
        results = db_conn.execute(sqlalchemy.text(f"SELECT * FROM {table_name}")).fetchall()


    with open(f"exp_data/{table_name}.csv", "w", newline='') as csv_file:  # Python 3 version   
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(Header)
        csv_writer.writerows(results)

query(pool,table_name)