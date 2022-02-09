import json
import base64
import boto3

#from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-02-09-21-08-42-810" ## TODO: fill in
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    #print("Received event: " + json.dumps(event, indent=2))

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor
    predictor = runtime.invoke_endpoint(EndpointName =ENDPOINT, ContentType = "image/png", Body= image)
## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    #predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = json.loads(predictor['Body'].read().decode())
    #predictor.predict(image, initial_args= {'ContentType': 'application/x-image'})## TODO: fill in
    #print(inferences)
    # We return the data back to the Step Function    
    event["inferences"] = inferences #.decode('utf-8')
    #print (event["inferences"] )
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }