from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class Services(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(self, int1, int2):
        return int1 + int2

    @rpc(Integer, Integer, _returns=Integer)
    def sub(self, int1, int2):
        return int1 - int2
    
    @rpc(str, _returns=str)
    def toCipher(self, input):
        out = ""
        input = input.encode(encoding='ascii', errors='replace')
        seed = len(input)

        for char in input:
            char += seed
            if char > 126:
                char %= 127
                if char < 32:
                    char += 32
            seed = char
            char = chr(char)
            out += char
            
        return out

    @rpc(str, _returns=str)
    def fromCipher(self, input):
        out = ""
        input = input.encode(encoding='ascii', errors='replace')
        seed = len(input) % 128

        for char in input:
            temp = char
            char -= seed
            if char < 32:
                char += 127
                if char > 126:
                    char -= 32
            seed = temp
            char = chr(char)
            out += char

        return out

soap_app = Application([Services], 'namespace.com',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())
soap_wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 1337, soap_wsgi_app)
    print("SOAP server started")
    server.serve_forever()
