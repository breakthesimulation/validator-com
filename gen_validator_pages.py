#!/usr/bin/env python3
"""Generate SEO pages for each validator."""
import json
from datetime import datetime

with open("/home/openclaw/vault/Dev/validator-com/validators.json") as f:
    data = json.load(f)

validators = data["validators"]
output_dir = "/home/openclaw/vault/Dev/validator-com/docs/validators"

for v in validators:
    name = v["name"]
    slug = name.lower().replace(" ", "-").replace("|", "-").replace("🔥", "").replace("🤟", "").replace("💥", "").replace("⭐", "")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")
    
    content = f"""---
title: {name} - Solana Validator Review
description: Stake your SOL with {name}. Commission: {v['commission']}%, APY: {v['apy']:.2f}%, Stake: {v['stake_sol']:,.0f} SOL. Uptime: {v['uptime']:.2f}%.
---

# {name}

## Validator Details

| Metric | Value |
|--------|-------|
| **Name** | {name} |
| **Commission** | {v['commission']}% |
| **Stake Amount** | {v['stake_sol']:,.0f} SOL (${v['stake_millions']:.1f}M) |
| **APY** | {v['apy']:.2f}% |
| **Uptime** | {v['uptime']:.2f}% |
| **Jito Enabled** | {'Yes' if v['is_jito'] else 'No'} |
| **Delinquent** | {'Yes ⚠️' if v['delinquent'] else 'No'} |
| **Rank** | #{v['rank']} |

## Why Stake with {name}?

"""

    # Add commentary based on stats
    if v["commission"] == 0:
        content += "- **0% Commission** - Maximize your staking rewards\n"
    if v["is_jito"]:
        content += "- **Jito MEV** - Additional yield from MEV capture\n"
    if v["uptime"] > 99.5:
        content += "- **High Uptime** - Reliable validator performance\n"
    if v["delinquent"]:
        content += "⚠️ **Warning**: This validator is currently delinquent. Consider a different validator.\n"
    
    content += f"""
## Estimated Rewards

Staking **100 SOL** with {name} at {v['apy']:.2f}% APY:

- **Monthly**: ~{100 * v['apy'] / 12:.2f} SOL
- **Yearly**: ~{100 * v['apy'] / 100:.2f} SOL

## How to Stake

1. Choose {name} from your wallet's validator list
2. Select the amount of SOL to stake
3. Confirm your delegation

## Related Validators

[View all validators →](/validators)

---
*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    filename = f"{output_dir}/{slug}.md"
    with open(filename, "w") as f:
        f.write(content)
    print(f"Created: {filename}")
