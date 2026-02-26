import os
from dataclasses import dataclass


@dataclass
class BotConfig:
    polymarket_host: str
    private_key: str
    chain_id: int
    market_id: str
    token_id_yes: str
    token_id_no: str
    order_size: float
    max_position: float
    cooldown_seconds: int
    momentum_threshold_bps: float
    dry_run: bool
    poll_interval_seconds: float


def _must_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required env var: {name}")
    return value


def load_config() -> BotConfig:
    return BotConfig(
        polymarket_host=os.getenv("POLYMARKET_HOST", "https://clob.polymarket.com"),
        private_key=_must_env("PRIVATE_KEY"),
        chain_id=int(os.getenv("CHAIN_ID", "137")),
        market_id=_must_env("MARKET_ID"),
        token_id_yes=_must_env("TOKEN_ID_YES"),
        token_id_no=_must_env("TOKEN_ID_NO"),
        order_size=float(os.getenv("ORDER_SIZE", "5")),
        max_position=float(os.getenv("MAX_POSITION", "50")),
        cooldown_seconds=int(os.getenv("COOLDOWN_SECONDS", "10")),
        momentum_threshold_bps=float(os.getenv("MOMENTUM_THRESHOLD_BPS", "25")),
        dry_run=os.getenv("DRY_RUN", "true").lower() in {"1", "true", "yes"},
        poll_interval_seconds=float(os.getenv("POLL_INTERVAL_SECONDS", "2")),
    )
