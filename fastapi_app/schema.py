from pydantic import BaseModel

class PredictionInput(BaseModel):
    store_id: int
    sku_id: int
    category: int
    channel: int
    unit_price: float
    discount_pct: float
    stock_on_hand: int
    reorder_point: int
    safety_stock: int
    year: int
    month: int
    week: int
    day: int
    day_of_week: int
    is_weekend: int
    lag_1: float
    lag_7: float
    lag_30: float
    rolling_7: float
    rolling_30: float
    stock_gap: float