import requests, json
from datetime import datetime

try:
    r = requests.get("https://api.stakewiz.com/validators", timeout=30)
    data = r.json()
    
    validators = []
    for v in data[:100]:
        validators.append({
            "name": v.get("name", v.get("identity", "Unknown")[:12]),
            "commission": v.get("commission", 0),
            "stake_sol": round(v.get("activated_stake", 0), 2),
            "stake_millions": round(v.get("activated_stake", 0) / 1e6, 2),
            "apy": v.get("apy_estimate", 0),
            "uptime": v.get("uptime", 0),
            "delinquent": v.get("delinquent", False),
            "rank": v.get("rank", 0),
            "is_jito": v.get("is_jito", False),
        })
    
    out = {"timestamp": datetime.now().isoformat(), "validators": validators}
    
    with open("/home/openclaw/public/data/validators.json", "w") as f:
        json.dump(out, f, indent=2)
    
    print(f"Got {len(validators)} validators")
    for v in validators[:5]:
        print(f"  {v['name']}: {v['stake_sol']:,.0f} SOL")

except requests.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"Error: {e}")
