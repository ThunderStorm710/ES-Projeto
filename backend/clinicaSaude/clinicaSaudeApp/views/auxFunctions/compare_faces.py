import boto3


def compare_faces(path):
    flag = False
    aws_access_key_id = "ASIA453LFNKUHD4X7ODB"
    aws_secret_access_key = "xdwrTgechw6Gw25CPC6+kYR95U0HYCgO9Bm7lHqt"
    aws_session_token = "IQoJb3JpZ2luX2VjENr//////////wEaCXVzLXdlc3QtMiJGMEQCIF6QbGuVTu4Y7dP9gKkyeAiNb/FC2SaEI/wttM9ZUSN8AiA5j+tZgmnzsxy2+qYb4Ke9Ll2OlYsH6RwxyIrcUwo4byq0AghTEAAaDDg4ODc0NjEwOTYwOCIMzT2pNv2cGdJUpo4WKpECZoG7ejm66q2tuGCklmJRQ2Dr4gXjjil8WrjbFWk+vFfcc3Z6lVcprlzqZocAA9uP8jd+HV3pgsycRscDrUSnLnqmyGmXszLcCSVG710/vGGK/CEeNVmxfB8nHJZYmVN4676hbkmdI2PCwt1g5g1sfcnnOHw+mYAA1SV2tXxE6C6Cm79H3+KtNpSi93vcMr6I8JKVb3iEM2544CHC7GV+rCJvaeyS1zduUkNOOesO5XN2bZHUtTYqRQSgCvTdV3NZjFoS2pmGR6YL0GO3bnCubuLjd/N4bRdWnhXf+6/7R31Xgz5jSHUW8onKN6i3IJ+BiObjjbJY7g0WS7bJD/l3FvCly+qAe9RTqKoIYG//N0lkMOqktbIGOp4B6zGI+6EcEB9JH0/4plyfZrRwK0rXNeIVHCNpAPVe4bahvRyMyJotpbx/IZ6mCKefj6Fgn6BEbOW8v8PWM8ex2tv+ByG+DXvsfCknp1bPELeOQXT6FtBl3zD2y8BhyNbVp2Ftk03SNeO3F1DoDjUshBwY22qPf7UcY+Iv3sWQqeudbCIq7oyNTaeWBQCWmlImyPXhDsI1Vg0N0/hruxU="
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
