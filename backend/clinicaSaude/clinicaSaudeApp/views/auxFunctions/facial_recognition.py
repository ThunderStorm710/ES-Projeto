import boto3

# Inicialize o cliente Rekognition
rekognition_client = boto3.client('rekognition')
# Carregue a imagem
with open('imagem.jpg', 'rb') as image_file:
    image_bytes = image_file.read()

# Detecte rostos na imagem
response = rekognition_client.detect_faces(
    Image={'Bytes': image_bytes},
    Attributes=['ALL']  # Pode especificar os atributos que deseja retornar
)

# Exiba os resultados
for face_detail in response['FaceDetails']:
    print('Confiança: ', face_detail['Confidence'])
    print('Idade: ', face_detail['AgeRange'])
    print('Gênero: ', face_detail['Gender']['Value'])
    print('Emoções: ', face_detail['Emotions'])
    # Etc.
