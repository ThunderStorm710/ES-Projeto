import boto3


def search_faces_by_image(image):
    aws_access_key_id = "ASIA453LFNKULIIZ7X5A"
    aws_secret_access_key = "UG8Fya0GhXSL+nyItOz/+52+LV3YBoHQnixwQj7P"
    aws_session_token = "IQoJb3JpZ2luX2VjEP7//////////wEaCXVzLXdlc3QtMiJIMEYCIQC12F7GrcGT2jEZzNkXLaK/D1GhSBsMRBCxCHv1Wm6AlQIhAO6H7gs9LhCDpZP1P7gQvNlWuV3D4wkQM2An/AURagCFKrQCCHcQABoMODg4NzQ2MTA5NjA4IgwcIQLzdRPF9kwJTXwqkQJx4z0wp/Nw0rutgIlbIKgI6apVHvPL6ER6NUX4ZT0Pw/cGEwjlhe5prpXpq6/4Rz2qAZ6eXRJYLkNVJyhxP7noETQ3CLidAJ/g1p4pszRuY0MszxjPbD+TSIx3OSD8Q42wAASBdvmy5pJ1JYOTJX6nmdTO9yxG8qeRYknRUNOL2mSi5ZEckVJRGuStpYC8+0Rdlffz0CQlR/yVkbwitZ/LJua748s9KCJCwzBBkO6krZc6Nrwpjja9vCNpDgFviZVQCCjlpfZHJWG7oqu+8EygPIUJVeGTyf9V1yQu3XJ5AzpYy1NcoJBZZiQ/3KXqcCgwKdZOgyeUZ93oROXCaJfOAffE8PKDvVHABpIbBIuZe/Qwrpi9sgY6nAGV3OrZnbBU5Yqx0m5+OmqsF1QIPBKTFT+AMP5Pnb46SAZ3d0guGcLNcuTEySPieaA0F6a2wWHyHsLyb3wjIkjgW2YDrRkjrpd+pSC2cBKjc1PTQ6XbdOblocDvrROjhs4NpnX7o/TPc/KqbjXAI6+NtoGwXZS85ISRA7AguiQ6YxsyKvMgmi4ZPJ14iaIhXyIwnpkDAPvosEb+aoc="

    s3 = boto3.resource('s3', region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

    client = boto3.client('rekognition', region_name='us-east-1',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          aws_session_token=aws_session_token)

    my_bucket = s3.Bucket('clinic-clients-images')

    with open(image, "rb") as image_file:
        imagem = image_file.read()

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

    '''
    response = client.search_faces_by_image(
        CollectionId='clinicasaudecollection',
        Image={
            'S3Object': {
                'Bucket': 'clinic-clients-images',
                'Name': '.jpg'
            }
        },
        MaxFaces=123,
    )
    '''
    response = client.list_faces(CollectionId='clinicasaudecollection')
    print(response['Faces'])

    response = client.search_faces_by_image(
        CollectionId='clinicasaudecollection',
        Image={'Bytes': imagem},
        MaxFaces=10,
        FaceMatchThreshold=95
    )

    print(response, "!!!")

    if 'ExternalImageId' in response['FaceMatches'][0]['Face']:
        return response['FaceMatches'][0]['Face']['ExternalImageId']
    else:
        return -1



if __name__ == '__main__':
    #with open("C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/images_5Athw6T.jpg", "rb") as image_file:
        #image1_bytes = image_file.read()
    search_faces_by_image("C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/Marcelo_Rebelo_de_Sousa_(Web_Summit).jpg")
