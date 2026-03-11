<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Stats | validator.com</title>
    <meta name="description" content="Real-time blockchain network statistics for Solana, Ethereum, Cosmos and more. Track total staked, validator counts, APY, and network health.">
    <link rel="canonical" href="https://validator.com/network-stats.html">
    <style>
        :root {
            --bg-primary: #0a0a0f;
            --bg-secondary: #12121a;
            --bg-card: #1a1a24;
            --text-primary: #ffffff;
            --text-secondary: #a0a0b0;
            --accent: #00d4aa;
            --accent-dim: #00a88a;
            --border: #2a2a3a;
            --solana: #9945ff;
            --ethereum: #627eea;
            --cosmos: #2e3148;
            --polygon: #8247e5;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 2rem;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent);
            text-decoration: none;
        }
        
        nav a {
            color: var(--text-secondary);
            text-decoration: none;
            margin-left: 2rem;
            transition: color 0.2s;
        }
        
        nav a:hover { color: var(--accent); }
        
        h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }
        
        .network-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }
        
        .network-card {
            background: var(--bg-card);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--border);
        }
        
        .network-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .network-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: 700;
        }
        
        .network-icon.solana { background: linear-gradient(135deg, #9945ff, #14f195); }
        .network-icon.ethereum { background: linear-gradient(135deg, #627eea, #8c9eff); }
        .network-icon.cosmos { background: linear-gradient(135deg, #2e3148, #4a5568); }
        .network-icon.polygon { background: linear-gradient(135deg, #8247e5, #a78bfa); }
        
        .network-name {
            font-size: 1.25rem;
            font-weight: 600;
        }
        
        .network-tag {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        
        .stat-item {
            background: var(--bg-secondary);
            padding: 0.75rem;
            border-radius: 8px;
        }
        
        .stat-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            margin-bottom: 0.25rem;
        }
        
        .stat-value {
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        .stat-value.accent { color: var(--accent); }
        
        .stat-value.warning { color: #ffaa00; }
        
        .stat-value.danger { color: #ff4757; }
        
        .update-time {
            text-align: center;
            margin-top: 2rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        footer {
            margin-top: 4rem;
            padding: 2rem 0;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        footer a {
            color: var(--accent);
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <a href="/" class="logo">validator.com</a>
            <nav>
                <a href="/">Trackers</a>
                <a href="/calculator.html">Calculator</a>
                <a href="/network-stats.html" class="active">Stats</a>
                <a href="/guides/">Guides</a>
            </nav>
        </header>
        
        <h1>Network Stats</h1>
        <p class="subtitle">Real-time blockchain network statistics. Last updated: March 11, 2026</p>
        
        <div class="network-grid">
            <div class="network-card">
                <div class="network-header">
                    <div class="network-icon solana">S</div>
                    <div>
                        <div class="network-name">Solana</div>
                        <div class="network-tag">Proof of Stake</div>
                    </div>
                </div>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-label">Total Staked</div>
                        <div class="stat-value">4.2B SOL</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Validators</div>
                        <div class="stat-value">2,450</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Current APY</div>
                        <div class="stat-value accent">5.89%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Token Price</div>
                        <div class="stat-value">$175.00</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Inflation</div>
                        <div class="stat-value">5.0%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Stake Rate</div>
                        <div class="stat-value accent">72%</div>
                    </div>
                </div>
            </div>
            
            <div class="network-card">
                <div class="network-header">
                    <div class="network-icon ethereum">E</div>
                    <div>
                        <div class="network-name">Ethereum</div>
                        <div class="network-tag">Proof of Stake</div>
                    </div>
                </div>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-label">Total Staked</div>
                        <div class="stat-value">33.2M ETH</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Validators</div>
                        <div class="stat-value">1,037,500</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Current APY</div>
                        <div class="stat-value accent">3.20%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Token Price</div>
                        <div class="stat-value">$2,450</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Issuance</div>
                        <div class="stat-value">0.54%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Stake Rate</div>
                        <div class="stat-value">28%</div>
                    </div>
                </div>
            </div>
            
            <div class="network-card">
                <div class="network-header">
                    <div class="network-icon cosmos">C</div>
                    <div>
                        <div class="network-name">Cosmos</div>
                        <div class="network-tag">Proof of Stake</div>
                    </div>
                </div>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-label">Total Staked</div>
                        <div class="stat-value">190M ATOM</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Validators</div>
                        <div class="stat-value">180</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Current APY</div>
                        <div class="stat-value accent">14.5%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Token Price</div>
                        <div class="stat-value">$8.50</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Inflation</div>
                        <div class="stat-value">9.2%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Stake Rate</div>
                        <div class="stat-value accent">66%</div>
                    </div>
                </div>
            </div>
            
            <div class="network-card">
                <div class="network-header">
                    <div class="network-icon polygon">P</div>
                    <div>
                        <div class="network-name">Polygon</div>
                        <div class="network-tag">Proof of Stake</div>
                    </div>
                </div>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-label">Total Staked</div>
                        <div class="stat-value">3.4B MATIC</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Validators</div>
                        <div class="stat-value">3,200</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Current APY</div>
                        <div class="stat-value accent">4.8%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Token Price</div>
                        <div class="stat-value">$0.45</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Inflation</div>
                        <div class="stat-value">4.5%</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">Stake Rate</div>
                        <div class="stat-value">35%</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="update-time">
            Data refreshed every 15 minutes from mainnet APIs
        </div>
        
        <footer>
            <p>© 2026 <a href="/">validator.com</a> — Compare and choose the best validators</p>
        </footer>
    </div>
</body>
</html>
