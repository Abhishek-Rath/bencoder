from benoder.parser import BencoderParser

parser = BencoderParser()
data = b'l4:spami42ee'
result = parser.decoder(data)
print(result)


# Encoding an integer
encoded_integer = parser.encoder(42)
print(encoded_integer)  # Output: b'i42e'

# Encoding a string
encoded_string = parser.encoder("spam")
print(encoded_string)  # Output: b'4:spam'

# Encoding a list
encoded_list = parser.encoder([42, "spam"])
print(encoded_list)  # Output: b'li42e4:spame'

# Encoding a dictionary
encoded_dict = parser.encoder({"key": "value"})
print(encoded_dict)  # Output: b'd3:key5:valuee'
