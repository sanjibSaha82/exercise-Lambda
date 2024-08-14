import boto3, os, json

ssm = boto3.resource('ssm')
s3 = boto3.resource('s3')


key = os.environ['UserName']


def lambda_handler(event, context):
   
    print("[INFO] STRING PARAMETER: "+ ssm.get_parameter(Name=UserName)['Parameter']['Value'])

      

    bucket_name = "parametersdatastoreb-bucket"
    lambda_path = "/tmp/" + UserName
    s3_path = "output/" + UserName
  
    return {
        'statusCode': 200,
        'body': json.dumps('file is store:'+s3/buckets/parametersdatastoreb-bucket)
    }

    
   
