#!/usr/bin/env python3
from aiohttp import web

from track import factory


def listen_and_serve():
    app = factory.make_app()
    web.run_app(app)


if __name__ == '__main__':
    listen_and_serve()
