import { implicitReturnType } from '../base/types.js';
import { Exchange as _Exchange } from '../base/Exchange.js';
interface Exchange {
    publicGetCcxtSystemTime(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtSystemStatus(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtExchangeTradefee(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtExchangeTradefees(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtMarketOrderBook(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtMarketTicker24Hr(params?: {}): Promise<implicitReturnType>;
    publicGetCcxtMarketMarkets(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtWalletBalance(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtTradeOrder(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtTradeOrderOpenOrders(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtTradeUserLeverages(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtTradeUserLeverage(params?: {}): Promise<implicitReturnType>;
    privateGetCcxtTradePositions(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradeOrder(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradeOrderAddTPSL(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradeAddMargin(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradeReduceMargin(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradePositionClose(params?: {}): Promise<implicitReturnType>;
    privatePostCcxtTradeUpdateUserLeverage(params?: {}): Promise<implicitReturnType>;
    privateDeleteCcxtTradeOrder(params?: {}): Promise<implicitReturnType>;
}
declare abstract class Exchange extends _Exchange {
}
export default Exchange;
