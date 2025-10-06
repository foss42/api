# Static currency rates for demo purposes
# In production, fetch from a real API
CURRENCY_RATES = {
    'USD': {
        'EUR': 0.945,
        'INR': 83.0,
        'USD': 1.0,
    },
    'EUR': {
        'USD': 1.058,
        'INR': 87.8,
        'EUR': 1.0,
    },
    'INR': {
        'USD': 0.012,
        'EUR': 0.011,
        'INR': 1.0,
    },
}

def get_rate(from_currency: str, to_currency: str) -> float:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency in CURRENCY_RATES and to_currency in CURRENCY_RATES[from_currency]:
        return CURRENCY_RATES[from_currency][to_currency]
    raise ValueError(f"Conversion rate from {from_currency} to {to_currency} not available.")
