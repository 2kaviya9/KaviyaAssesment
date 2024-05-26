from enum import Enum

class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'
    CONNECT = 'CONNECT'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

# Example usage
if __name__ == "__main__":
    for choice in HTTPMethods.choices():
        print(choice)
