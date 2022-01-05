"""A WelcomeController Module."""
from platform import python_version
from masonite.views import View
from masonite.response import Response
from masonite.controllers import Controller 

from app.models.User import User
from wsgi import application
import time


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def debug(self, response: Response):
        debugger = application.make('debugger')
        debugger.get_collector("Time").start_measure('user_queries')
        print(User.all())
        print(User.all())
        print(User.select('name,email').get())
        print(User.select('name,email').get())
        debugger.get_collector("Time").stop_measure('user_queries')


        debugger.get_collector('messages').add_message("Success")
        debugger.get_collector('messages').add_message("Failure")
        debugger.get_collector('Environment').add("Python Version", python_version())
        return response.json({"data": debugger.to_dict(), "collectors": list(debugger.collectors.keys())})