# ReArc-assessment

#### Part 1: AWS S3 & Sourcing Datasets
All the files from this open dataset https://download.bls.gov/pub/time.series/pr/ are downloaded to local and uploaded to S3 bucket.<br/>
The path of S3 bucket is given below:<br/>
s3://assessment-mayank-solanki/part-1-files/ <br/>

To run the script for Part 1: <br/>
- upload the assessment-script-part-1.py to EC2 instance
- setup the python3 virtual environment
- setup the download & script folder
- configure aws
<br/>
After the setup just run start.sh script to run python scripts and files will be synced to S3 bucket.<br/>
To keep the bucket in sync we can setup a cronjob which can run every day at specific time.
<br/>
<br/>
#### Part 2: APIs
Similar to Part 1 we can run this script for part 2 and the json file would be stored in respective download folder. <br/>
Script name : assessment-script-part-2.py <br/>
python3 assessment-script-part-2.py <br/>
<br/>
#### Part 3: Data Analytics
A notebook named 'Part-3-assessment.ipynb' is uploaded with the analisys and result of each section.<br/>
