import boto3



def index_faces(image, id):
    aws_access_key_id = "ASIA453LFNKUMU74524W"
    aws_secret_access_key = "NABlH/tLniw3yv7NuHZNw4WZc7UMdoeb2mgT8VSF"
    aws_session_token = "IQoJb3JpZ2luX2VjEOr//////////wEaCXVzLXdlc3QtMiJGMEQCIDygnYDrkQnaDs5YmL3hgkWjZ2bGls9TIOXTJ7Tk/HeQAiAJLUJSW4MVd3u+Q++PcnL0ArFjFBuP51zThvTCw3BbqCq0AghjEAAaDDg4ODc0NjEwOTYwOCIMM4gxf+FADCp+upeAKpECvgqgEGI9zRVe/HaDzYFYQm2iJtNpI3xOvQeWDpUDN4yv2n5xHyZjsCFIrow+fADMxcIFHXKexqd6PpfYbU33JBkQp1XzP8jKGijzleXKQqlOO/fEB87s5IkblS45ueIH8hcxfoElsGDnwPPJ+fbsR5GI6P0k1+6dGfhxM6xfVovXYenlXDbR3c69VlCuEjludsw2PlsVWaM52eOT7YLAUs+WDxwfl65yJISbPDMrPAAK8N2eclipWYJ+9947g6ZvrbkbYPLI2PZ5hOb2umMxfUmadaFeYCA2I+cuyDu2XTvKAMwlnzEWdWUf3OuQk1lrdoR3g7/CXXmHoDaQk7QPV1wMW555s3HpfhdLSxCksVTBMMnmuLIGOp4B2M/8EH6LAq9yJeZxYSkyubuuXVcq615LZEMaQcrs2DkRyDHvypXhJAOXHrF19q455xpn5Ogu/PmUgDydZAfhLOhuc6JEG2hwa7tNuocX79zxJe97t2eFX/9g1eDOeBcLehgM+cgpLeLVduJkXfsCcU5AN+Kah6KNZPlLJ9ePNgY7wVOBKo+CmD5eMOzT3BQ+headF/+N0LZhfRNa7zA="

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
    index_faces(image, 3)
