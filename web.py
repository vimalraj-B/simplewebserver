from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
 <style>
    .product-link {
        background-color: (0,113,133);
    }
    .product-name{
        color: black;
        font-size: larger;
        font-weight: bolder;
    }
    .product-status {
        color: green;
        font-size: medium;
        font-weight: bold;
    }
    .product-cart{
        background-color: rgb(255, 216, 20);
        color: black;
        border: none;
        height: 35px;
        width: 105px;
        border-radius: 20px;
        font-weight: bold;
        cursor: pointer;
        margin-right: 8px;
    }
    .product-buy{
        background-color: rgb(255, 164, 28);
        color: black;
        border: none;
        height: 35px;
        width: 105px;
        border-radius: 20px;
        font-weight: bold;
        cursor: pointer;
        margin-right: 8px;
    }
 </style>
 
 
 
 <a class="product-link"
    href="https://www.amazon.com/nike-running-shoes/s?k=nike+running+shoes">
    Back to amazon
 </a>

 <p class="product-name">
    Nike Black Running Shoes 
 </p>

<p class="product-status">
    $39 - in stock
</p>

<p class="product-delivery">
    Free Delivery tomorrow.
</p>

<button class="product-cart">
    Add to Cart
</button>

<button class="product-buy">
    Buy now
</button>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()