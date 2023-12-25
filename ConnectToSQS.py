import boto3

# Specify the AWS Region
aws_region = 'ap-southwest-2'  # Example: 'us-west-2', 'us-east-1', etc.


# Initialize a session using Amazon SQS
#session = boto3.session.Session()
#sqs = session.client('sqs',region_name=aws_region)

# AWS Credentials - Replace with your credentials
aws_access_key_id = 'AKIxxxxxxxxxxxxxxxxxx'
aws_secret_access_key = 'pRjxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# Initialize a session using Boto3 with explicit AWS credentials
sqs = boto3.client('sqs',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=aws_region)

# Get the queue URL
queue_url = 'https://xxxxxxxxxxxxx/xxxx/xxxxxxxxxxx/xxx'

# Send a message to the SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'My First SQS MESSAGE'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Jyoti'
        }
        
    },
    MessageBody=(
        'This is a Test Message from Jyoti'
        'This is the message to demo connection from Phython Code'
        'Date of the Message  12/25/2023'
    )
)

print(response['MessageId'])



