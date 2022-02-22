import boto3
import pandas as pd
import os

session = boto3.Session(profile_name= 'XXXX')
r53 = session.client('route53')
s3 = session.resource('s3')

response = r53.list_hosted_zones()

y = []
for item in response['HostedZones']:
    y.append(item['Id'])
zone_ids = []
for item in y:
    a = item[12:]
    zone_ids.append(a)
    print(a)
y = []
for item in response['HostedZones']:
    y.append(item['Name'])
Names = []
for item in y:
    a = item[:-1]
    Names.append(a)

def r53_bak(zone_id_fun_par):
    paginator = r53.get_paginator('list_resource_record_sets')
    try:
        x=[]
        source_zone_records = paginator.paginate(HostedZoneId=zone_id_fun_par)
        for record_set in source_zone_records:
            for record in record_set['ResourceRecordSets']:
                if record['Type'] == 'CNAME':
                    x.append(record)
                if record['Type'] == 'A':
                    x.append(record)
        Name_1 = []
        Type = []
        TTL = []
        Value = []
        for item in x:
            Name_1.append(item['Name'])
            Type.append(item['Type'])
            TTL.append(item['TTL'])
            Value.append(item['ResourceRecords'][0]['Value'])
        Name = []
        for item in Name_1:
            a = item[:-1]
            Name.append(a)
        d = {'Name': Name, 'Type': Type, "TTL": TTL, 'Value': Value}
        df = pd.DataFrame(d)
        file_name = zone_id_fun_par + ".csv"
        df.to_csv(file_name)

    except Exception as error:
        print('An error occurred getting source zone records:')
        print(str(error))
        raise

for zone_id in zone_ids:
    r53_bak(zone_id)


for zone_id in zone_ids:
    file_name_for_s3 = zone_id + ".csv"
    #s3.meta.client.upload_file(file_name_for_s3, 'karthik-poc', file_name_for_s3)
    #os.remove(file_name_for_s3)

