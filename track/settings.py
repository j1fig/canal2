import os


PORT=os.getenv('PORT', 8080)
ENV=os.getenv('ENV', 'dev')
STATIC_URL=os.getenv('TRACK_ROOT_URL', f'http://0.0.0.0:{PORT}/static')
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR=os.path.join(ROOT_DIR, 'static')
