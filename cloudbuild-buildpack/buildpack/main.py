from google.cloud import storage
import csv

def download_blob(bucket_name, source_blob_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename("input.csv")

def process_file():
    survivors = {}
    output = open('output.csv', 'w')

    with open('input.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Survived'] == '1':
                survivors[row['Pclass']] = survivors.get(row['Pclass'], 0) + 1
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Ticket class', 'Survived'])
        for pclass, count in survivors.items():
            writer.writerow([pclass, count])

def upload_blob(bucket_name, source_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)
    blob.upload_from_filename(source_file_name)

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    source_blob_name = 'titanic.csv'

    download_blob(bucket_name, source_blob_name)
    process_file()
    upload_blob(bucket_name, 'output.csv')
    