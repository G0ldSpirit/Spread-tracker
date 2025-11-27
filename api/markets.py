from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add py_clob_client to imports
try:
    from py_clob_client.client import ClobClient
    from py_clob_client.clob_types import BookParams
except ImportError:
    # Will be installed via requirements.txt
    pass

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get credentials from environment variables
            api_key = os.environ.get('POLYMARKET_API_KEY')
            api_secret = os.environ.get('POLYMARKET_API_SECRET')
            api_passphrase = os.environ.get('POLYMARKET_API_PASSPHRASE')
            
            if not all([api_key, api_secret, api_passphrase]):
                raise Exception("Missing API credentials in environment variables")
            
            host = "https://clob.polymarket.com"
            
            # Initialize client with API credentials
            client = ClobClient(host)
            client.set_api_creds({
                'api_key': api_key,
                'api_secret': api_secret,
                'api_passphrase': api_passphrase
            })
            
            # Get top markets by volume (limit to 30 for performance)
            markets_response = client.get_markets(limit=30)
            markets = markets_response if isinstance(markets_response, list) else []
            
            processed = []
            
            for market in markets[:30]:  # Limit to 30
                try:
                    # Get token ID for the YES outcome
                    tokens = market.get('tokens', [])
                    if not tokens or len(tokens) < 2:
                        continue
                    
                    yes_token_id = tokens[0].get('token_id')
                    no_token_id = tokens[1].get('token_id')
                    
                    if not yes_token_id or not no_token_id:
                        continue
                    
                    # Get order book for YES token
                    try:
                        book = client.get_order_book(yes_token_id)
                        
                        bids = book.get('bids', [])
                        asks = book.get('asks', [])
                        
                        if not bids or not asks:
                            continue
                        
                        # Best bid and ask for YES
                        yes_bid = float(bids[0]['price'])
                        yes_ask = float(asks[0]['price'])
                        
                        # Calculate NO prices (complement)
                        no_bid = 1 - yes_ask
                        no_ask = 1 - yes_bid
                        
                        # Calculate spreads
                        yes_spread = ((yes_ask - yes_bid) / ((yes_bid + yes_ask) / 2)) * 100 if (yes_bid + yes_ask) > 0 else 0
                        no_spread = ((no_ask - no_bid) / ((no_bid + no_ask) / 2)) * 100 if (no_bid + no_ask) > 0 else 0
                        
                        # Average spread
                        avg_spread = (yes_spread + no_spread) / 2
                        
                        # Add to market data
                        market['yesPrice'] = yes_bid  # Using bid as the "current" price
                        market['noPrice'] = no_bid
                        market['yesBid'] = yes_bid
                        market['yesAsk'] = yes_ask
                        market['noBid'] = no_bid
                        market['noAsk'] = no_ask
                        market['spread'] = avg_spread
                        
                        processed.append(market)
                        
                    except Exception as e:
                        # Skip markets with order book errors
                        continue
                        
                except Exception as e:
                    continue
            
            # Sort by spread descending
            processed.sort(key=lambda x: x.get('spread', 0), reverse=True)
            
            # Response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                'markets': processed,
                'count': len(processed)
            }).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                'error': str(e),
                'markets': []
            }).encode())
