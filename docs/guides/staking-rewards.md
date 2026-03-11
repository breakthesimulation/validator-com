---
title: Understanding Staking Rewards
description: Learn how Solana staking rewards are calculated. Understand APY, epoch rewards, compound interest, and how to maximize your returns.
---

# Understanding Staking Rewards

Staking rewards are the key benefit of delegating your SOL to validators. This guide explains how they work and how to maximize them.

## How Solana Rewards Work

### The Basics

Solana produces new tokens every epoch (~2 days) as inflation. These tokens are distributed to validators and their delegators based on stake weight.

**Current inflation rate:** ~5-7% annually

### Reward Distribution

```
Total Rewards = (Epoch Inflation × Validator's Stake Weight) - Validator Commission
```

Your share = Total Rewards × (Your Stake ÷ Total Validator Stake)

## Key Metrics Explained

### APY (Annual Percentage Yield)

APY accounts for compound interest. The formula:

```
APY = (1 + r/n)^n - 1

Where:
r = annual interest rate (as decimal)
n = number of compounding periods per year
```

For Solana, rewards compound every epoch (~26 epochs/year).

### Effective APY

Your actual return after validator commission:

```
Effective APY = Stated APY × (1 - Commission%)
```

**Example:**
- Validator APY: 6%
- Commission: 5%
- Your Effective APY: 6% × 0.95 = 5.7%

### Why 0% Commission Matters

| Commission | 6% APY Validator | Difference |
|------------|------------------|------------|
| 0% | 6.00% | Baseline |
| 5% | 5.70% | -5% |
| 10% | 5.40% | -10% |

On 1,000 SOL staked:
- 0% commission: 60 SOL/year
- 10% commission: 54 SOL/year
- **Difference: 6 SOL/year** 💰

## Jito MEV Rewards

### What is MEV?

Maximum Extractable Value (MEV) is extra value captured from transaction ordering. Validators with Jito:

1. Bundle transactions for optimal ordering
2. Capture arbitrage opportunities
3. Share MEV profits with stakers

### Extra Rewards

Jito validators typically add **1-3% additional APY**:

| Validator Type | Base APY | + Jito MEV | Total |
|-----------------|----------|------------|-------|
| Standard | 6% | 0% | 6% |
| Jito Enabled | 6% | 1.5% | 7.5% |

**Jito can increase your rewards by 25%+!**

## Reward Calculation Examples

### Example 1: 100 SOL Staked

```
Stake: 100 SOL
Validator APY: 6.14%
Commission: 0%
Jito: Yes (+1.5%)

Year 1: 100 × 0.0714 = 7.14 SOL
Year 5 (compounded): ~41 SOL total
```

### Example 2: 1,000 SOL Staked

```
Stake: 1,000 SOL
Validator APY: 6.14%
Commission: 5%
Jito: Yes

Year 1: 1000 × 0.065 = 65 SOL
Year 5 (compounded): ~370 SOL total
```

### Example 3: 10,000 SOL Staked

```
Stake: 10,000 SOL  
Validator APY: 6.14%
Commission: 0%
Jito: Yes

Year 1: 10,000 × 0.0714 = 714 SOL
Year 5 (compounded): ~4,100 SOL total
```

## Reward Timeline

### When Do Rewards Start?

- **Staking:** Immediate
- **First rewards:** ~2-4 days (after 2 epochs)
- **Claimable:** Every ~2 days thereafter

### How to Claim

Most wallets auto-claim:

1. Phantom: Automatic
2. Solflare: Automatic  
3. Ledger: Manual claim in Solflare

### Unstaking

- **Deactivation:** Instant (no new rewards)
- **Liquid:** 2-3 epochs (~1-2 days)
- **Transferable:** Once liquid

## Maximizing Your Rewards

### Strategy 1: 0% Commission + Jito

**Best for:** Maximum returns

```
Validator selection:
- Commission: 0%
- Jito: Enabled
- Uptime: 99.9%+

Expected APY: 7-8%
```

### Strategy 2: Compound Re-staking

**Best for:** Long-term growth

```
Year 1: Stake 100 SOL → earn 7 SOL
Year 2: Stake 107 SOL → earn 7.5 SOL
Year 3: Stake 114.5 SOL → earn 8 SOL
```

### Strategy 3: Diversification

**Best for:** Risk management

```
Split 1000 SOL:
- 500 SOL: Top 0% commission validator
- 300 SOL: Medium stake validator
- 200 SOL: Small community validator
```

## Tax Implications

Staking rewards are generally:

- **Taxable income** in most jurisdictions
- **FIFO accounting** recommended
- **Track all transactions** for reporting

*Consult a tax professional for your specific situation.*

## Common Questions

### Why did my rewards decrease?

Possible causes:
- Validator changed commission
- Network inflation adjustment
- Validator uptime issues

### Can I stake from an exchange?

Some exchanges offer staking, but:
- Less control
- Higher fees
- Custodial risks

**We recommend self-custody staking.**

### What if the validator gets slashed?

- You don't lose principal
- Only lose potential rewards during downtime
- Consider switching validators

## Summary

| Factor | Impact on Rewards |
|--------|------------------|
| 0% commission | +5-10% |
| Jito MEV | +15-25% |
| High uptime | +1-2% |
| Compounding | +10-20%/year |

**Optimal strategy:** Choose 0% commission + Jito validator, compound rewards annually.

[Start earning →](/docs/guides/how-to-stake-sol)
