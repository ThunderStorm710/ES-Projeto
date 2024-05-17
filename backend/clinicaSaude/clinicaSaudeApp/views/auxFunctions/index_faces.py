import boto3

aws_access_key_id=""
aws_secret_access_key=""
aws_session_token=""
s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                      aws_session_token=aws_session_token)


client.delete_collection(CollectionId='clinicasaudecollection')

response = client.create_collection(CollectionId='clinicasaudecollection')


my_bucket = s3.Bucket('clinic-clients-images')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
    filename = my_bucket_object.key.split('/')[-1]
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        response = client.index_faces(
            CollectionId='clinicasaudecollection',
            Image={
                'S3Object': {
                    'Bucket': 'clinic-clients-images',
                    'Name': my_bucket_object.key
                }
            },
        )
        print(my_bucket_object, response, '\n\n')


response = client.list_collections()
print(response['CollectionIds'])

# Descrever uma coleção
response = client.describe_collection(CollectionId='clinicasaudecollection')
print(response)

# Listar faces indexadas na coleção
response = client.list_faces(CollectionId='clinicasaudecollection')
print(response['Faces'])
