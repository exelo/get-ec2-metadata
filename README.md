# get-ec2-metadata
The python script is intended to query the metadata of an instances in AWS. 

## Setup requirements
* When running the script outside of AWS
  * You will need to load credentials access key ID and secret access key or Assume a IAM Roles that access correct ec2 policy attached to describe your instances.
* When Running script inside of AWS on an EC2
  * You will need to make sure the IAM Role has the correct ec2 policy attached to describe your instances.

## How to Run
An Instances ID is the only required input to the script. Details are listed below.
* A specific region can be provided. Default region is `us-east-1`
* The script prints to stdout by default. You have the option to output to a file (json format).
* If No specific data key is provided. The script will get all metadata of the instances. 
* If a key provided is not found it will just print: `"Data for Key:<KeyProvided> Not Found"`


### Help:
```
╰─> python3 ./ec2-metadata.py -h
usage: ec2-metadata.py [-h] -i INSTANCE_ID [-k KEY] [-o OUTFILE] [-r REGION]

options:
  -h, --help            show this help message and exit
  -i, --instance_id INSTANCE_ID
  -k, --key KEY
  -o, --outfile OUTFILE
  -r, --region REGION
```

### Get entire metadata of an instance in aws and output to file
```
python3 ./ec2-metadata.py -i i-xyzbe25xyz123 -o metadata.json 
metadata.json was generated
```

### Get metadata for a speicifc data key of an instance in aws   
```
python3 ./ec2-metadata.py -i i-xyzbe25xyz123 -k PublicIpAddress
"12.218.230.151"
```


### Get metadata of an instance in aws and output to stdout
`The data has be replaced with "..." to avoid displaying my metadata to the world`
```
╰─ python3 ./ec2-metadata.py -i i-xyzbe25xyz123                  
{
  "Architecture": "...",
  "BlockDeviceMappings": [...],
  "ClientToken": "****",
  "EbsOptimized": false,
  "EnaSupport": true,
  "Hypervisor": "...",
  "IamInstanceProfile": {...},
  "NetworkInterfaces": [...],
  "RootDeviceName": "...",
  "RootDeviceType": "...",
  "SecurityGroups": [...],
  "SourceDestCheck": true,
  "VirtualizationType": "...",
  "CpuOptions": {...},
  "CapacityReservationSpecification": {...},
  "HibernationOptions": {...},
  "MetadataOptions": {...},
  "EnclaveOptions": {...},
  "BootMode": "...",
  "PlatformDetails": "...",
  "UsageOperation": "...",
  "UsageOperationUpdateTime": "...",
  "PrivateDnsNameOptions": {...},
  "MaintenanceOptions": {...},
  "CurrentInstanceBootMode": "...",
  "NetworkPerformanceOptions": {...},
  "Operator": {...},
  "InstanceId": "...",
  "ImageId": "...",
  "State": {...},
  "PrivateDnsName": "...",
  "PublicDnsName": "...",
  "StateTransitionReason": "",
  "KeyName": "...",
  "AmiLaunchIndex": 0,
  "ProductCodes": [],
  "InstanceType": "...",
  "LaunchTime": "...",
  "Placement": {...},
  "Monitoring": {...},
  "SubnetId": ""...",
  "VpcId": "...",
  "PrivateIpAddress": "..."
  "PublicIpAddress": "..."
}
```

### Get metadata for a speicifc data key of an instance in aws that is NOT FOUND
```
╰─ python3 ./ec2-metadata.py -i i-xyzbe25xyz123 -k KeyDoesntExisit
"Data for Key:KeyDoesntExisit Not Found"
```