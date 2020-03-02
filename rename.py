import boto3


s3 = boto3.resource('s3')
s3.Object('smashistaging','fbtest2/MoneyandBusiness_20200227.mp4').copy_from(CopySource='smashistaging/fbtest2/MoneyandBusiness_20200227.m3u8')
s3.Object('smashistaging','fbtest2/MoneyandBusiness_20200227.m3u8').delete()


