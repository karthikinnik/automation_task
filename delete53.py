import boto3
from pandas import *

#session = boto3.Session(profile_name='XXXX')
#client = session.client('route53')

data = read_csv("saasit.csv")
x = data['name'].tolist()

for item in x:
    response = client.change_resource_record_sets(
        HostedZoneId='Z2CVUUV7IO1Y2W',
        ChangeBatch={
            "Comment": "Automatic DNS update",
            "Changes": [
                {
                    "Action": "DELETE",
                    "ResourceRecordSet": {
                        "Name": item,
                        "Type": "CNAME",
                        "TTL": 300,
                        "ResourceRecords": [
                            {
                                "Value": 'XXXXXX'
                            },
                        ],
                    }
                },
            ]
        }
    )