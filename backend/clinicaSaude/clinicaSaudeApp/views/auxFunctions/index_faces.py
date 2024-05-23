import boto3



def index_faces(image, id):
    aws_access_key_id = "ASIA453LFNKULIIZ7X5A"
    aws_secret_access_key = "UG8Fya0GhXSL+nyItOz/+52+LV3YBoHQnixwQj7P"
    aws_session_token = "IQoJb3JpZ2luX2VjEP7//////////wEaCXVzLXdlc3QtMiJIMEYCIQC12F7GrcGT2jEZzNkXLaK/D1GhSBsMRBCxCHv1Wm6AlQIhAO6H7gs9LhCDpZP1P7gQvNlWuV3D4wkQM2An/AURagCFKrQCCHcQABoMODg4NzQ2MTA5NjA4IgwcIQLzdRPF9kwJTXwqkQJx4z0wp/Nw0rutgIlbIKgI6apVHvPL6ER6NUX4ZT0Pw/cGEwjlhe5prpXpq6/4Rz2qAZ6eXRJYLkNVJyhxP7noETQ3CLidAJ/g1p4pszRuY0MszxjPbD+TSIx3OSD8Q42wAASBdvmy5pJ1JYOTJX6nmdTO9yxG8qeRYknRUNOL2mSi5ZEckVJRGuStpYC8+0Rdlffz0CQlR/yVkbwitZ/LJua748s9KCJCwzBBkO6krZc6Nrwpjja9vCNpDgFviZVQCCjlpfZHJWG7oqu+8EygPIUJVeGTyf9V1yQu3XJ5AzpYy1NcoJBZZiQ/3KXqcCgwKdZOgyeUZ93oROXCaJfOAffE8PKDvVHABpIbBIuZe/Qwrpi9sgY6nAGV3OrZnbBU5Yqx0m5+OmqsF1QIPBKTFT+AMP5Pnb46SAZ3d0guGcLNcuTEySPieaA0F6a2wWHyHsLyb3wjIkjgW2YDrRkjrpd+pSC2cBKjc1PTQ6XbdOblocDvrROjhs4NpnX7o/TPc/KqbjXAI6+NtoGwXZS85ISRA7AguiQ6YxsyKvMgmi4ZPJ14iaIhXyIwnpkDAPvosEb+aoc="
    s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

    client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                          aws_session_token=aws_session_token)


    #client.delete_collection(CollectionId='clinicasaudecollection')
    #response = client.create_collection(CollectionId='clinicasaudecollection')

    my_bucket = s3.Bucket('clinic-clients-images')

    '''
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
    '''
    # Convert the image to bytes
    image = open(image, 'rb')

    image_bytes = image.read()

    # Call AWS Rekognition to detect faces
    response = client.index_faces(
        CollectionId='clinicasaudecollection',
        Image={'Bytes': image_bytes},
        ExternalImageId=str(id),
        DetectionAttributes=['ALL']
    )

    # Extract the faceId
    face_id = response['FaceRecords'][0]['Face']['FaceId']
    print(face_id)
    print(response)

    response = client.list_faces(CollectionId='clinicasaudecollection')
    print(response['Faces'])

    return face_id


if __name__ == '__main__':
    image = open('C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/images.jpg', 'rb')
    index_faces('C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/FPFImageHandler.jpg', 18)
