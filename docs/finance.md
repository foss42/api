# Currency Conversion API

Convert an amount from one currency to another using static rates.

**Endpoint:** `POST /currency/convert`

**Request Body:**
```json
{
  "amount": 100,
  "from_currency": "USD",
  "to_currency": "EUR"
}
```

**Response:**
```json
{
  "from_currency": "USD",
  "to_currency": "EUR",
  "amount": 100,
  "converted": 94.5,
  "rate": 0.945
}
```

- Supported currencies: USD, EUR, INR
- Returns 400 if conversion is not available.

---

> **Note:** In production, rates should be fetched from a real provider.
