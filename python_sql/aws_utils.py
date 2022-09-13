import boto3
import os
from pathlib import Path

def get_aws_access_keys():
    """
    Description: This function retrieves access keys for the AWS S3 bucket where the database file is to be stored.
    

    Arguments:
        None

    Returns:
        Dictionary containing values for AWSAccessKeyId and AWSSecretKey
    """
    file_name = data_directory = str(Path.home()) + "/Desktop/University/data-science-and-business-analytics/programming-for-data-science/st2195_assignment_3/rootkey.csv"
    key_dictionary = {}
    with open(file_name, "r") as file:
        for line in file.readlines():
            key_dictionary[line.split("=")[0].strip()] = line.split("=")[1].strip()
    
    return key_dictionary


def aws_connect():
    """
    Description: This function is responsible for establishing the interface with the AWS S3 bucket where the database
    file should be stored.

    Arguments:
        None

    Returns:
        Boto3 client and resource objects
    """
    access_keys = get_aws_access_keys()
    
    # Creating the low level functional client
    client = boto3.client(
        's3',
        aws_access_key_id = access_keys['AWSAccessKeyId'],
        aws_secret_access_key = access_keys['AWSSecretKey'],
        region_name = 'eu-central-1'
    )

    # Creating the high level object oriented interface
    resource = boto3.resource(
        's3',
        aws_access_key_id = access_keys['AWSAccessKeyId'],
        aws_secret_access_key = access_keys['AWSSecretKey'],
        region_name = 'eu-central-1'
    )
    
    return client, resource


def upload_dbfile(filename):
    """
    Description: This function is responsible for uploading a given database file to the designated AWS S3 bucket.
    Once succesfully uploaded, the local file is deleted.

    Arguments:
        filename (string): name of the database file (format-agnostic)

    Returns:
        None
    """
    # generate AWS interface objects
    client, resource = aws_connect()
    
    try:   
        # open the file and upload to S3 bucket
        with open(filename, 'rb') as data:
            client.upload_fileobj(data, 'flights-db', 'db-file')

        # delete the local file
        os.remove(filename)
    except ClientError as e:
        print("Error uploading database file")