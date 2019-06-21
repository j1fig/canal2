#!/usr/bin/env python3
import logging
import os

from aiohttp import web

from track import factory, settings


def listen_and_serve():
    logging.basicConfig(level=logging.DEBUG)

    app = factory.make_app()
    web.run_app(app, port=settings.PORT)


if __name__ == '__main__':
    listen_and_serve()
