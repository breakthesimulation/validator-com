#!/usr/bin/env python3
"""Update validator.com landing page with fresh data from validators.json"""
import json
from datetime import datetime

VALIDATORS_FILE = "/home/openclaw/vault/Dev/validator-com/validators.json"
INDEX_FILE = "/home/openclaw/vault/Dev/validator-com/docs/index.md"

def generate_table_row(v, rank):
    """Generate a table row for a validator"""
    name_link = f"[{v['name']}](/docs/validators/{v['name'].lower().replace(' ', '-').replace('|', '-').replace('🔥', '').replace('🤟', '').replace('💥', '').replace('⭐', '')})"
    jito = "✅" if v.get('is_jito') else "❌"
    return f"| {rank} | {name_link} | {v['commission']}% | {v['stake_sol']:,.0f} SOL | {v['apy']:.2f}% | {v['uptime']:.1f}% | {jito} |"

def main():
    # Load validators
    with open(VALIDATORS_FILE) as f:
        data = json.load(f)
    
    validators = data.get("validators", [])[:10]  # Top 10
    
    # Generate table rows
    rows = []
    for i, v in enumerate(validators, 1):
        rows.append(generate_table_row(v, i))
    
    table = "\n".join(rows)
    
    # Read current index.md
    with open(INDEX_FILE) as f:
        content = f.read()
    
    # Replace the table (between "## Top Validators" and the next ##)
    import re
    
    # Pattern to find the table section
    pattern = r'(\| # \| Validator \| Commission \| Stake \| APY \| Uptime \| Jito \|.*?)\n\|(?: -+ \|)+\|.*?(\n## Why Validator)'
    
    replacement = f"""\| # | Validator | Commission | Stake | APY | Uptime | Jito |
|---|-----------|------------|-------|-----|--------|------|
{table}

## Why Validator"""
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Update the "Last updated" date
    new_content = new_content.replace(
        "Last updated: March 8, 2026",
        f"Last updated: {datetime.now().strftime('%B %d, %Y')}"
    )
    
    # Write updated content
    with open(INDEX_FILE, "w") as f:
        f.write(new_content)
    
    print(f"✅ Updated index.md with top 10 validators")
    print(f"📅 Updated date to {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()