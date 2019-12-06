import csv
import boto3

with open('../credentials.csv', 'r') as input:
    # Skip the first row
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name='us-west-2')

# If image is local convert into bytes
# with open(photo, 'rb') as source_image:
#   source_bytes = source_image.read()

response = client.detect_faces(Image={'S3Object': {
            'Bucket': 'troekens123',
            'Name': 'facial_Analysis_Happy.jpg'
        }}, Attributes=['ALL'])

for key, value in response.items():
    if key == 'FaceDetails':
        for people_att in value:
            print(people_att)
            print("======")
