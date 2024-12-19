from django.db import models

class MetaField:
    def __init__(self, verbose_name, name):
        self.verbose_name = verbose_name
        self.name = name

def get_table_data_by_model(model: models.Model) -> dict:
    fields = [field.verbose_name for field in model._meta.fields]
    items = model.objects.all()
    return {
        "fields": fields,
        "items": items
    }
