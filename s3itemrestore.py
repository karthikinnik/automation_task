import boto3

session = boto3.Session(profile_name= 's3automation')
s3client = session.client('s3')
s3r = session.resource('s3')

bucket = 'XXXXXX'

paginator = s3client.get_paginator('list_object_versions')
pageresponse = paginator.paginate(Bucket=bucket)

count  = 0
for pageobject in pageresponse:
    if 'DeleteMarkers' in pageobject.keys():
        for each_delmarker in pageobject['DeleteMarkers']:
            fileobjver = s3r.ObjectVersion(
                bucket,
                each_delmarker['Key'],
                each_delmarker['VersionId']
            )
            print('Restoring ' + each_delmarker['Key'])
            fileobjver.delete()
            count +=1
            print(count)
print(count)