import argparse
import boto3
import json 

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--instance_id", required=True)
parser.add_argument("-k", "--key",)
parser.add_argument("-o", "--outfile")
parser.add_argument("-r", "--region", default="us-east-1")

args = parser.parse_args()
instance_id = args.instance_id
key = args.key
outfile = args.outfile
region = args.region

try:
    ec2 = boto3.client('ec2',region_name=region)
    response = ec2.describe_instances(InstanceIds=[instance_id])
    reservations = response.get('Reservations')[0]
    instance = reservations.get('Instances')[0]
    
    # if a data key is provided set 'data' just to the data for the key
    if key:
        data = instance.get(key,f"Data for Key:{key} Not Found")
    else:
        data = instance

    # if outfile is provided we send the json output to {outfile} else stdout 
    if outfile:
        with open(outfile, "w") as f:
            json.dump(data, f, default=str, indent=4)
        
        print(f"{outfile} was generated")
    else:
        json_string = json.dumps(data, default=str, indent=2)
        print(json_string)

except Exception as e:
    print("Exception: ",e)