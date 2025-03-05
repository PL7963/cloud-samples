## Tags: Cloud Build, Buildpacks, Cloud Run Job, Workflow, Eventarc, Cloud Storage

### Process the files automatically when file uploaded to Cloud Storage
In this task you have to build a image with Cloud Build and Buildpacks and deploy to Cloud Run. And configure eventarc to trigger workflow when titanic.csv uploaded to your bucket. The workflow will trigger Cloud Run ,process the file and upload the result back to your bucket.

You can get titanic.csv at [kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset)