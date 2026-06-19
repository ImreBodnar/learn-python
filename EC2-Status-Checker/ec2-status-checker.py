import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    instance_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    print(
        f"Instance {status['InstanceId']} is {state} with instance status {instance_status} and system status {system_status}.")
