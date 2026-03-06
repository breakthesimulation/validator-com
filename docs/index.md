---
title: Introduction
description: Validator.com API Documentation
---

# Validator.com API

API endpoint for fetching Solana validator data.

## Base URL

```
https://validator.com/api
```

## Endpoints

### Get Validators

```bash
GET /data/validators.json
```

Returns list of top validators with detailed metrics.

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| name | string | Validator name |
| commission | number | Commission rate (0-100) |
| stake_sol | number | Total stake in SOL (millions) |
| apy | number | Annual percentage yield |
| uptime | number | Uptime percentage |
| epoch | number | Current epoch |
| rank | number | Validator rank by stake |
| deliquency | boolean | Whether validator is delinquent |

### Get Validator Details

```bash
GET /api/validator/{name}
```

Returns detailed info for a specific validator.

### Get Market Stats

```bash
GET /api/stats
```

Returns network-wide statistics.

## Example Response

```json
{
  "validators": [
    {
      "name": "ParaFi Technologies",
      "commission": 0,
      "stake_sol": 0.13,
      "apy": 6.13,
      "uptime": 100,
      "epoch": 636,
      "rank": 1,
      "delinquency": false
    }
  ],
  "network_stats": {
    "total_stake": 450000000,
    "validator_count": 1850,
    "avg_apy": 6.2
  }
}
```

## Rate Limits

- 100 requests per minute for public endpoints
- 1000 requests per minute for authenticated endpoints

## Authentication

Some endpoints require an API key. Include in header:

```
X-API-Key: your-api-key
```

## SDK Examples

### Python

```python
import requests

resp = requests.get("https://validator.com/data/validators.json")
validators = resp.json()
for v in validators["validators"]:
    print(f"{v['name']}: {v['apy']}% APY")
```

### JavaScript

```javascript
fetch('https://validator.com/data/validators.json')
  .then(r => r.json())
  .then(data => {
    data.validators.forEach(v => {
      console.log(`${v.name}: ${v.apy}% APY`);
    });
  });
```

## Support

- Email: support@validator.com
- Discord: https://discord.gg/validatorcom
