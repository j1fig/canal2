from aiohttp import web
import aiohttp_jinja2
import jinja2

from track.views import index, ws


async def make_app():
    app = web.Application()
    app['websockets'] = {}

    app.on_shutdown.append(cleanup)

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('track', 'templates')
    )

    # app.add_routes([web.get('/', index)])
    app.router.add_get('/', index)
    app.router.add_get('/ws', ws)

    return app


async def cleanup(app):
    for ws in app['websockets'].values():
        ws.close()
    app['websockets'].clear()
