from google.cloud import storage

bucket = "buclet"
obj = "images.zip"

def downloader():
    storage_client = storage.Client()
    _bucket = storage_client.bucket(bucket)

    blob = _bucket.blob(f'zip/{obj}')
    blob.download_to_filename("images.zip")

    return 0

def unzip():
    import zipfile
    with zipfile.ZipFile("images.zip","r") as zip_ref:
        zip_ref.extractall("./images/")
    import os
    for name in os.listdir("./images/"):
        os.rename(f'./images/{name}',"./images/image.jpg")

def upload():
    storage_client = storage.Client()
    _bucket = storage_client.bucket(bucket)
    _obj = _bucket.blob(obj)
    blob = _bucket.blob("images/image.jpg")

    blob.upload_from_filename("./images/image.jpg")

if __name__ == "__main__":
    downloader()
    unzip()
    upload()
