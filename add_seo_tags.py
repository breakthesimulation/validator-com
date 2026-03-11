#!/usr/bin/env python3
"""
Add SEO meta tags to validator.com docs
"""
import os
import re

DOCS_DIR = "/home/openclaw/public/validator/docs"

# SEO data for each page
SEO_DATA = {
    "what-is-a-validator.html": {
        "title": "What is a Solana Validator? | Complete Guide 2026",
        "description": "Learn what a Solana validator does, how the network achieves consensus, and why validators are essential to blockchain infrastructure.",
    },
    "what-is-a-validator-full.html": {
        "title": "Solana Validator Guide: Full Technical Deep Dive",
        "description": "Comprehensive technical guide to Solana validators,Proof of History, consensus mechanisms, and network security.",
    },
    "proof-of-history.html": {
        "title": "Proof of History Explained | Solana Validator Technology",
        "description": "Understand Proof of History and how Solana validators use it to achieve 65,000 TPS. Technical explanation for validators.",
    },
    "hardware-requirements.html": {
        "title": "Solana Validator Hardware Requirements 2026",
        "description": "Minimum and recommended hardware specifications for running a Solana validator. CPU, RAM, storage, and network requirements.",
    },
    "running-your-own-validator.html": {
        "title": "How to Run a Solana Validator | Step-by-Step Guide",
        "description": "Complete tutorial on setting up and running your own Solana validator. From server setup to stake management.",
    },
    "validator-roi.html": {
        "title": "Solana Validator ROI & Earnings | 2026 projections",
        "description": "Calculate your potential returns as a Solana validator. Stake rewards, commission rates, and operational costs explained.",
    },
    "staking-rewards.html": {
        "title": "Solana Staking Rewards Guide | Validator.com",
        "description": "How Solana staking rewards work. Understand APY, validator commission, and how to maximize staking returns.",
    },
    "solana-vs-ethereum.html": {
        "title": "Solana vs Ethereum Validators | Network Comparison",
        "description": "Compare Solana and Ethereum validator systems. Proof of Stake vs Proof of History, TPS, and infrastructure differences.",
    },
    "choose-validator.html": {
        "title": "How to Choose a Solana Validator | Staking Guide",
        "description": "Guide to selecting the best Solana validator for staking. Commission, uptime, decentralization, and security factors.",
    },
    "mev-validators.html": {
        "title": "MEV on Solana | Validator Max Extractable Value",
        "description": "Understanding Max Extractable Value (MEV) in Solana. How validators capture MEV opportunities and impact on network.",
    },
}

def add_seo_tags(html_file, seo_info):
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Check if already has og:title
    if 'og:title' in content:
        print(f"  Already has SEO: {os.path.basename(html_file)}")
        return
    
    # Build SEO meta tags
    seo_tags = f'''  <meta name="description" content="{seo_info['description']}">
  <meta property="og:title" content="{seo_info['title']}">
  <meta property="og:description" content="{seo_info['description']}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://validator.com/docs/{os.path.basename(html_file)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{seo_info['title']}">
  <meta name="twitter:description" content="{seo_info['description']}">'''
    
    # Insert after <title> tag
    pattern = r'(<title>[^<]+</title>)'
    replacement = r'\1\n  ' + seo_tags
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    with open(html_file, 'w') as f:
        f.write(new_content)
    
    print(f"  Added SEO: {os.path.basename(html_file)}")

def main():
    print("Adding SEO meta tags to validator docs...")
    
    for filename, seo_info in SEO_DATA.items():
        filepath = os.path.join(DOCS_DIR, filename)
        if os.path.exists(filepath):
            add_seo_tags(filepath, seo_info)
        else:
            print(f"  File not found: {filename}")
    
    print("Done!")

if __name__ == "__main__":
    main()
