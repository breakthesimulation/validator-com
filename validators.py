#!/usr/bin/env python3
"""Fixed validator data fetcher"""
import requests, json
from datetime import datetime

OUTPUT = "/home/openclaw/vault/Dev/validator-com/validators.json"

def main():
    r = requests.get("https://api.stakewiz.com/validators", timeout=30)
    data = r.json()
    
    validators = []
    for v in data[:20]:
        validators.append({
            "name": v.get("name", v.get("identity", "Unknown")[:12]),
            "commission": v.get("commission", 0),
            "stake_sol": round(v.get("activeStake", 0) / 1e9, 0),
            "apy": v.get("apy_estimate", 0),
            "uptime": v.get("uptime_pct", 0),
        })
    
    with open(OUTPUT, "w") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "validators": validators}, f, indent=2)
    
    print(f"✅ Saved {len(validators)} validators")

if __name__ == "__main__":
    main()
