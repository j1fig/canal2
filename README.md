track
=====

`track` tracks all my carbon related activity.

## setup

    pip3 install -r requirements.txt
	alembic upgrade head

## running

    ./run.py

## migrations

    alembic migrate

## vision

Pure self-made, family use software to quantify and gamify my own carbon footprint down.


## roadmap

1. ~~automatic migration system support.~~
    * see [here](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#autogenerating-multiple-metadata-collections) for when there are more models.
    * we can simply get all the subclasses of base and automatically populate the metadata list.
	* works locally, missing command for production.
2. change random naming to name set by user.
    * possibly just OAUTH integration to google.
3. DB I/O support from aiohttp.
4. RESTful endpoint for `waste`, `energy`, `transport`.
