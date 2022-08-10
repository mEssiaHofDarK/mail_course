def app(environ, start_response):
    """Simplest possible application object"""
    try:
        query = (environ.get('QUERY_STRING')).replace('&', '\n')
        # data = b'Hello, World!\n'
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(query)))
        ]
        start_response(status, response_headers)
        return query
    except KeyError:
        return 1
