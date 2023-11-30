from pydantic import BaseModel


class Response(BaseModel):
    status: bool = None
    code: int = None
    message: str = None
    data: dict = None

    def __init__(self, status: bool = None, code: int = None, message: str = None, data: dict = None):
        super().__init__(status=status, code=code, message=message, data=data)

    def DefaultOK(data: dict = {}):
        return Response(status=True, code=200, message="OK", data=data)

    def DefaultBadRequest():
        return Response(status=False, code=400, message="Bad Request", data={})

    def DefaultNotFound():
        return Response(status=False, code=404, message="Not Found", data={})

    def DefaultInternalServerError():
        return Response(status=False, code=500, message="Internal Server Error", data={})
