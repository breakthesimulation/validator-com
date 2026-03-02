#!/usr/bin/env python3
"""
Live Solana Validator Data Fetcher - FIXED
"""
import json, requests
from datetime import datetime

OUTPUT_FILE = "/home/openclaw/vault/Dev/validator-com/validators-live.json"

def get_validators():
    """Fetch from Stakewiz API - it's a LIST not dict"""
    try:
        r = requests.get("https://api.stakewiz.com/validators", timeout=30)
        data = r.json()
        
        # Stakewiz returns a LIST, iterate it
        validators = []
        for v in data[:20]:  # Top 20
            validators.append({
                "identity": v.get("identity", ""),
                "name": v.get("name", v.get("identity", "")[:12]),
                "commission": v.get("commission", 0),
                "activeStake": v.get("activeStake", 0) / 1e9,  # Convert to SOL
                "apy": v.get("apy_estimate", v.get("apy", 0)),
                "uptime": v.get("uptime_pct", v.get("skip_rate", 0)),
                "dataCenter": v.get("dataCenter", ""),
            })
        
        print(f"✅ Stakewiz: Got {len(validators)} validators")
        return validators
    except Exception as e:
        print(f"❌ Stakewiz error: {e}")
        return []

def render_markdown(validators):
    """Render markdown table"""
    md = """# Top 20 Solana Validators

| # | Validator | Commission | Stake (SOL) | APY | Uptime |
|------|-----------|-------------|--------------|-----|---------|
"""
    for i, v in enumerate(validators, 1):
        name = v.get("name", v.get("identity", "Unknown")[:12])
        commission = v.get("commission", 0)
        stake = v.get("activeStake", 0)
        apy = v.get("apy", 0)
        uptime = v.get("uptime", 0)
        md += f"| {i} | {name} | {commission}% | {stake:,.0f} | {apy}% | {uptime}% |\n"
    return md

def main():
    print("🔍 Fetching Solana validators...")
    validators = get_validators()
    
    if not validators:
        print("❌ No data")
        return
    
    # Save JSON - FIX: ensure 20 entries
    output = {
        "timestamp": datetime.now().isoformat(),
        "source": "stakewiz",
        "validators": validators
    }
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✅ Saved {len(validators)} validators to {OUTPUT_FILE}")
    print(render_markdown(validators))

if __name__ == "__main__":
    main()
