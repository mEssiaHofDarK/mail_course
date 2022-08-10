def app(environ, start_response):
    """Simplest possible application object"""
    try:
        query = '\n'.join(environ['QUERY_STRING'].split('&'))
        # data = b'Hello, World!\n'
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(query)))
        ]
        start_response(status, response_headers)
        return iter([bytes(query)])
    except KeyError:
        return 1
