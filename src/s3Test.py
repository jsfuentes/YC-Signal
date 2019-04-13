import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# s3.create_bucket(Bucket='yc-signal-bucket', CreateBucketConfiguration={
#         'LocationConstraint': 'us-west-1'
#     })

    # Upload a new file
data = open('./Endgame.mp3', 'rb')
s3.Bucket('yc-signal-bucket').put_object(Key='Endgame.mp3', Body=data)
