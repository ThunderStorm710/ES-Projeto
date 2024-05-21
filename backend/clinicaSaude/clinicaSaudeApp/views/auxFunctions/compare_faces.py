import boto3


def compare_faces(sourceFile):
    flag = False
    aws_access_key_id = "ASIA453LFNKUHYYCCUVK"
    aws_secret_access_key = "eCDvqHHmylCzfjF4NG/BdV+Nf8C7r74bA4Kc5Y6m"
    aws_session_token = "IQoJb3JpZ2luX2VjEL7//////////wEaCXVzLXdlc3QtMiJIMEYCIQDFMeiQRWEg7YIcVlj013NIS2EaR46eZmh27UtKrpC/vgIhANeQ8UdwBjtOf3HOCI5xnQTcfaD2f3ZSmOiM+o+pa2G2KrQCCDcQABoMODg4NzQ2MTA5NjA4IgwrkNnqZKdOZ2AhuBsqkQJv5Xq+PHU1MZysIHXv4MVLofh4b2r5bX2TdFFGTK888+7Bx0JK0aXN+xImTFsxS8Ug6yJfYCw5UakXVqDbQlGiGoPlAktV64z7UaT+GTqokAIXpQykd+KM+u4d/AEQ+AZfwRnu3uYoNEdTDyuiIWgcqXF/KDzEj6vSLQMJ9Yh4db2SG+Mq7vWqy7FnEv/cj5y1bzBuFh3q36512nj7C8RtzVyOsKDRpSz1WgbeA9+uPc3XpTxJ/s+5O04O+8xLbcl+j7nWvy5sSsB7MwIsZLf0jIX4vJiyTJ8zRmHtUX1ns+yAUSGl4si06jqEIQOM8rfuXGIx2bB1iy8pys5c0aVHh/IvtP+wtnEQ1GQa352VAogws46vsgY6nAHjGC+j8bP+J2hXBZ4sSreo0+9xCZkY50Z7QQe7h11xHzb32QKxr7P3bu8/ObCc6KOrwoRTZ47b0T8lkp+SSDpE8hu7GM8lrNcNaHc1nWTgcX19qHnzfiPAg1BIE8F1nKHV2obYTEpmeRoQka8H2+zPMAJL1Xb/gEVCraAPbwvHqBI4n2BQRWRbykvqNPSWNrZcu3CRB7S77bXvocM="

    s3 = boto3.resource('s3', region_name='us-east-1',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        aws_session_token=aws_session_token)

    client = boto3.client('rekognition', region_name='us-east-1',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          aws_session_token=aws_session_token)

    imageSource = open("C://Users/pasce/OneDrive/Ambiente de Trabalho/ES-Projeto/backend/clinicaSaude/media/10.jpeg", 'rb')

    my_bucket = s3.Bucket('clinic-clients-images')

    imagem = imageSource.read()
    ''''''
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
