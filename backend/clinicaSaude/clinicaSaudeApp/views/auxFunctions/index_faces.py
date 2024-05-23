import boto3



def index_faces(image, id):
    aws_access_key_id = "ASIA453LFNKULJBHV47W"
    aws_secret_access_key = "n6o5I7ftVD+HrmqzGZ2CQKaqOZS+mkdNvuvmtN1j"
    aws_session_token = "IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIF5M8A5YRy3wUNgitCGRTEhsTT8IMTZWSQefum209lPOAiBRlOKYcIJTWxDMGeUKHqji0L0PRUNuv9p769n96z0E+iq0Agh6EAAaDDg4ODc0NjEwOTYwOCIMXmqyWDHUXxRCjjIrKpECV6CU6k4MDNNqz/HJxiN2ItCdaSJHpV1/gp1RJvuFO633xm8nTx49niz/m7ewKqT17GGe5L5tPQ6lhOsGaoF8QAjb2VQ4NurpFw/PqBP0FVXsRBpsvQ75e4sI0ib6L6Qsf5C5ido2Z3ld4RlhS/B7xI+mfH0vgUDyCRVl3EHrAESS3evPMhR/UIvAZLvqblnduWjmNVj+EERdnyIpk65phJOFUBVkGNYBla8oH+gcpOaXvx36PDS3B7597cisTO7rGWVmlJ4B9Itx45zYHddcORwyYVJAOxqRfJDnJhQBjI+0Czgftx29s9VDjRufkXnRCk4Nc+1RoZPfp4Tf0VDNMp1qISAMLaX1m2kJeB9yoqK9ML/uvbIGOp4B9/a5kzdDdGFV4X/rRkCaJN0L55JfHtEkpnIpQIsdjBfJGzNiR1DJqLK+ALNEGrGv9jlMBJ/84Lg9nmflvwJ0rU+9vxZBHvv5kuQ8+qfRvgwh/UaAjCdTYkOgeS94/ht39JOT0v5fAF6pCBguYf/0dzucDDdRZkKvZlruJyQKCQk1pQzyS1QPa4cpvSyvRGn5kcmDgd6/2Daze52OGdo="

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
