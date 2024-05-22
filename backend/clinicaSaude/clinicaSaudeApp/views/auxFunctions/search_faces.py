import boto3


def search_faces_by_image(image):
    aws_access_key_id = "ASIA453LFNKUMU74524W"
    aws_secret_access_key = "NABlH/tLniw3yv7NuHZNw4WZc7UMdoeb2mgT8VSF"
    aws_session_token = "IQoJb3JpZ2luX2VjEOr//////////wEaCXVzLXdlc3QtMiJGMEQCIDygnYDrkQnaDs5YmL3hgkWjZ2bGls9TIOXTJ7Tk/HeQAiAJLUJSW4MVd3u+Q++PcnL0ArFjFBuP51zThvTCw3BbqCq0AghjEAAaDDg4ODc0NjEwOTYwOCIMM4gxf+FADCp+upeAKpECvgqgEGI9zRVe/HaDzYFYQm2iJtNpI3xOvQeWDpUDN4yv2n5xHyZjsCFIrow+fADMxcIFHXKexqd6PpfYbU33JBkQp1XzP8jKGijzleXKQqlOO/fEB87s5IkblS45ueIH8hcxfoElsGDnwPPJ+fbsR5GI6P0k1+6dGfhxM6xfVovXYenlXDbR3c69VlCuEjludsw2PlsVWaM52eOT7YLAUs+WDxwfl65yJISbPDMrPAAK8N2eclipWYJ+9947g6ZvrbkbYPLI2PZ5hOb2umMxfUmadaFeYCA2I+cuyDu2XTvKAMwlnzEWdWUf3OuQk1lrdoR3g7/CXXmHoDaQk7QPV1wMW555s3HpfhdLSxCksVTBMMnmuLIGOp4B2M/8EH6LAq9yJeZxYSkyubuuXVcq615LZEMaQcrs2DkRyDHvypXhJAOXHrF19q455xpn5Ogu/PmUgDydZAfhLOhuc6JEG2hwa7tNuocX79zxJe97t2eFX/9g1eDOeBcLehgM+cgpLeLVduJkXfsCcU5AN+Kah6KNZPlLJ9ePNgY7wVOBKo+CmD5eMOzT3BQ+headF/+N0LZhfRNa7zA="

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
    #response = client.list_faces(CollectionId='clinicasaudecollection')
    #print(response['Faces'])

    response = client.search_faces_by_image(
        CollectionId='clinicasaudecollection',
        Image={'Bytes': imagem},
        MaxFaces=5,
        FaceMatchThreshold=95
    )

    if 'ExternalImageId' in response['Face']:
        return response['Face']['ExternalImageId']
    else:
        return -1



if __name__ == '__main__':
    with open("C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/download.jpg", "rb") as image_file:
        image1_bytes = image_file.read()
    search_faces_by_image(image1_bytes)
