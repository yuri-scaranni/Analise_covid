import aws_functions as af
import os
from datetime import datetime

bucket_name = os.getenv('BUCKETNAME', 'analisecovid')


def get_latest_file(bucket_name):
    default_string_name = "owid_covid19_"
    default_string_ext = ".csv"
    objects = af.list_objects_in_bucket(bucket_name, prefix='owid', folders_=False)

    latest = None
    latest_name = None
    for obj in objects:
        file = (os.path.split(obj)[-1])
        timestamp = file.replace(default_string_name, "").replace(default_string_ext, "")
        timestamp_datetime = datetime.strptime(timestamp, "%Y%m%d_%H%M%S")

        if latest is None:
            latest = timestamp_datetime
            latest_name = obj
        if timestamp_datetime > latest:
            latest = timestamp_datetime
            latest_name = obj

    return latest_name