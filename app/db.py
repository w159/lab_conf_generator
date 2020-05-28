from datetime import datetime

from mongoengine import (
    Document,
    StringField,
    DateField
)


class ConfigRecord(Document):
    date = DateField(default=datetime.now())
    data = StringField()
    dev_name = StringField()
    node_eve_id = StringField()
    node_type = StringField()
    lab_name = StringField()


def is_config_present(dev_name, lab_name) -> bool:
    """
    Validates if the node and lab is present in Database, returns True if present else false.

    """
    docs = ConfigRecord.objects(dev_name=dev_name, lab_name=lab_name)
    if len(list(docs)) >= 1:
        return True

    return False
