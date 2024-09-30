class BencodeDecodeError(Exception):
    """Exception raised for errors in the decoding of bencoded data."""
    def __init__(self, message):
        super().__init__(message)
