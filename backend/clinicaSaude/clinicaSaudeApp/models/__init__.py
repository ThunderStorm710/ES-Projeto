from django.db import models


# Has to be defined before the other imports to avoid issues
def fk(model):
    return models.ForeignKey(model, on_delete=models.CASCADE)


from .appointment import *
from .user import *
from .payment import *
from .doctor import *
