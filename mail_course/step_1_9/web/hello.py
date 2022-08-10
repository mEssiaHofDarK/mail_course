def app(environ, start_response):
    """Simplest possible application object"""
    print(environ)
    try:
        query = bytes(environ.get('QUERY_STRING').encode('utf-8').replace('&', '\n'))
        print(environ.get('QUERY_STRING'))
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
