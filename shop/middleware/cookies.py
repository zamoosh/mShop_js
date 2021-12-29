class Cookie:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.kir = "salam"
        print(request.COOKIES)
        print("hello world!")
        print(response.kir)
        return response
