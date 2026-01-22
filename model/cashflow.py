def monthly_noi(emart_rent, parking_rent, operating_cost=0):
    """
    Calculate monthly net operating income (NOI).
    """
    return emart_rent + parking_rent - operating_cost


def monthly_interest(debt, annual_rate):
    """
    Calculate monthly interest expense.
    """
    return debt * annual_rate / 12


def net_cashflow(noi, interest):
    """
    Net cashflow after debt service.
    """
    return noi - interest
