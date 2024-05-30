import boto3
import json

# Creating a client for Amazon SageMaker
sagemaker = boto3.client('sagemaker', region_name='us-west-2')

# Your input data
body = json.dumps({
    "instances": [
        {"data": {"prompt": "Test"}}
    ],
    "target_model": 'arn:aws:bedrock:us-west-2:105294882233:agent/WS6RZUACM3',
    "token_max_length": 300,
    "temperature": 0.1,
    "top_p": 0.9
})

# Invoke the SageMaker endpoint
response = sagemaker.invoke_endpoint(
    EndpointName='your-endpoint-name',
    Body=body,
    ContentType='application/json'
)

# Processing the response
response_body = response['Body'].read().decode('utf-8')
response_json = json.loads(response_body)
completion = response_json['predictions'][0]['generated_text']
print(completion)
