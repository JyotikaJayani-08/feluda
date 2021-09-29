from flask import request
import json


class HealthRequestModel:
    pass


class HealthRoute:
    def __init__(self):
        pass

    def handle_health(self):
        print("---", request.path)
        return "OK"

    def handle_post_health(self):
        # data = request.get_json(force=True)
        print("---")
        print(request.get_json())
        print(type(request.files["media"]))
        print(json.load(request.files["data"]))
        print("---")
        return {"message": "OK2"}

    def make_handlers(self):
        print(request.path)
        if request.path == "/health":
            return self.handle_health()
        elif request.path == "/post_health":
            return self.handle_post_health()
        else:
            raise "Unsupported Health API endpoint"


class HealthController:
    def __init__(self):
        pass

    def get_routes(self):
        return [
            ("/health", "health", ["GET"]),
            ("/post_health", "post_health", ["POST"]),
        ]

    def get_handler(self):
        route = HealthRoute()
        return route.make_handlers()
