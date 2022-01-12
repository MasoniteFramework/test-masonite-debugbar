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


        debugger.get_collector('Messages').add_message("Success")
        debugger.get_collector('Messages').add_message("Failure")
        return view.render("welcome")

    def debug(self, response: Response):
        requests = []
        files = application.make('storage').disk('debug').get_files()
        files = sorted(files, key=lambda x: x.name())
        for file in files:
            requests.append({
                "request_id": json.loads(file.content)['__meta']['request_id'],
                "request_url": json.loads(file.content)['__meta']['request_url']
            })

        return response.json({"data": json.loads(files[0].content)["data"], "collectors": list(json.loads(files[0].content)["data"].keys()), "requests": requests})

    def get_debug(self, response: Response, request: Request):
        requests = []
        files = application.make('storage').disk('debug').get_files()
        files = sorted(files, key=lambda x: x.name())

        for file in files:
            requests.append({
                "request_id": json.loads(file.content)['__meta']['request_id'],
                "request_url": json.loads(file.content)['__meta']['request_url']
            })

        file = application.make('storage').disk('debug').get(f"{request.param('id')}.json")

        return response.json({"data": json.loads(file)["data"], "collectors": list(json.loads(file)["data"].keys()), "requests": requests})

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