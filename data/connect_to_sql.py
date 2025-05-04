from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

###########################################################
#
# Run these in termial first:
# gcloud auth application-default login
# pip3 install pymysql
# 
###########################################################





def insert(pool):
    with pool.connect() as db_conn:
        # insert data into our ratings table
        insert_stmt = sqlalchemy.text(
            "INSERT INTO testing_table (pid, os_id, os, os_c, os_cp, paras, paras_c, paras_cp) "
            "VALUES (:pid, :os_id, :os, :os_c, :os_cp, :paras, :paras_c, :paras_cp)",
        )

        # insert entries into table
        db_conn.execute(insert_stmt, parameters={   "pid": "8088",
                                                    "os_id": "2222",
                                                    "os": "I am so hot",
                                                    "os_c":"TRUE",
                                                    "os_cp":70.78,
                                                    "paras":"so hot am I",
                                                    "paras_c":"TRUE",
                                                    "paras_cp":99.99})

        # commit transactions
        db_conn.commit()


def query(pool):
    with pool.connect() as db_conn:
        # query and fetch ratings table
        results = db_conn.execute(sqlalchemy.text("SELECT * FROM testing_table")).fetchall()

        # show results
        for row in results:
            print(row)

def create_table(pool):
    # interact with Cloud SQL database using connection pool
    with pool.connect() as db_conn:
        # create ratings table in our sandwiches database
        db_conn.execute(
            sqlalchemy.text(
            "CREATE TABLE IF NOT EXISTS testing_table "
            "( id SERIAL NOT NULL, "
            "pid VARCHAR(255) NOT NULL, "
            "os_id VARCHAR(255) NOT NULL, "
            "os TEXT NOT NULL, "
            "os_c VARCHAR(255) NOT NULL, "
            "os_cp FLOAT NOT NULL, "
            "paras TEXT NOT NULL, "
            "paras_c VARCHAR(255) NOT NULL, "
            "paras_cp FLOAT NOT NULL, "
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
        db="demo",
        ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
    )
    return conn

# create SQLAlchemy connection pool
# username:password@host:port/database
# mysql+pymysql://paraphraseluca:papihugh@34.13.217.210:3306/demo
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

#create_table(pool)
#insert(pool)
query(pool)

# close Cloud SQL Connector
connector.close()