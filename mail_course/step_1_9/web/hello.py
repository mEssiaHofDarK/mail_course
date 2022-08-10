def app(environ, start_response):
    """Simplest possible application object"""
    try:
        query = '\n'.join(environ['QUERY_STRING'].split('&'))
        # data = b'Hello, World!\n'
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain')
        ]
        start_response(status, response_headers)
        return iter(query)
    except KeyError:
        return 1
