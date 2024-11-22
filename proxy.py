from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if "sahtesite.com" in flow.request.pretty_url:
        # Yönlendirme yapılacak URL
        flow.response = http.Response.make(
            302,  # HTTP Status code 302 (Yönlendirme)
            b"",  # Boş bir gövde
            {"Location": "http://localhost:8080/analiz.php"}  # Yönlendirilecek URL
        )
