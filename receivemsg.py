import boto3

from secret import region_name as region
from secret import aws_access_key_id as accessId
from secret import aws_secret_access_key as accessKey

from secret import queueName
from secret import queueUrl


client = boto3.client(
    'sqs', 
    region_name = region,
    aws_access_key_id = accessId, 
    aws_secret_access_key = accessKey
)

response = client.receive_message(
    QueueUrl=queueUrl,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

print(response['Messages'][0]['Body'])