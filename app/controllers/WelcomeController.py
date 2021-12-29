"""A WelcomeController Module."""
from masonite.views import View
from masonite.response import Response
from masonite.controllers import Controller

from debugbar.debugger import Debugger
from debugbar.collectors.MessageCollector import MessageCollector
from debugbar.collectors.PythonCollector import PythonCollector


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def debug(self, response: Response):
        debugger = Debugger()
        debugger.add_collector(MessageCollector())
        debugger.add_collector(PythonCollector())

        debugger.get_collector('messages').add_message("Success")
        debugger.get_collector('messages').add_message("Failure")
        return response.json({"data": debugger.to_dict(), "collectors": list(debugger.collectors.keys())})