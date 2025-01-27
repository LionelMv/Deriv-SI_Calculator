# SIRC API Documentation
This API calculates the position size (lot), the number of pips, and the total risk in USD for a trade based on input parameters. This endpoint is ideal for frontend integration to dynamically calculate trade risk without storing data.
#### Base URL
```
http://127.0.0.1:8000/api/risk-calculation/
```
---

### Endpoint

#### `POST /api/risk-calculation/`

Calculates the risk parameters for a synthetic index trade.

---

### Request Parameters

| Field             | Type    | Required | Description                                                                                         |
|-------------------|---------|----------|-----------------------------------------------------------------------------------------------------|
| `synthetic_index` | String  | Yes      | Synthetic index name (or symbol). Accepted values depend on `CHOICES` defined in `instrument_map`.  |
| `account_balance` | Decimal | Yes      | The user's account balance in USD, with a maximum of 10 digits and 2 decimal places.                |
| `entry_price`     | Decimal | Yes      | The entry price of the trade, up to 10 digits with 5 decimal places.                                |
| `stop_price`      | Decimal | Yes      | The stop price for the trade, up to 10 digits with 5 decimal places.                                |
| `risk_percent`    | Decimal | Yes      | The percentage of the account balance that the user is willing to risk on the trade.                |

---

### Response Fields

Upon a successful request, the API returns the following calculated fields:

| Field            | Type    | Description                                                            |
|------------------|---------|------------------------------------------------------------------------|
| `synthetic_index`| String  | Synthetic index specified in the request.                              |
| `account_balance`| Decimal | Account balance specified in the request.                              |
| `entry_price`    | Decimal | Entry price specified in the request.                                  |
| `stop_price`     | Decimal | Stop price specified in the request.                                   |
| `risk_percent`   | Decimal | Risk percentage specified in the request.                              |
| `lot`            | Decimal | Calculated lot size for the trade, with up to 3 decimal places.        |
| `num_pips`       | Decimal | Calculated number of pips for the trade, with up to 5 decimal places.  |
| `total_risk`     | Decimal | Calculated total risk in USD, with up to 2 decimal places.             |

---

### Example Request

```json
POST /api/risk-calculation/

{
    "synthetic_index": "Volatility 75",
    "account_balance": 1000.00,
    "entry_price": 1500.12345,
    "stop_price": 1490.12345,
    "risk_percent": 2.00
}
```

### Example Response

```json
{
    "synthetic_index": "Volatility 75",
    "account_balance": 1000.00,
    "entry_price": 1500.12345,
    "stop_price": 1490.12345,
    "risk_percent": 2.00,
    "lot": 0.100,
    "num_pips": 10.00000,
    "total_risk": 20.00
}
```

### Error Responses

If an error occurs (e.g., invalid input data), the API will return a 400 Bad Request status with error details.

#### Example Error Response

```json
{
    "account_balance": [
        "A valid number is required."
    ],
    "risk_percent": [
        "Ensure this value is greater than 0."
    ]
}
```

### Notes

- **Authentication**: This API does not require authentication. Add authentication if needed for secure access.

---

This documentation should help any developers integrate and use the API effectively. Contact me if you'd like any additional information added!
