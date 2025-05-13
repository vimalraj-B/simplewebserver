# EX01 Developing a Simple Webserver
## Date:13.05.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot 2025-05-12 103908.png>)

![alt text](<Screenshot 2025-05-12 103919.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
