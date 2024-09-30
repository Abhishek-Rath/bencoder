import re
import string
import itertools as it

from benoder.exceptions import BencodeDecodeError

class BencoderParser():

    def encoder(self, data):
        if isinstance(data, int):
            return b"i" + str(data).encode() + b"e"
        elif isinstance(data, bytes):
            return str(len(data)).encode() + b":" + data
        elif isinstance(data, str):
            return self.encoder(data.encode("ascii"))
        elif isinstance(data, list):
            return b"l" + b"".join(map(self.encoder, data)) + b"e"
        elif isinstance(data, dict):
            items = [(k.encode('utf-8') if isinstance(k, str) else k, v) for k, v in data.items()]
            items.sort()  # Sort items by keys

            encoded_dict = b"d" + b"".join(
                self.encoder(k) + self.encoder(v) for k, v in items
            ) + b"e"

            return encoded_dict


    def decoder(self, data):
        if data.startswith(b"i"):
            match = re.match(b"i(-?\\d+)e", data)
            return int(match.group(1)), data[match.span()[1]:]

        elif data.startswith(b"l") or data.startswith(b"d"):
            items = []
            rest = data[1:] # skip the first character
            while not rest.startswith(b"e"):
                item, rest = self.decoder(rest)
                # print("Item: ", item)
                # print("Rest: ", rest)
                items.append(item)
            rest = rest[1:]
            if data.startswith(b"l"):
                return items, rest
            else:
                return {i: j for i, j in zip(items[::2], items[1::2])}, rest

        elif any(data.startswith(i.encode()) for i in string.digits):
            match = re.match(b"(\\d+):", data)
            length = int(match.group(1))
            rest_index = match.span()[1]
            start_index = rest_index
            end_index = start_index + length
            return data[start_index:end_index], data[end_index:]
        else:
            print("Invalid Input")
