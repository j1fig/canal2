#!/usr/bin/env python3
import os

from aiohttp import web

from track import factory


def listen_and_serve():
    app = factory.make_app()
    web.run_app(app, port=os.getenv('PORT', 5000))


if __name__ == '__main__':
    listen_and_serve()
