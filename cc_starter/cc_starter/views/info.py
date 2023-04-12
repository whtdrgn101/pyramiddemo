from pyramid.view import view_config


@view_config(route_name='info', renderer='cc_starter:templates/info.jinja2')
def my_view(request):
    return {'project': 'cc_starter'}
