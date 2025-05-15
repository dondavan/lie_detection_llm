from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy



###########################################################
#
# Run these in termial first:
# gcloud auth application-default login
# pip3 install pymysql
# 
###########################################################


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
            "CREATE TABLE IF NOT EXISTS testing_table_time_production "
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

create_feedback_table(pool)
create_table_with_time(pool)

# close Cloud SQL Connector
connector.close()