import unittest

from benoder.parser import BencoderParser
from benoder.exceptions import BencodeDecodeError

class TestBencodeParser(unittest.TestCase):
    def setUp(self):
        self.parser = BencoderParser()

    def test_parse_integer(self):
        result, _ = self.parser.decoder(b'i42e')
        self.assertEqual(result, 42)

    def test_parse_list(self):
        # Test for a simple list 'l4:spami42ee' -> ['spam', 42]
        result, _ = self.parser.decoder(b'l4:spami42ee')
        self.assertEqual(result, [b'spam', 42])

    def test_parse_dict(self):
        result, _ = self.parser.decoder(b'd3:foo3:bar3:baz3:quxe')
        self.assertEqual(result, {b'foo': b'bar', b'baz': b'qux'})

    def test_parse_string(self):
        result, _ = self.parser.decoder(b'4:spam')
        self.assertEqual(result, b'spam')


if __name__ == '__main__':
    unittest.main(verbosity=2)
