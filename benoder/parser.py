class BencodeParser:

    def parse(self, bencode_data):
        """
        Main entry point for parsing bencode data
        :param bencode_data:
        :return: parsed bencode data
        """
        if isinstance(bencode_data, bytes):
            bencode_data = bencode_data.decode('utf-8')
        return self._parse_value(bencode_data)

    def _parse_value(self, data):
        """
        Parse data based on it's type
        :param bencode_data:
        :return:
        """
        if data.startswith('i'):
            return self._parse_integer(data)
        elif data.startswith('l'):
            return self._parse_list(data)
        elif data.startswith('d'):
            return self._parse_dict(data)
        else:
            return self._parse_string(data)

    def _parse_integer(self, data):
        pass

    def _parse_list(self, data):
        pass

    def _parse_dict(self, data):
        pass

    def _parse_string(self, data):
        pass
