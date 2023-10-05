import math

# User input variables
_NUM_PROJECTION_YEARS = 5
_ESTIMATED_GROWTH_RATE = 0.1
_DISCOUNT_RATE = 0.08
_PERMANENT_GROWTH_RATE = 0.025

# Info that can be found on ER or Yahoo finance
_INITIAL_CASH_FLOW = 100
_CASH_AND_SHORT_TERM_INVESTMENTS_VALUE = 500
_TOTAL_DEBT = 800
_TOTAL_FLOATING_SHARES = 100

def EstimateFutureCashFlow(initial_cash_flow, num_projection_years, estimated_growth_rate):
	future_cash_flow = [initial_cash_flow]

	for i in range(0, num_projection_years):
		cash_flow = future_cash_flow[-1] * (1 + estimated_growth_rate)
		future_cash_flow.append(round(cash_flow, 2))

	return future_cash_flow

def CalculateCashFlowUltimateValue(initla_year_cash_flow, discount_rate, permanent_growth_rate):
	return (initla_year_cash_flow * (1 + permanent_growth_rate)) / (discount_rate - permanent_growth_rate)

def DiscountFutureCashFlow(cash_flows, discount_rate):
	discounted_future_cash_flows = []

	for i in range(0, len(cash_flows)):
		power = min(len(cash_flows)-1, (1 + i))
		discounted_cash_flow = cash_flows[i] / ((1 + discount_rate) ** power)
		discounted_future_cash_flows.append(round(discounted_cash_flow, 2))

	return discounted_future_cash_flows

def ConvertEnterpriseValueToEquityValue(enterprise_value, cash, debt):
	return enterprise_value + cash - debt

def CalculateFairStockValue(equity_value, total_floating_shares):
	return round(equity_value / total_floating_shares, 2)

if __name__ == '__main__':
	estimated_future_cash_flow = EstimateFutureCashFlow(_INITIAL_CASH_FLOW, _NUM_PROJECTION_YEARS, _ESTIMATED_GROWTH_RATE)
	print(f'estimated_future_cash_flow: {estimated_future_cash_flow}')

	cash_flow_ultimate_value = CalculateCashFlowUltimateValue(estimated_future_cash_flow[-1], _DISCOUNT_RATE, _PERMANENT_GROWTH_RATE)
	print(f'cash_flow_ultimate_value: {cash_flow_ultimate_value}')

	estimated_future_cash_flow.append(cash_flow_ultimate_value)
	discounted_future_cash_flows = DiscountFutureCashFlow(estimated_future_cash_flow[1:], _DISCOUNT_RATE)
	print(f'discounted_future_cash_flows: {discounted_future_cash_flows}')

	company_fair_value = sum(discounted_future_cash_flows)
	print(f'company_fair_value: {company_fair_value}')

	equity_value = ConvertEnterpriseValueToEquityValue(company_fair_value, _CASH_AND_SHORT_TERM_INVESTMENTS_VALUE, _TOTAL_DEBT)
	print(f'equity_value: {equity_value}')

	fair_stock_value = CalculateFairStockValue(equity_value, _TOTAL_FLOATING_SHARES)
	print(f'fair_stock_value: {fair_stock_value}')

