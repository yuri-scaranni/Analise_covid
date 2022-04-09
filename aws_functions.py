import boto3


s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')


def list_buckets():
    return s3_client.list_buckets()['Buckets']


def list_objects_in_bucket(bucket_name, prefix=None, objects_=True, folders_=True):
    objects = []
    Bucket = s3_resource.Bucket(bucket_name)
    for key_summary in Bucket.objects.all():
        if prefix is None:
            if objects_ is True and folders_ is True:
                pass
            elif objects_ is True and folders_ is False:
                if str(key_summary.key).endswith('/'):
                    continue
            elif objects_ is False and folders_ is True:
                if str(key_summary.key)[-1] != '/':
                    continue
            elif objects_ is False and folders_ is False:
                continue

            objects.append('s3://' + key_summary.bucket_name + '/' + key_summary.key)
        else:
            if str(key_summary.key).startswith(prefix):
                if objects_ is True and folders_ is True:
                    pass
                elif objects_ is True and folders_ is False:
                    if str(key_summary.key).endswith('/'):
                        continue
                elif objects_ is False and folders_ is True:
                    if str(key_summary.key)[-1] != '/':
                        continue
                elif objects_ is False and folders_ is False:
                    continue

                objects.append('s3://' + key_summary.bucket_name + '/' + key_summary.key)
    return objects
