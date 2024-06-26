import boto3
import json


def state_machine(input_data):
    if "appointment_id" not in input_data or "payment_id" not in input_data:
        return False
    # Crie um cliente para o Step Functions
    client = boto3.client('stepfunctions')

    # Defina o ARN da sua State Machine
    state_machine_arn = 'arn:aws:states:us-east-1:888746109608:stateMachine:Workflow-Pagamento'

    try:
        # Inicie a execução da State Machine
        response = client.start_execution(
            stateMachineArn=state_machine_arn,
            input=json.dumps(input_data)
        )

        # Exiba o ID da execução
        print('Execution ARN:', response['executionArn'])
        print('Start Date:', response['startDate'])

        return True

    except Exception as e:
        print('Error starting execution:', e)


if __name__ == '__main__':
    state_machine({"appointment_id": 5, "payment_id": 3})
