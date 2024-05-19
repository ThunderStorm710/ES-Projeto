import boto3


def compare_faces(sourceFile):

    aws_access_key_id = "ASIA453LFNKUJHSI3QVT"
    aws_secret_access_key = "hV/+ANOyshXkyuIOY20d3kRYcRKZcXxbPoiL+ih2"
    aws_session_token = "IQoJb3JpZ2luX2VjEJH//////////wEaCXVzLXdlc3QtMiJHMEUCIHoiMkvgt8YTOaSXW+lq5fB/6KYKU+1XUOU5lyywGyVSAiEAwjhh2/fObqQWXep5nK3VKXgtvx3QguRcc8UDtRnNwQ0qvQII+v//////////ARAAGgw4ODg3NDYxMDk2MDgiDKgZTII1d0kOm0OozSqRAnP03iXHqAEzfhiVRjRd3OePLWh8v+yZwUzwNpymE1xAjwMBlV9LwqfJq+OCBF6v52v5iEyOKSQTRMzm1/YGdgUOoaXdHbbR69jvTeGW5VhRexz23sZtDZXsq5yyKCT1YNNVeloE/VDwfgL9vnLXvJPRw9NU8r1acF/rP29Z9IFS1vK0ElcT6K77Dx2S0JUX1bq2UltHILoBQ/WyjZ7PTD3Hk9EUd/uU3xaK7Z5Z4Iq5YXjImCZe5fvLz45ckV5lfeA/CFDA2WyxrxQmYsqFFz5YXy45bwlxnCia/Pu5iDomx3BtvOwmq93jJXSfu/C29Jol3d/EmwqGYB+zWBDz0GDnBX9mun7BtPPMOCil8mS/pDCrl6WyBjqdAfuvGVl7B9rm4Nzgmyff8XqDAN/zokPqQxv41OuzTPDUtBzq4SDL447Dy+LTsS6iEXac7xqkDzvxZxdbHj1drM3jrnz4BoDMAj9CouFRObYA3r3wYOtHL3WTHcIFj2+I9F9DRaelZtvlrGrcjE6TE/xreNelWxz/edVHQyS6zuU7kbSwXOImDylrsOdQtoPV1/nbL4y9neV4cW+5jAg="

    s3 = boto3.resource('s3', region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

    client = boto3.client('rekognition', region_name='us-east-1',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          aws_session_token=aws_session_token)

    imageSource = open("C://Users/USER1/Desktop/ES-Projeto/backend/clinicaSaude/media/10.jpeg", 'rb')

    my_bucket = s3.Bucket('clinic-clients-images')

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
        response = client.compare_faces(SimilarityThreshold=80,
                                        SourceImage={'Bytes': imageSource.read()},
                                        TargetImage={
                                                    'S3Object': {
                                                        'Bucket': 'clinic-clients-images',
                                                        'Name': f'{my_bucket_object.key}'
                                                    }
                                        })
        print(response)
        for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            similarity = str(faceMatch['Similarity'])
            print('The face at ' +
                  str(position['Left']) + ' ' +
                  str(position['Top']) +
                  ' matches with ' + similarity + '% confidence')

            print(len(response['FaceMatches']))
    imageSource.close()

    return len(response['FaceMatches'])
