# sqs-pilot
### Introduction
SQS, or Simple Queue Service, is a powerful messaging system designed to help developers build scalable and reliable applications. It allows different components within a system to communicate with each other through message queues. Think of it as a virtual line where messages wait to be processed by various services or applications. By using SQS, developers can decouple the sender and receiver, making it easier to build distributed systems that can handle bursts of traffic without overloading the application. It ensures that messages are delivered at least once, and it provides various delivery modes for different use cases, including standard and FIFO queues. Whether you're building a simple application or a complex distributed system, SQS offers a reliable and scalable solution for handling message-based communication, making it a valuable tool in any developer's toolbox.
<br>
###### Introduction generated with the help of ChatGPT

### Steps:
1) Generate Access key on the AWS portal. We will require it to access the SQS.
2) Navigate to AWS SQS page and click on 'Create Queue' Button.
3) Click on the 'Create Queue' Button after you are done tweaking the settings according to your requirements. Once you click on the button, your Queue will now be up and running.
4) create a file with name ```secrets.py```. Add the necessary details in the file mentioned below.
```
  region_name = <region_name>
  aws_access_key_id = <generated_aws_access_key_id>
  aws_secret_access_key = <generated_aws_secret_access_key>
  queueName = <queue_name_you_created>
  queueUrl = <autogenerated_queue_url>
```
5) Run the file ```sendmessage.py``` in the terminal to insert message(s) into the SQS Queue.<br>
``` python sendmessage.py ```
6) Now to check for the messages inside the queue we will use another file with name ```receivemsg.py``` <br>
``` python receivemsg.py ``` <br> 
this should show you one of the messages inside the queue along with the attributes associated with the message.
7) We also need to delete the message from the queue once we recieve it. So to get that done we will use the file ```deletemsg.py```. This does the same thing as we did for receiving the messages. It also extracts the ```ReceiptHandle``` from the message object which is required to delete the message. <br>.
Then we use the code below to delete the message from the queue.<br>
```
client.delete_message(
    QueueUrl = queueUrl,
    ReceiptHandle = uniqueHandle
)
```
8) that's it! You have successfully utilized the power of AWS SQS.

###### If you need any help with it feel free to reach out.
