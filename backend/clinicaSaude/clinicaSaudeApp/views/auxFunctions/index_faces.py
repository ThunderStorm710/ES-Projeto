import boto3

aws_access_key_id="ASIA453LFNKUMFQ4VOTB"
aws_secret_access_key="VSLvl4tNppyfX8av19DXrEFUKcjYAyVjGm3oC3EL"
aws_session_token="IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIHnflo7Zro5jgZ3R4pv9P1+MNrJiuLuZ1lmrG0JqksiOAiB7UhhggfVzRRU/mA2zPBN7a3Ml8czNjOFHvmbmBhjBGyq9Agi8//////////8BEAAaDDg4ODc0NjEwOTYwOCIMiFVVefRdY3Ir2bCpKpECttddykVcVKiNjrV7bGxtB9x6SGkbP6OvprqjlhIBV3rMLZ1xh/MMrKquod/lPou6Mm25yPAONFMlP90JSiBaXMoTVMGJm+oXWbRELnRyKUBESnD2YK4j2bxPD95P2OL+qshr7PM94GsXqjo8KnbtLs1kKNMPqP0cyTNe6JSb/XVUQCB30/1ydUk3fz9lDJjzxnlgmtzN/v7QAz79awuWtN3W0uxkXRtssoSCTJTLO28wzjy/DijusnkZYIqW1S4ipmkoN2ZheE/sQUDSpLfQTrOhLxvyrCXCJisYLeZPMB3MN6EPY+eSo7vgXB+BoJBmHUeHhAeNRirQtjPFcfnkzcXD4HMY41nv7lYaCv5ClrqHMMnIl7IGOp4Bb/8QI+seFObP9D8OeLX8QMnp9sXHgAQiIdgN8IosyLpHZtFJePAWu06T7mFiMYOyL3bL2G5TaThQJ88jGgWhtN2yhB7aDmMX/7zexXOmnKw1vZ/n5Si5dHSvAvvEx01hyQopwcvf2BO70qApt8lgk/FOU/11Vbikz066OBhUDblPC+P1LveyWh3unHBV0iAHr3VpdshmPVlh6agIYOY="
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
