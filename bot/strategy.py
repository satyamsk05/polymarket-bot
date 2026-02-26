from dataclasses import dataclass
from enum import Enum


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass
class Signal:
    side: Side
    token_id: str
    size: float


@dataclass
class BotState:
    last_mid_price: float | None = None
    position_yes: float = 0.0
    position_no: float = 0.0


class MomentumStrategy:
    def __init__(self, threshold_bps: float, order_size: float, max_position: float):
        self.threshold_bps = threshold_bps
        self.order_size = order_size
        self.max_position = max_position

    def generate(
        self,
        state: BotState,
        current_mid: float,
        token_id_yes: str,
        token_id_no: str,
    ) -> Signal | None:
        if state.last_mid_price is None:
            state.last_mid_price = current_mid
            return None

        prev = state.last_mid_price
        state.last_mid_price = current_mid
        if prev <= 0:
            return None

        move_bps = ((current_mid - prev) / prev) * 10_000

        if move_bps >= self.threshold_bps:
            if state.position_yes + self.order_size <= self.max_position:
                return Signal(side=Side.BUY, token_id=token_id_yes, size=self.order_size)
            return None

        if move_bps <= -self.threshold_bps:
            if state.position_no + self.order_size <= self.max_position:
                return Signal(side=Side.BUY, token_id=token_id_no, size=self.order_size)
            return None

        return None
