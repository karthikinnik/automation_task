import boto3

client = session.client('route53')

x = ['karthik-test.trysaasiteu.com','karthik-test1.trysaasiteu.com'] # TRY SAASITEU URL's
i = 0
for item in x:
    response = client.change_resource_record_sets(
        HostedZoneId='Z28MXH3H9TORHE',
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
                                "Value": 'XXXXX'
                            }
                        ]
                    }
                },
                {
                    "Action": "CREATE",
                    "ResourceRecordSet": {
                        "Name": item,
                        "Type": "A",
                        "TTL": 300,
                        "ResourceRecords": [
                            {
                                "Value": 'XXXX'
                            },
                        ],
                    }
                },
            ]
        }
    )
    print(item + ' updated successfully', file=open("output.txt", "a"))
    i += 1
print(i)