from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_ccxt_system_time = publicGetCcxtSystemTime = Entry('ccxt/system/time', 'public', 'GET', {'cost': 10})
    public_get_ccxt_system_status = publicGetCcxtSystemStatus = Entry('ccxt/system/status', 'public', 'GET', {'cost': 10})
    public_get_ccxt_exchange_tradefee = publicGetCcxtExchangeTradefee = Entry('ccxt/exchange/tradefee', 'public', 'GET', {'cost': 10})
    public_get_ccxt_exchange_tradefees = publicGetCcxtExchangeTradefees = Entry('ccxt/exchange/tradefees', 'public', 'GET', {'cost': 10})
    public_get_ccxt_market_orderbook = publicGetCcxtMarketOrderBook = Entry('ccxt/market/orderBook', 'public', 'GET', {'cost': 10})
    public_get_ccxt_market_ticker24hr = publicGetCcxtMarketTicker24Hr = Entry('ccxt/market/ticker24Hr', 'public', 'GET', {'cost': 10})
    public_get_ccxt_market_markets = publicGetCcxtMarketMarkets = Entry('ccxt/market/markets', 'public', 'GET', {'cost': 10})
    private_get_ccxt_wallet_balance = privateGetCcxtWalletBalance = Entry('ccxt/wallet/balance', 'private', 'GET', {'cost': 10})
    private_get_ccxt_trade_order = privateGetCcxtTradeOrder = Entry('ccxt/trade/order', 'private', 'GET', {'cost': 10})
    private_get_ccxt_trade_order_open_orders = privateGetCcxtTradeOrderOpenOrders = Entry('ccxt/trade/order/open-orders', 'private', 'GET', {'cost': 10})
    private_get_ccxt_trade_userleverages = privateGetCcxtTradeUserLeverages = Entry('ccxt/trade/userLeverages', 'private', 'GET', {'cost': 10})
    private_get_ccxt_trade_userleverage = privateGetCcxtTradeUserLeverage = Entry('ccxt/trade/userLeverage', 'private', 'GET', {'cost': 10})
    private_get_ccxt_trade_positions = privateGetCcxtTradePositions = Entry('ccxt/trade/positions', 'private', 'GET', {'cost': 10})
    private_post_ccxt_trade_order = privatePostCcxtTradeOrder = Entry('ccxt/trade/order', 'private', 'POST', {'cost': 10})
    private_post_ccxt_trade_order_addtpsl = privatePostCcxtTradeOrderAddTPSL = Entry('ccxt/trade/order/addTPSL', 'private', 'POST', {'cost': 10})
    private_post_ccxt_trade_addmargin = privatePostCcxtTradeAddMargin = Entry('ccxt/trade/addMargin', 'private', 'POST', {'cost': 10})
    private_post_ccxt_trade_reducemargin = privatePostCcxtTradeReduceMargin = Entry('ccxt/trade/reduceMargin', 'private', 'POST', {'cost': 10})
    private_post_ccxt_trade_position_close = privatePostCcxtTradePositionClose = Entry('ccxt/trade/position/close', 'private', 'POST', {'cost': 10})
    private_post_ccxt_trade_update_userleverage = privatePostCcxtTradeUpdateUserLeverage = Entry('ccxt/trade/update/userLeverage', 'private', 'POST', {'cost': 10})
    private_delete_ccxt_trade_order = privateDeleteCcxtTradeOrder = Entry('ccxt/trade/order', 'private', 'DELETE', {'cost': 10})
