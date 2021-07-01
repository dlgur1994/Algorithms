class Codec:
    def __init__(self):
        self.dict = {}

    def encode(self, longUrl: str) -> str:
        shortUrl = hash(longUrl) # Create a hash value through hash()
        self.dict[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.dict[shortUrl]

codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.encode(url))
print(codec.decode(codec.encode(url)))
