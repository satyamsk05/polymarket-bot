import asyncio
import time

from config import load_config
from polymarket_client import PolymarketClient
from strategy import BotState, MomentumStrategy


async def run() -> None:
    cfg = load_config()
    client = PolymarketClient(
        host=cfg.polymarket_host,
        chain_id=cfg.chain_id,
        private_key=cfg.private_key,
    )
    strategy = MomentumStrategy(
        threshold_bps=cfg.momentum_threshold_bps,
        order_size=cfg.order_size,
        max_position=cfg.max_position,
    )
    state = BotState()
    last_order_ts = 0.0

    print("Bot started", {"market_id": cfg.market_id, "dry_run": cfg.dry_run})

    while True:
        quote = await client.get_quote(cfg.token_id_yes)
        signal = strategy.generate(
            state=state,
            current_mid=quote.mid,
            token_id_yes=cfg.token_id_yes,
            token_id_no=cfg.token_id_no,
        )

        now = time.time()
        if signal and now - last_order_ts >= cfg.cooldown_seconds:
            order_id = await client.place_limit_buy(
                token_id=signal.token_id,
                size=signal.size,
                price=quote.mid,
                dry_run=cfg.dry_run,
            )
            last_order_ts = now
            if signal.token_id == cfg.token_id_yes:
                state.position_yes += signal.size
            else:
                state.position_no += signal.size

            print(
                "Order sent",
                {
                    "order_id": order_id,
                    "token": signal.token_id,
                    "size": signal.size,
                    "mid": round(quote.mid, 4),
                    "pos_yes": state.position_yes,
                    "pos_no": state.position_no,
                },
            )

        await asyncio.sleep(cfg.poll_interval_seconds)


if __name__ == "__main__":
    asyncio.run(run())
