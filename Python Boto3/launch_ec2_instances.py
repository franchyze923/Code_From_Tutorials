import boto3

ec2 = boto3.resource('ec2')

# instance = ec2.create_instances(
#     ImageId='ami-0885b1f6bd170450c',
#     MinCount=1,
#     MaxCount=2,
#     InstanceType='t2.micro',
# )
# print(instance)

#ec2.instances.filter(InstanceIds=["i-0b92235b01c30cafd", "i-0d6cedd2bb5544c46"]).terminate()

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type)