from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    EmbeddedDocumentField,
    EmbeddedDocumentListField
)


class ManagementConfigDocument(EmbeddedDocument):

    link_id = StringField(required=True)
    ip_address = StringField(required=True)
    netmask = StringField(required=True)


class InterfaceConfigDocument(EmbeddedDocument):
    link_id = StringField(required=True)
    description = StringField()
    ip_address = StringField(required=True)
    netmask = StringField(required=True)


class BaseConfigDocument(Document):
    node_type = StringField(required=True, default='ios')
    hostname = StringField(required=True)
    management = EmbeddedDocumentField(ManagementConfigDocument, required=True)
    interfaces = EmbeddedDocumentListField(InterfaceConfigDocument)
