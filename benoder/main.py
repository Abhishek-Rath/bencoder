from benoder.parser import BencoderParser

parser = BencoderParser()
data = b'l4:spami42ee'
result = parser.decoder(data)
print(result)  # Output: {b'foo': b'bar'}
