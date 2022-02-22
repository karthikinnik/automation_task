import boto3
region = 'us-east-1'
session = boto3.Session(profile_name='ivanti')
ec2 = session.resource('ec2',region_name=region)


instances = ec2.instances.filter(Filters=[{
    'Name': 'tag:Name',
    'Values': ['XXXXXXXXXXXX']}])

print(instances)

'''
x = []
for instance in instances:
    x.append(instance.id)
client= session.client('ec2', region_name=region)
client.start_instances(InstanceIds=x)'''