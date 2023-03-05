class FailedSchemaException(Exception):
    '''
    Exception raised when a schema test fails.

    Attributes:
    	message: A description of the error. optional.
    '''

    def __init__(self, message="Data did not conform to schema"):
        self.message = message
        super().__init__(self.message)
