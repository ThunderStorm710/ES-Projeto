import boto3

aws_access_key_id=""
aws_secret_access_key=""
aws_session_token=""

s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                      aws_session_token=aws_session_token)

my_bucket = s3.Bucket('clinic-clients-images')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)


response = client.search_faces_by_image(
    CollectionId='clinicasaudecollection',
    Image={
        'S3Object': {
            'Bucket': 'clinic-clients-images',
             'Name': '1.jpg'
        }
    },
    MaxFaces=123,
    )

print(response)