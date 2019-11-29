from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(object):
    """
    First function of Hello World! in Pyramid.
    :param object:
    :return: Response of Hello WOrld!
    """
    return Response('<body><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
