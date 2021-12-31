"""A WelcomeController Module."""
from platform import python_version
from masonite.views import View
from masonite.response import Response
from masonite.controllers import Controller 

from app.models.User import User
from wsgi import application


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def debug(self, response: Response):
        print(User.all())
        print(User.all())
        print(User.select('name,email').get())
        debugger = application.make('debugger')


        debugger.get_collector('messages').add_message("Success")
        debugger.get_collector('messages').add_message("Failure")
        debugger.get_collector('python').add_message(python_version(), "Python Version")
        return response.json({"data": debugger.to_dict(), "collectors": list(debugger.collectors.keys())})