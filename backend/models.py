from pydantic import BaseModel
from typing import Optional


class StockData(BaseModel):
    Date: str
    Ticker: str
    Ticker_Open: float
    Ticker_Close: float
    Ticker_High: float
    Ticker_Low: float
    Ticker_Volume: float
    Ticker_SMA_10: Optional[float] = None
    Ticker_EMA_10: Optional[float] = None
    Ticker_SMA_30: Optional[float] = None
    Ticker_EMA_30: Optional[float] = None
    Ticker_RSI: Optional[float] = None
    Ticker_Stochastic_K: Optional[float] = None
    Ticker_Stochastic_D: Optional[float] = None
    Ticker_MACD: Optional[float] = None
    Ticker_MACD_Signal: Optional[float] = None
    Ticker_MACD_Diff: Optional[float] = None
    Ticker_TSI: Optional[float] = None
    Ticker_UO: Optional[float] = None
    Ticker_ROC: Optional[float] = None
    Ticker_Williams_R: Optional[float] = None
    Ticker_Bollinger_High: Optional[float] = None
    Ticker_Bollinger_Low: Optional[float] = None
    Ticker_Bollinger_Mid: Optional[float] = None
    Ticker_Bollinger_PBand: Optional[float] = None
    Ticker_Bollinger_WBand: Optional[float] = None
    Ticker_On_Balance_Volume: Optional[float] = None
    Ticker_Chaikin_MF: Optional[float] = None
    Ticker_Force_Index: Optional[float] = None
    Ticker_MFI: Optional[float] = None


class CompanyInfo(BaseModel):
    Ticker: str
    FullName: Optional[str] = None
    Sector: Optional[str] = None
    Subsector: Optional[str] = None
    MarketCap: Optional[int] = None
    Country: Optional[str] = None
    Website: Optional[str] = None
    Description: Optional[str] = None
    CEO: Optional[str] = None
    Employees: Optional[int] = None
    City: Optional[str] = None
    State: Optional[str] = None
    Zip: Optional[str] = None
    Address: Optional[str] = None
    Phone: Optional[str] = None
    Exchange: Optional[str] = None
    Currency: Optional[str] = None
    QuoteType: Optional[str] = None
    ShortName: Optional[str] = None
    Price: Optional[float] = None
    DividendRate: Optional[float] = None
    DividendYield: Optional[float] = None
    PayoutRatio: Optional[float] = None
    Beta: Optional[float] = None
    PE: Optional[float] = None
    EPS: Optional[float] = None
    Revenue: Optional[int] = None
    GrossProfit: Optional[int] = None
    FreeCashFlow: Optional[int] = None


class StockGroupings(BaseModel):
    momentum: list[str]
    breakout: list[str]
    trend_strength: list[str]


class SearchResult(BaseModel):
    ticker: str
    name: str
