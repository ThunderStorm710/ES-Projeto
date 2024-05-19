from django.db import models


def fk(model):
    return models.ForeignKey(model, on_delete=models.CASCADE)


from .appointment import *
from .user import *
from .payment import *
from .doctor import *
from .specialty import *
from .slot import *
from .posts import *

