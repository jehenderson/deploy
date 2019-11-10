import urllib.request

def logging_middleware(get_response):
    # One-time configuration and initialization.
    url = "https://npky8rle0m.execute-api.us-east-1.amazonaws.com/default/analytics"

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.method == 'GET':
            req = urllib.request.Request(url)
        elif request.method == 'POST':
            data = request.body
            req = urllib.request.Request(url, data)
        else:
            return("Bad request type")
        response = urllib.request.urlopen(req)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
