"""A WelcomeController Module."""
from masonite.views import View
from masonite.response import Response
from masonite.request import Request
from masonite.controllers import Controller
import json

from app.models.User import User
from wsgi import application
import time


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        debugger = application.make('debugger')
        users = User.with_('profile').select('id').get()


        debugger.get_collector('Messages').add_message("Success", tags={"color": "green", "message": "tag name"})
        debugger.get_collector('Messages').add_message("Failure", tags={"color": "red", "message": "tag name"})
        return view.render("welcome")

    def api(self, response: Response, request: Request):
        users = User.select('password').get()

        return users

    def settings(self, response: Response, request: Request):
        users = User.select('id').get()
        debugger = application.make('debugger')
        debugger.get_collector('Messages').add_message("Success from settings")

        return users

    def profile(self, response: Response, request: Request):
        users = User.select('email').get()

        return users