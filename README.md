# How to run this app?
Be under the top-level dir of this repo: 
> sh run.sh

# Docker compose
at root dir
> docker-compose -f build/docker-compose.yaml up --build

#, "--server.address=0.0.0.0"

# Data DAO
##  Statement input
uid     Participant ID  Original statemnt ID    Original statement      class   class probability   Paraphrase      class   class probability

## prolific datafile
prolific datafile
Participant ID  Participant ID


## GCP sql detail
instance ID
paraphraseluca

password
papihugh


# How to deploy to the cloud
> sh build_and_deploy.sh
In terminal, select all of the y
and for regions, always select europe-west4-a.
the server is located in netherland( and we are in dutchland)


# How to use csv export magic button
go into /data folder
> python3 export_csv.py 
csv will be in foler /data/exp_data/
name: testing_table_time.csv


# Condition
It should be : 0 = deceptive, 1 = truthful 

distill-bert : 1 = deceptive, 0 = truthful
Data set : deceptive, truthful



# How to deploy to data collection
1. under /data folder, run
> python3 reset_statement_count.py

2. 