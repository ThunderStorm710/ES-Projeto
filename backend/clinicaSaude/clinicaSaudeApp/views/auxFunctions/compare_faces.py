import boto3


def compare_faces(path):
    flag = False
    aws_access_key_id = "ASIA453LFNKUOFWMIAUT"
    aws_secret_access_key = "gYPxZggexiInjADzUaqVl79EuwNCsMjENUWS/oiv"
    aws_session_token = "IQoJb3JpZ2luX2VjEPv//////////wEaCXVzLXdlc3QtMiJGMEQCICOt3HmfompnPtsM0CLlxOZqrWpUAcKKqIigfXVYk3vPAiAkWLpN3GQ9mtYPQsOJIi69d5jopfQQA0vHvL/RfZoPzyq0Agh0EAAaDDg4ODc0NjEwOTYwOCIMBjmkTz6NugYgZMcTKpECOS8jL2fwGM4YWUr8xrtMEB+X5eB29i9stETUiQ3Equp/d4Ha+43/R2L2lLaQhgxBwkeLCnFonFRJ+SAb5+46wOmKZBz4qEJOOqdewokNo7nDE19YRn5WCPYjon/QMAuKJaa6skTIEI8ezWTAcWibs5y1AOmdA88Z0L4zUMIT79pnQTLQnWKcaL+zd3TL78JSX+3HBqYhGE+oVF3Kg5hkbv8DezXlitBqgBotjyh0xTr72Mc+o5wEylTlZM8xhw6tUZJnO4PdInx1w6WSV3k3gT27/q0g+A3t7Gz2rRQuj/ZJTeDU9Rka/v5onnY3iW3p5+HuTz12p7n1keYHxVObMfHhhw6n/Rv8UZz4zW0uExSZMLXIvLIGOp4BKu+1jcCBirp77hRirB3/f7N1zyy4PdaxB5JQ1zFdb+5grgVnZNNndRL/FuizvAWo3y78xklhK7t4AdNm09J25n2gKOcGL3RpmbwX/fMz53W4k03RYEI9R6hqcaDvmVYvjjOs6Ge4KFErPDtCACBxSq5MAwh7lKtjEHKH2YyLWEcrmqeaRpDwFq+eK398KxfOPX5nFcIvj5/K5ZB8W/A="

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
