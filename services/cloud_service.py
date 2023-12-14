import boto3

s3_bucket = "abou-contacts-bucket"

def uploadToS3(object_path: str, object_name = "contacts.json"):
    try:
        s3 = boto3.client('s3')
        f = open(object_path, "rb")
        s3.upload_fileobj(f, s3_bucket, object_name)
        print("Contacts uploaded to the cloud!")
    except Exception as e:
        print("Unable to upload the file to S3.")
        print(e)

def downloadContacts(file_name: str, object_name = "contacts.json"):
    try:
        s3 = boto3.client('s3')
        s3.download_file(s3_bucket, object_name, file_name)
    except Exception as e:
        print("Unable to download the file from S3.")
        print(e)