#start virtual environment for python
/bin/echo "Starting python3 virtual environment"
source /home/script/mayank-assessment/venv/bin/activate

/bin/echo "Running assessment-script-part-1"

#Run python script for part-1
/home/scripts/mayank-assessment/scripts/python3 part-1-script.py

/bin/echo "files are downloaded from url and saved to download folder"

/bin/echo "synchronizing the files with S3 folder"
/usr/bin/aws s3 sync /home/scripts/mayank-assessment/downloads/ s3://mayank-assessment/part-1-files/

/bin/echo "files are in sync with S3"
