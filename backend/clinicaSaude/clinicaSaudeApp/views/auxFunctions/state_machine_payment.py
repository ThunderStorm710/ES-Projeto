import boto3
import json

# Criar o cliente do Step Functions
client = boto3.client('stepfunctions')

# Definir o ARN da state machine
state_machine_arn = 'arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine'

# Definir a entrada JSON (payload) para a state machine
input_payload = {
    'order_id': '12345',
    'other_data': 'example'
}

# Iniciar a execução da state machine
response = client.start_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps(input_payload)
)

# Imprimir a resposta
print(response)
