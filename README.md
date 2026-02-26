# Polymarket Trading Bot (Starter)

Ye ek **starter bot** hai jo Polymarket CLOB API ke saath connect hoke simple strategy run karta hai.
Default mode `dry-run` hai taaki real order place na ho jab tak aap explicitly live mode enable na karo.

## Features
- Python based async polling bot
- Basic momentum strategy (mid-price change based)
- Risk controls:
  - max position per market
  - max order size
  - cooldown between orders
  - dry-run mode
- `.env` driven configuration

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Phir `.env` me apni values set karo.

## Run

```bash
python bot/main.py
```

## Important
- Ye educational starter hai, guaranteed profitable strategy nahi.
- Live trading se pehle:
  - small size se test karo
  - API keys aur wallet permissions verify karo
  - exchange rules aur jurisdiction compliance check karo

## Next improvements
- Multi-market portfolio logic
- Better signal generation (orderbook imbalance, volatility filter)
- Backtesting module
- Structured logging + alerting
