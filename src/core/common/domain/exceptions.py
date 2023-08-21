class InvalidUuidException(Exception):
    def __init__(self, error='ID must be a valid UUID') -> None:
        super().__init__(error)


class InvalidCpfException(Exception):
    def __init__(self, error='Invalid CPF') -> None:
        super().__init__(error)


class EntityValidationException(Exception):
    def __init__(self, error='Entity Validation Error') -> None:
        super().__init__(error)


class LoadEntityException(Exception):
    def __init__(self, error='Load Entity Error') -> None:
        super().__init__(error)


class NotFoundException(Exception):
    pass