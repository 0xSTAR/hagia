def HAGIA_ASSERT(STATEMENT:bool,MSG:str=""):
    if not STATEMENT:
        raise BASE_HAGIA_ERROR(MSG)

class BASE_HAGIA_ERROR(BaseException):
    def __init__(self,msg:str="Error."):
        super().__init__(str(msg))

    #def __raise__(self,msg=None):
    #    super().__init__(msg)
