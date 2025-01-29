import json

def lambda_handler(event, context):

  return {
      'statusCode': 200,
      'body': json.dumps('Hi! Hello! This is Lambda working with you.')
  }