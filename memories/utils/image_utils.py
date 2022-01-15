from datetime import datetime


def get_upload_path(instance, filename):
    date = datetime.date(datetime.now())
    image_type = instance._meta.model_name
    return f'{date}/{image_type}/{filename}'


