from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage


class CustomUploadStorages(S3Boto3Storage):
    """This sends uploaded files to a folder in our AWS Storage. You can do similar for Static Files
    If you don't like the fact that it's all over the bucket.
    """
    location = settings.CUSTOM_S3_UPLOAD_FOLDER
