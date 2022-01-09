from masoniteorm.models import Model



class Profile(Model):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
    __timestamps__ = False