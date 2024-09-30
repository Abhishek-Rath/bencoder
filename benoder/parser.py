import re
import string

from benoder.exceptions import BencodeDecodeError

class BencoderParser():

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
