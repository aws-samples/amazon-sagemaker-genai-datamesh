import boto3
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-c", "--glue_crawler_name", help="script help")
args = argParser.parse_args()

client = boto3.client('glue')

# This is the command to start the Crawler
try:
    response = client.start_crawler(
        Name=args.glue_crawler_name 
    )
    print("Successfully started crawler. The crawler may take 2-5 mins to detect the schema.")
except:
    print("error in starting crawler. Check the logs for the error details.")
