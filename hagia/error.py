class pyco8_init_error(RuntimeError):
    def __init__(self,msg) -> None:
        self.exception_message = msg
    def __repr__(self) -> str:
        sys.stdout.write(f'\n{self.exception_message}')
        return self.exception_message

class atlas_error(Exception):
    def __init__(self,msg:str)->None:
        super().__init__(msg)

        self.error_message:str = msg

    @property
    def error(self) -> str:
        return self.error_message

    def __str__(self) -> str:
        return str(self.error)

    def __repr__(self):
        return self.error