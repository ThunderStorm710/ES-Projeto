import boto3


def compare_faces(path):
    flag = False
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

    #imageSource = open("C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/10.jpeg", 'rb')
    imageSource = open(path, 'rb')
    imagem = imageSource.read()

    my_bucket = s3.Bucket('clinic-clients-images')


    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
        response = client.compare_faces(SimilarityThreshold=90,
                                        SourceImage={'Bytes': imagem},
                                        TargetImage={
                                                    'S3Object': {
                                                        'Bucket': 'clinic-clients-images',
                                                        'Name': f'{my_bucket_object.key}'
                                                    }
                                        })
        print(response)
        if len(response['FaceMatches']) != 0:
            flag = True
            for faceMatch in response['FaceMatches']:
                position = faceMatch['Face']['BoundingBox']
                similarity = str(faceMatch['Similarity'])
                print('The face at ' +
                      str(position['Left']) + ' ' +
                      str(position['Top']) +
                      ' matches with ' + similarity + '% confidence')

                print(len(response['FaceMatches']))
    imageSource.close()

    return flag


if __name__ == '__main__':
    compare_faces('C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/download.jpg')
