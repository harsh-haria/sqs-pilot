import boto3

from secret import region_name as region
from secret import aws_access_key_id as accessId
from secret import aws_secret_access_key as accessKey

from secret import queueName

client = boto3.resource(
    'sqs', 
    region_name = region, 
    aws_access_key_id = accessId, 
    aws_secret_access_key = accessKey
)

queue = client.get_queue_by_name(QueueName = queueName)

response = queue.send_messages(Entries=[
    {
        "Id": "1",
        "MessageBody": "checkout",
        "MessageAttributes":{
            "product":{
                "StringValue": "ObjectId('64c4fe9c9fdabe7f8111bc3c')",
                "DataType":"String"
            }
        }
    }
])
print(response)