import boto3

# Specify the AWS Region
aws_region = 'ap-southwest-2'  # Example: 'us-west-2', 'us-east-1', etc.


# Initialize a session using Amazon SQS
#session = boto3.session.Session()
#sqs = session.client('sqs',region_name=aws_region)

# AWS Credentials - Replace with your credentials
aws_access_key_id = 'AKIxxxxxxxxxxxxxxxxxxx'
aws_secret_access_key = 'pRjxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
aws_region = 'ap-southeast-2'  # Example: 'us-west-2'
# Initialize a session using Boto3 with explicit AWS credentials
sqs = boto3.client('sqs',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=aws_region)

# Get the queue URL
queue_url = 'https://xxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxx/SQS_q001'

counter=1 
while True:  # Send 10 messages in Loop 
    counter = counter + 1   
    messagetext='This is a Test Message from Jyoti.  This is the message to demo connection from Phython Code to SQS Counter#' + "{:06}".format(counter) + '\n Date of the Message  12/25/2023'
    if counter > 21:
        break   # break out of the loop after 10 iterations     
    # Send a message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
        'Title': { 'DataType': 'String', 'StringValue': 'Test Message from Jyoti' },
        'Author': {'DataType': 'String', 'StringValue': 'Jyoti'
        }
        },
        MessageBody=(messagetext)
    )
    print(response['MessageId'])


