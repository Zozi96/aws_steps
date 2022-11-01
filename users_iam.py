import boto3

iam = boto3.client('iam')

def get_users():
    users = iam.list_users()
    return users

print(get_users())