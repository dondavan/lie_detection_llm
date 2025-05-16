from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import csv



###########################################################
#
# Run these in termial first:
# gcloud auth application-default login
# pip3 install pymysql
# 
###########################################################



def query_feedback(pool):
    Header = ["id","pid","motivation_scale","difficulty_scale","strategies","feedback"]
    table_name = "feedback_table_production"

    with pool.connect() as db_conn:
        # query and fetch ratings table
        results = db_conn.execute(sqlalchemy.text(f"SELECT * FROM {table_name}")).fetchall()


    with open(f"exp_data/saved_{table_name}.csv", "w", newline='') as csv_file:  # Python 3 version   
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(Header)
        csv_writer.writerows(results)

def query_statement(pool):
    Header = ["id","pid","os_id","os","os_c","os_cp","paras","paras_c", "paras_cp","start_time","end_time"]
    table_name = "statement_table_production"

    with pool.connect() as db_conn:
        # query and fetch ratings table
        results = db_conn.execute(sqlalchemy.text(f"SELECT * FROM {table_name}")).fetchall()


    with open(f"exp_data/saved_{table_name}.csv", "w", newline='') as csv_file:  # Python 3 version   
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(Header)
        csv_writer.writerows(results)


def create_feedback_table(pool):
    # interact with Cloud SQL database using connection pool
    with pool.connect() as db_conn:
        # create ratings table in our sandwiches database
        db_conn.execute(
            sqlalchemy.text(
            "CREATE TABLE IF NOT EXISTS feedback_table_production "
            "( id SERIAL NOT NULL, "
            "pid VARCHAR(255) NOT NULL, "
            "motivation_scale FLOAT NOT NULL, "
            "difficulty_scale FLOAT NOT NULL, "
            "strategies TEXT NOT NULL, "
            "feedback TEXT NOT NULL, "
            "PRIMARY KEY (id));"
            )
        )

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()

def create_table_with_time(pool):
    # interact with Cloud SQL database using connection pool
    with pool.connect() as db_conn:
        # create ratings table in our sandwiches database
        db_conn.execute(
            sqlalchemy.text(
            "CREATE TABLE IF NOT EXISTS statement_table_production"
            "( id SERIAL NOT NULL, "
            "pid VARCHAR(255) NOT NULL, "
            "os_id VARCHAR(255) NOT NULL, "
            "os TEXT NOT NULL, "
            "os_c VARCHAR(255) NOT NULL, "
            "os_cp FLOAT NOT NULL, "
            "paras TEXT NOT NULL, "
            "paras_c VARCHAR(255) NOT NULL, "
            "paras_cp FLOAT NOT NULL, "
            "start_time DATETIME NOT NULL, "
            "end_time DATETIME NOT NULL, "
            "PRIMARY KEY (id));"
            )
        )

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()

# initialize Cloud SQL Connector
connector = Connector()

# SQLAlchemy database connection creator function
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

def drop_existing_table(pool):
    with pool.connect() as db_conn:
        # create ratings table in our sandwiches database
        db_conn.execute(
            sqlalchemy.text(
            "DROP TABLE IF EXISTS feedback_table_production;"
            )
        )

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()

        # create ratings table in our sandwiches database
        db_conn.execute(
            sqlalchemy.text(
            "DROP TABLE IF EXISTS statement_table_production;"
            )
        )

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()
    
query_feedback(pool)
query_statement(pool)
drop_existing_table(pool)
create_feedback_table(pool)
create_table_with_time(pool)

# close Cloud SQL Connector
connector.close()