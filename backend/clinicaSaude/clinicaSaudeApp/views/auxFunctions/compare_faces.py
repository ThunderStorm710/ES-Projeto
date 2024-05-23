import boto3


def compare_faces(path):
    flag = False
    aws_access_key_id = "ASIA453LFNKULJBHV47W"
    aws_secret_access_key = "n6o5I7ftVD+HrmqzGZ2CQKaqOZS+mkdNvuvmtN1j"
    aws_session_token = "IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIF5M8A5YRy3wUNgitCGRTEhsTT8IMTZWSQefum209lPOAiBRlOKYcIJTWxDMGeUKHqji0L0PRUNuv9p769n96z0E+iq0Agh6EAAaDDg4ODc0NjEwOTYwOCIMXmqyWDHUXxRCjjIrKpECV6CU6k4MDNNqz/HJxiN2ItCdaSJHpV1/gp1RJvuFO633xm8nTx49niz/m7ewKqT17GGe5L5tPQ6lhOsGaoF8QAjb2VQ4NurpFw/PqBP0FVXsRBpsvQ75e4sI0ib6L6Qsf5C5ido2Z3ld4RlhS/B7xI+mfH0vgUDyCRVl3EHrAESS3evPMhR/UIvAZLvqblnduWjmNVj+EERdnyIpk65phJOFUBVkGNYBla8oH+gcpOaXvx36PDS3B7597cisTO7rGWVmlJ4B9Itx45zYHddcORwyYVJAOxqRfJDnJhQBjI+0Czgftx29s9VDjRufkXnRCk4Nc+1RoZPfp4Tf0VDNMp1qISAMLaX1m2kJeB9yoqK9ML/uvbIGOp4B9/a5kzdDdGFV4X/rRkCaJN0L55JfHtEkpnIpQIsdjBfJGzNiR1DJqLK+ALNEGrGv9jlMBJ/84Lg9nmflvwJ0rU+9vxZBHvv5kuQ8+qfRvgwh/UaAjCdTYkOgeS94/ht39JOT0v5fAF6pCBguYf/0dzucDDdRZkKvZlruJyQKCQk1pQzyS1QPa4cpvSyvRGn5kcmDgd6/2Daze52OGdo="

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
