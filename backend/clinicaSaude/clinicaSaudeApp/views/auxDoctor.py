import boto3
import auxSpecialty


def insertDoctor(item):
    if item is None or 'name' not in item or 'email' not in item or 'specialty_id' not in item or 'room' not in item:
        return -1, "Missing field"

    if any(value is None or value == '' for value in item.values()):
        return -1, "Invalid field value"

    # Criando o cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Nome da tabela
    table_name = 'Doctors'

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    data = auxSpecialty.getAllDoctors()

    for existing_item in data:
        if existing_item['email'] == item['email']:
            return -1, "Doctor with this email already exists"

    # Nome da tabela
    table_name_specialties = 'Specialties'

    # Obtendo a tabela
    table_specialties = dynamodb.Table(table_name_specialties)

    if getSpecialtiesById(item['specialty_id']) is None:
        return -1, "Specialty not found"

    max_item = max(data, key=lambda x: int(x["DoctorId"])) if data else {"DoctorId": "0"}
    id = int(max_item["DoctorId"]) + 1

    item["DoctorId"] = str(id)

    response = table.put_item(Item=item)
    return id, response


def getDoctorsById(id):
    # Criando o cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Doctors'  # Mudança para a tabela Doctors

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    response = table.get_item(Key={'DoctorId': id})  # Ajuste na chave
    item = response.get('Item')
    return item


def getAllDoctors():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Doctors'  # Mudança para a tabela Doctors

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    response = table.scan()
    data = response['Items']

    # Continuar escaneando enquanto LastEvaluatedKey estiver presente na resposta
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data


if __name__ == '__main__':
    '''print(insertDoctor({
        "name": "Pedro",
        "specialty": "1",
        "email": "pedro@dei.pt",
        "room": "A"
    }))'''
    print(getAllDoctors())
    print(getDoctorsById("1"))
