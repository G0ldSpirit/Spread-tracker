# 🚀 Polymarket Market Finder

A modern web app to discover and analyze Polymarket prediction markets.

## Features

- 📊 Real-time market data from Polymarket
- 🔍 Filter by volume and liquidity
- 📈 Sort markets by various metrics
- 💰 View current Yes/No prices
- 📱 Fully responsive design

## Deploy to Vercel

### Quick Deploy (Recommended)

1. Push this code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Click "Deploy" ✅

### Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd polymarket-vercel-final
vercel
```

## Local Development

```bash
# Install Vercel CLI
npm install -g vercel

# Run locally
vercel dev
```

Then open http://localhost:3000

## Project Structure

```
polymarket-vercel-final/
├── index.html          # Frontend
├── api/
│   └── markets.py     # Serverless API function
├── vercel.json        # Vercel configuration
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## API Endpoint

- `GET /api/markets` - Returns top 100 active markets by volume

## Tech Stack

- Frontend: Vanilla HTML/CSS/JavaScript
- Backend: Python (Serverless Functions)
- Deployment: Vercel
- Data Source: Polymarket Gamma API

## Notes

- Markets are sorted by volume by default
- Prices are shown in cents (¢)
- Click any market card to open it on Polymarket.com

## License

MIT
