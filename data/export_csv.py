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

Header = ["id","pid","os_id","os","os_c","os_cp","paras","paras_c", "paras_cp","start_time","end_time"]

def query(pool):
    with pool.connect() as db_conn:
        # query and fetch ratings table
        results = db_conn.execute(sqlalchemy.text("SELECT * FROM testing_table_time")).fetchall()


    with open("exp_data/out.csv", "w", newline='') as csv_file:  # Python 3 version   
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(Header)
        csv_writer.writerows(results)

query(pool)