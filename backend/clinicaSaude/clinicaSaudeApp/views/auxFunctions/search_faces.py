import boto3

aws_access_key_id="ASIA453LFNKUFXDAH22H"
aws_secret_access_key="BvPjCEUA+OmZNgwNBFbC6wnFTCrFTUqI3Isvk6pV"
aws_session_token="IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIFT5IogVAIwxAZY4wIPAlPAdIAXhSXyAnavB6X+wFoacAiEAqIDIfS6wi2RNImkU3URowtBPJuKAL0M/38OOGfRARtYqvQIIr///////////ARAAGgw4ODg3NDYxMDk2MDgiDKxKUpvuTdCgWKMbqyqRAoe0WXOF/Iq6OfV/wpSa4aTj8fwMGyedN8k+fD8Ntbh5yddu7ZdlrxvBkoiJH9e/eW68/e6j01ISCNdW4TzQEVUn/RFEw6Utv3ubDD3eHWmU3jgVo9yk5u8Ji4cIMIruLb0bFXZjQdJBx/NGccqxP0RkFbQZPNHByjAg6Dqj+mVMd2ApbADck92b0r8ArFSAX/Yo7OKllXDzGGaZGOPYD69xhAt1iGUgYppZDaawBK5u9DkLLlpdCmgwdnPzuwSElfsoimULIJPmbeVAEBZMSKYJsJCeCbGWtDb6mzt73jDIy0hyR0W8WW9wKIZeip2kar6Ty6iI2/PnQQ/xb8QL1wcU8hoG+1wL/3T4VXXBtDLlGTDO0pSyBjqdAWJCke41VikC08aFWh+CwgjWshHsGz95VkOyquGBq53KlgYzLaZ4Qh9Xmrdwe02hj6IYutodtKdKQcB570d2BgUd/VhJJsTX24mqcsZvN9KccdqZx/0OUr+UOXnh25PfY2feLeQsmCWtJTbJg9O+v7MmvFXSdzJ2jmUAwXhgK7iupLrgRLwnzTvvfksI4a5K5foNVkEBLXXWSsNX7g8="

s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                    aws_session_token=aws_session_token)

client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                      aws_session_token=aws_session_token)

my_bucket = s3.Bucket('clinic-clients-images')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)


response = client.search_faces_by_image(
    CollectionId='clinicasaudecollection',
    Image={
        'S3Object': {
            'Bucket': 'clinic-clients-images',
             'Name': 'todetect/1.jpg'
        }
    },
    MaxFaces=123,
    )

print(response)