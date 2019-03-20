import boto3
# ############Launching EC2###############################
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami25615740',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro'
)
print instance[0].id
######################For terminating the launch instance###########################
instance_id =''#give the instance id generated
instance = ec2.Instance(instance_id)
response = instance.terminate
print response
