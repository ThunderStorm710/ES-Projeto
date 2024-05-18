import boto3


def insertSpecialty(item):
    if item is None or 'name' not in item:
        return -1, "Name not inserted"

    if item['name'] is None or item['name'] == '':
        return -1, "Invalid name"

    # Criando o cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Substitua pela sua região

    # Nome da tabela
    table_name = 'Specialty'

    # Obtendo a tabela
    table = dynamodb.Table(table_name)

    data = getAllSpecialties()

    for existing_item in data:
        if existing_item['name'] == item['name']:
            return -1, "Specialty already exists"

    max_item = max(data, key=lambda x: int(x["SpecialtyId"])) if data else {"SpecialtyId": "0"}
    id = int(max_item["SpecialtyId"]) + 1

    item["SpecialtyId"] = str(id)

    response = table.put_item(Item=item)
    return id, response


def getSpecialtiesById(id):

    if type(id) != dict:
        id = {'SpecialtyId': id}

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
    insertSpecialty({'name': 'Pulmonar'})
    specialties = getAllSpecialties()
    print(specialties)
    print(getSpecialtiesById({'SpecialtyId': '5'}))
