---
title: Introduction
description: Validator.com API Documentation
---

# Welcome to Validator.com

API endpoint for fetching Solana validator data.

## Endpoints

### Get Validators

```bash
GET /data/validators.json
```

Returns list of top validators with:
- name
- commission
- stake_sol (millions)
- apy
- uptime

### Example Response

```json
{
  "validators": [
    {
      "name": "ParaFi Technologies",
      "commission": 0,
      "stake_sol": 0.13,
      "apy": 6.13,
      "uptime": 100
    }
  ]
}
```
