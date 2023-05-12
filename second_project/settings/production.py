from second_project.settings.base import *

ALLOWED_HOSTS.append(config("ALLOWED_HOSTS"))
SECRET_KEY = config("SECRET_KEY")

CUSTOM_S3_UPLOAD_FOLDER = "media_uploads"

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", default=None)
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "custom_storages.CustomUploadStorages"