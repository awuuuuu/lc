#记住string.ascii_letters, string.digits, random.choice, def __init__(self): self.m...

class Codec:
    s = string.ascii_letters + string.digits
    def __init__(self):
        self.m = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while 1:
            key = "".join([random.choice(Codec.s) for i in range(6)])
            if key not in self.m:
                self.m[key] = longUrl
                return key
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.m[shortUrl] if shortUrl in self.m else ""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
