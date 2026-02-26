import asyncio
import random
from dataclasses import dataclass


@dataclass
class Quote:
    best_bid: float
    best_ask: float

    @property
    def mid(self) -> float:
        return (self.best_bid + self.best_ask) / 2


class PolymarketClient:
    """
    Minimal placeholder client.

    TODO:
    - integrate with py-clob-client for real data and order placement.
    - authenticate with private key + chain id.
    """

    def __init__(self, host: str, chain_id: int, private_key: str):
        self.host = host
        self.chain_id = chain_id
        self.private_key = private_key
        self._synthetic_mid = 0.50

    async def get_quote(self, token_id: str) -> Quote:
        _ = token_id
        delta = random.uniform(-0.005, 0.005)
        self._synthetic_mid = max(0.01, min(0.99, self._synthetic_mid + delta))
        spread = 0.01
        bid = max(0.0, self._synthetic_mid - spread / 2)
        ask = min(1.0, self._synthetic_mid + spread / 2)
        await asyncio.sleep(0)
        return Quote(best_bid=bid, best_ask=ask)

    async def place_limit_buy(self, token_id: str, size: float, price: float, dry_run: bool = True) -> str:
        await asyncio.sleep(0)
        if dry_run:
            return f"dryrun-buy-{token_id}-{size}@{price:.4f}"

        # TODO: replace with real order placement in live mode.
        raise NotImplementedError("Live order placement not implemented yet. Keep DRY_RUN=true.")
