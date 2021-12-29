from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/_debugbar/", "WelcomeController@debug"),
]

