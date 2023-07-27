class InvalidUuidException(Exception):
    def __init__(self, error='ID must be a valid UUID') -> None:
        super().__init__(error)


class InvalidCpfException(Exception):
    def __init__(self, error='Invalid CPF') -> None:
        super().__init__(error)
