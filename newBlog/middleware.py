class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"  # Allows all origins (replace "*" with specific origins if needed)
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
