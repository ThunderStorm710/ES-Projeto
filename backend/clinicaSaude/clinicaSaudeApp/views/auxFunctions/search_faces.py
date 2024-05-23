import boto3


def search_faces_by_image(image):
    aws_access_key_id = "ASIA453LFNKUDTJSNG7U"
    aws_secret_access_key = "yvmXImXQZjPOnZTQxHbqJyHhdR7qI7P64t2nLSnv"
    aws_session_token = "IQoJb3JpZ2luX2VjEPL//////////wEaCXVzLXdlc3QtMiJHMEUCIF4ZlTFwCdEQK1iWlEm1tRCydFwlLKraS3A7glNIgb5hAiEA8Lez4q6fVyz2twI0bhx76zSMl9pd0x8owSdI1SbBnccqtAIIaxAAGgw4ODg3NDYxMDk2MDgiDHaMoTz9Vu/JlYfj2SqRAhi/n/+UfBmbtGjSmcHyA/kH0HuYtMfVLUNVkuhwCU/mtKvfCHYnuB9jDpgjLJjrHBymqxUysRQw+h4Xy38phncxj+2OK8YYz9N9EiXpTm0GjGaO0HEFe45n/mlCi9rET0d34BSOTjNkd9ANi4rTD4UMDhiQ0Ij896ewJWw7oFGLZCP9AS+oXMXrLEWGyGr8WxCWGdm/kjH5WyHezZVe/Sy78Tl4UCWfPVxuBexG1d+6a1ElNEFUKkS8U1WmAaJ3J4c+DCx7d7Fu4ZiJchEllz2CyRfuxvRrGsGw6YmJwaiUhcVXMuOfy0TMle/PMbWd5HeJtArgRw7i7SiYSUVEsv4DP9f7HqGox8HTo0ryuRaYbzDlw7qyBjqdAVt6fYDBdOoZDEELBYB2g+gNhGE3xHjyIBhfkGLu5agLvy3KeM2ITIGiOk87fm4zOSWORchbCANau9BXFqcvqvTjjNYi9FQbNGuCANqsaM9ZXK4d8aiVpJTzX1+c1oK3pq2UV+L/6IB17/Ll9XzCh45Rg24ZGM/URMQNpcCFwQqIjwLq+yCU65Z5xlPtZ30a0OU0u8tz1pSzIEBXgZw="

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
