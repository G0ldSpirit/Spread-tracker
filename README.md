# 📊 Polymarket Real Spreads

A secure web application that displays **real bid-ask spreads** from Polymarket order books.

## Features

- 🔐 **Secure API authentication** via environment variables
- 📊 **Real bid/ask spreads** calculated from order books
- 💰 **Top 30 markets** by volume
- 🎯 **Filter by minimum spread**
- 📈 **Sort by spread or volume**
- 🔄 **Real-time data**

## Tech Stack

- Frontend: HTML/CSS/JavaScript
- Backend: Python (Serverless Functions)
- API: Polymarket CLOB via `py-clob-client`
- Deployment: Vercel

## Setup

See **SETUP_GUIDE.md** for detailed deployment instructions.

### Quick Start

1. Clone repo
2. Push to GitHub
3. Deploy to Vercel
4. Add environment variables:
   - `POLYMARKET_API_KEY`
   - `POLYMARKET_API_SECRET`
   - `POLYMARKET_API_PASSPHRASE`

## Security

⚠️ **Never commit your API credentials to GitHub!**

All credentials are stored as Vercel environment variables and never exposed in the codebase.

## API Response Time

Fetching real spreads from order books takes 30-60 seconds due to multiple API calls.

## License

MIT
