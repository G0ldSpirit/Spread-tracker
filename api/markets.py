from http.server import BaseHTTPRequestHandler
import json
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Fetch from Polymarket API
            url = 'https://gamma-api.polymarket.com/markets?limit=100&closed=false&order=volume&ascending=false'
            
            req = urllib.request.Request(url)
            req.add_header('Accept', 'application/json')
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            with urllib.request.urlopen(req, timeout=15) as response:
                markets = json.loads(response.read().decode('utf-8'))
            
            # Process markets
            processed = []
            for market in markets:
                try:
                    prices = market.get('outcomePrices', [])
                    
                    if isinstance(prices, str):
                        prices = json.loads(prices)
                    
                    if prices and len(prices) >= 2:
                        yes = float(prices[0][0] if isinstance(prices[0], list) else prices[0])
                        no = float(prices[1][0] if isinstance(prices[1], list) else prices[1])
                        
                        market['yesPrice'] = yes
                        market['noPrice'] = no
                    
                    processed.append(market)
                except:
                    continue
            
            # Response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({'markets': processed}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                'error': str(e),
                'markets': []
            }).encode())
