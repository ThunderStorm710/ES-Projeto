import boto3


def insertSpecialty(item):
    # Criando o cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Specialty'

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    response = table.put_item(Item=item)
    return response


def getSpecialtiesById(id):
    # Criando o cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Specialty'

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    response = table.get_item(Key=id)
    item = response.get('Item')
    return item


def getAllSpecialties():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Specialty'

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
    insertSpecialty({'id': '1', 'name': 'Cardiologia'})
    specialties = getAllSpecialties()
    print(specialties)
    print(getSpecialtiesById({'id': '1'}))
