import boto3



def index_faces(image, id):
    aws_access_key_id = "ASIA453LFNKUME2T6BRA"
    aws_secret_access_key = "CCD8prglTy5zhdodGl/SL0sbRoIHgxL7adcNVSfi"
    aws_session_token = "IQoJb3JpZ2luX2VjEO7//////////wEaCXVzLXdlc3QtMiJGMEQCIGD6p70+VwEIs2tp8IrQGaowa4cS9B7++HMxzm4mYAaiAiA3OuFwDDX9yTGd9XJtlk1q/QRgk51HPnlRLzhYEPmMySq0AghnEAAaDDg4ODc0NjEwOTYwOCIMxis+QFMfZstg0gJsKpECm9SaKpv8gmGqUkpNumc8FGD3r5f5COjDjogJpR/xs6mqh27wEiZBY1yKVmiDKzvhrGuB26wAjbyo0KigFDPVxjvlcBVIt7DpRIYcVDzCEpV4wEEsm+JAMDjLdLPKhbwbV2k2Zh36A/FKsVg4bSTNfNWK/la19acIVEjz5zG/U4Wn/nmsjJKv6VB3LXuVXc2pDaFLB2buhk+Dn/ZCi3sDemOBn0zpCVHEjJuuyHdFbQdu55uabEHN2E0tvFDyV7CVD+uNoMGfOgg/u0yUMrbZs6YTlhrBLVT7F0GJF/ppR+vYHy7oJ8QZoYEg6guQ2+0LAXTc20OEZBQ1khmNTDLWESD0W0AayzWSdCTeKorspY4iMPjSubIGOp4BrsppShygHPrLrJLn2w/nf06XrQ2ddZTLaId32rZvZYEL3c6tH0xGnH01jX+o8g4L0p2AwCfvNPQZK8hv6YuRLrhNsk4VlhvQTBOdoD+e2UAsHxice2cbKnwkBcRHIbg7f5DDzGAxMfcyCsSfiEf47GV3IO+zmarggUl1J1FAGMAeYifADMDHIkC+QqQNnh9SSysSDhyioWZYPpr7Mcc="
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
