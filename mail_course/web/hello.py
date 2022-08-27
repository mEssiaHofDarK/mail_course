def app(environ, start_response):
    """Simplest possible application object"""
    body = [b'Hello, World!\n']
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, response_headers)
    return body
