def app(environ, start_response):
    """Simplest possible application object"""
    try:
        query = '\n'.join(environ['QUERY_STRING'].split('&'))
        body = [bytes(i+'\n', 'utf-8') for i in environ['QUERY_STRING'].split('&')]
        # data = b'Hello, World!\n'
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/plain')
        ]
        start_response(status, response_headers)
        return body
    except KeyError:
        return 1
