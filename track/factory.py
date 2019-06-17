import logging

from aiohttp import web
import aiohttp_jinja2
import jinja2


def make_app():
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    app['websockets'] = {}

    app.on_shutdown.append(cleanup_app)

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('track', 'templates')
    )

    from track.views import index
    app.router.add_get('/', index)

    return app


def cleanup_app(app):
    for ws in app['websockets'].values():
        ws.close()
    app['websockets'].clear()
