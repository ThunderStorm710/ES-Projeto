import boto3


def search_faces_by_image(image):
    aws_access_key_id = "ASIA453LFNKUME2T6BRA"
    aws_secret_access_key = "CCD8prglTy5zhdodGl/SL0sbRoIHgxL7adcNVSfi"
    aws_session_token = "IQoJb3JpZ2luX2VjEO7//////////wEaCXVzLXdlc3QtMiJGMEQCIGD6p70+VwEIs2tp8IrQGaowa4cS9B7++HMxzm4mYAaiAiA3OuFwDDX9yTGd9XJtlk1q/QRgk51HPnlRLzhYEPmMySq0AghnEAAaDDg4ODc0NjEwOTYwOCIMxis+QFMfZstg0gJsKpECm9SaKpv8gmGqUkpNumc8FGD3r5f5COjDjogJpR/xs6mqh27wEiZBY1yKVmiDKzvhrGuB26wAjbyo0KigFDPVxjvlcBVIt7DpRIYcVDzCEpV4wEEsm+JAMDjLdLPKhbwbV2k2Zh36A/FKsVg4bSTNfNWK/la19acIVEjz5zG/U4Wn/nmsjJKv6VB3LXuVXc2pDaFLB2buhk+Dn/ZCi3sDemOBn0zpCVHEjJuuyHdFbQdu55uabEHN2E0tvFDyV7CVD+uNoMGfOgg/u0yUMrbZs6YTlhrBLVT7F0GJF/ppR+vYHy7oJ8QZoYEg6guQ2+0LAXTc20OEZBQ1khmNTDLWESD0W0AayzWSdCTeKorspY4iMPjSubIGOp4BrsppShygHPrLrJLn2w/nf06XrQ2ddZTLaId32rZvZYEL3c6tH0xGnH01jX+o8g4L0p2AwCfvNPQZK8hv6YuRLrhNsk4VlhvQTBOdoD+e2UAsHxice2cbKnwkBcRHIbg7f5DDzGAxMfcyCsSfiEf47GV3IO+zmarggUl1J1FAGMAeYifADMDHIkC+QqQNnh9SSysSDhyioWZYPpr7Mcc="

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
