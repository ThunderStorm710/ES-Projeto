import boto3


def compare_faces(path):
    flag = False
    aws_access_key_id = "ASIA453LFNKUMKIW5K6C"
    aws_secret_access_key = "wu7Ec5oFeDahhUyt2nOpoQxzj6rSQ0sFY/DbNzzG"
    aws_session_token = "IQoJb3JpZ2luX2VjEOX//////////wEaCXVzLXdlc3QtMiJHMEUCIQC6bjbwvCFhwkv7WBvreR2YW4aqkfsGu9nPAZR0OloyZgIgY1KLPIJt+I4NVk3RzcyzlTHMVpS6/rTCIgi41WD82McqtAIIXhAAGgw4ODg3NDYxMDk2MDgiDAhfpJ8AfsCBqdVR/yqRAr/13fC313RLcKuhLibrjjsbWRcYcdksg1U+HcUzXHCACXFHVKogLW3pFyT4ZUeKA4nRkC6d/31G2yoP0wcShGQjQzSRSSt8kcsA2Mjntf5ulMjP2pLyJwyDRdd3DUFOJriwfZ/THDk9bCLJ5ITzn1n1pxRhmdPVYIHLodIDVDXy9h24LUdk2I+cfDA/XS0hayOMfB8kzsc4JQoptLdLgm1ZWLSy5xlc9VxE2BTDWarFEqOo8R6ATOUxn4gU77mtUEWmp+R2xzjjFxJe0YdMu2DxloE2RW8Q9Ssz4+mprh2zKAyoRsz2wXQo9J0be5p4o5vHaHb4DTt49bBOza5TAexFPD4HQh/3/6Z8RXVdr6k4LTDV3beyBjqdASZSpOaiBGYSy9R1UdXgc5gSmLk+bFGtaHWrLNGYaNd1cPWXt32EZp34IJDPi2DoLFuKRBiagmmL3jE3of64tV4Bq3WqgHlYsEcrouJWKlJ9V8Kk7yESp2upq11Tz4Z/B3c280QoOr805X6bNQdjJK94q1wpVte86WvNdNcSAJ1aHa+o5tGWmR64zEuizAMKiPqYGtr0kB5aDZcmUfc="
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
