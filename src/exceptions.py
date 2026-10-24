# Exception is built-in class
# available automatically

# invalid breederror
class InvalidBreedError(Exception):
    pass

# invalid pet size error
class InvalidSizeError(Exception):
    # __init__ + getMessage() ????
    pass

# invalid pet coat error
class InvalidCoatError(Exception):
    pass

class EmptySearchError(Exception):
    pass
