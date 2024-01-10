# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable= pointless-string-statement


from abc import ABC


class Tyre(ABC):
    def __init__(self):
        pass

    def tyre_needs_service(self):
        pass 