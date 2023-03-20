class BlockErrors:
    def __init__(self, exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return any([isinstance(exc_value, exception)
                    for exception in self.exceptions])
