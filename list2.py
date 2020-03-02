import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('smashi-proudction')

for object_summary in my_bucket.objects.filter(Prefix="20200120_MorningLive/"):
    print(object_summary.key)
    x = object_summary.key
    y = x.split(".m3u8")
    print(y[0])
    print(type(y))
    z = y[0]+".ts"
    print("##############New Name################")
    print(z)
    print("################Source ##############")
    b = "smashi-proudction/"+x
    print("########################################")
    print(b)
    s3 = boto3.resource('s3')
    s3.Object('smashi-proudction',z).copy_from(CopySource=b)
    s3.Object('smashi-proudction',x).delete()
    print("Video deleted")
