import boto3
import json

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

modelId = 'cohere.command-text-v14'

def lambda_handler(event, context):
    try:
        print('Event: ', json.dumps(event))

        requestBody = json.loads(event['body'])
        prompt = requestBody['prompt']
        print('Prompt: ', prompt)

        body = {
            "prompt": prompt,
            "max_tokens": 400,
            "temperature": 0.75,
            "p": 0.01,
            "k": 0
        }
        body = {k: v for k, v in body.items() if k in ['prompt', 'max_tokens', 'temperature', 'p', 'k']}
        print('Body: ', json.dumps(body, indent=4))

        bedrockResponse = bedrock.invoke_model(modelId=modelId,
                                               body=json.dumps(body),
                                               accept='*/*',
                                               contentType='application/json')
        print('Bedrock Response: ', bedrockResponse)

        response = json.loads(bedrockResponse['body'].read())['generations'][0]['text']
        print('Response: ', response)

        apiResponse = {
            'statusCode': 200,
            'body': json.dumps({
                'prompt': prompt,
                'response': response
            })
        }
        print('API Response: ', apiResponse)

        return apiResponse

    except Exception as e:
        print('Error: ', str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }