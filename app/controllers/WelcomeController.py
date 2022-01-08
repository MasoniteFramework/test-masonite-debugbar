"""A WelcomeController Module."""
from platform import python_version
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
        print(User.all())
        print(User.all())
        print(User.select('name,email').get())
        print(User.select('name,email').get())


        debugger.get_collector('messages').add_message("Success")
        debugger.get_collector('messages').add_message("Failure")
        debugger.get_collector('Environment').add("Python Version", python_version())
        return view.render("welcome")

    def debug(self, response: Response):
        requests = []
        files = application.make('storage').disk('debug').get_files()
        for file in files:
            requests.append({ 
                "request_id": json.loads(file.content)['__meta']['request_id'],
                "request_url": json.loads(file.content)['__meta']['request_url']
            })

        return response.json({"data": json.loads(files[0].content)["data"], "collectors": list(json.loads(files[0].content)["data"].keys()), "requests": requests})

    def get_debug(self, response: Response, request: Request):
        requests = []
        files = application.make('storage').disk('debug').get_files()
        for file in files:
            requests.append({ 
                "request_id": json.loads(file.content)['__meta']['request_id'],
                "request_url": json.loads(file.content)['__meta']['request_url']
            })

        file = application.make('storage').disk('debug').get(f"{request.param('id')}.json")

        return response.json({"data": json.loads(file)["data"], "collectors": list(json.loads(file)["data"].keys()), "requests": requests})

    def api(self, response: Response, request: Request):
        users = User.select('name,email').get()

        return users