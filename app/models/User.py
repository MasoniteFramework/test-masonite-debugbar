"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masoniteorm.relationships import belongs_to



class User(Model, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
    __timestamps__ = False

    @belongs_to("id", "member_id")
    def profile(self):
        from .Profile import Profile
        return Profile