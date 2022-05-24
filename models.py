from tortoise import fields
from tortoise.models import Model


class Register(Model):
    id = fields.UUIDField(pk=True)
    names = fields.CharField(max_length=300)
    password = fields.CharField(max_length=80)

