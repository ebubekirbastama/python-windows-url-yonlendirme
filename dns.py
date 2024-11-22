from dnslib import DNSRecord, QTYPE, RR, A
from socketserver import BaseRequestHandler, UDPServer

class DNSHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        request = DNSRecord.parse(data)
        reply = request.reply()
        for question in request.questions:
            if question.qname.match("örneksite.com.tr"):
                print(question)
                reply.add_answer(RR(question.qname, QTYPE.A, ttl=60, rdata=A("192.168.1.100")))
        socket.sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    server = UDPServer(("0.0.0.0", 53), DNSHandler)
    print("DNS server running on port 53...")
    server.serve_forever()
