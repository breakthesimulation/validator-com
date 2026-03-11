<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Staking ROI Calculator | validator.com</title>
    <meta name="description" content="Calculate your staking returns across Solana, Ethereum, and other networks. Compare validators and maximize your staking rewards.">
    <link rel="canonical" href="https://validator.com/calculator.html">
    <meta property="og:title" content="Staking ROI Calculator | validator.com">
    <meta property="og:description" content="Calculate your staking returns across multiple blockchain networks">
    <meta property="og:type" content="website">
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
            --success: #00d4aa;
            --warning: #ffaa00;
            --danger: #ff4757;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
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
        
        nav a:hover, nav a.active {
            color: var(--accent);
        }
        
        .hero {
            text-align: center;
            padding: 3rem 0;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--text-primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            color: var(--text-secondary);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .calculator-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-top: 2rem;
        }
        
        @media (max-width: 768px) {
            .calculator-grid {
                grid-template-columns: 1fr;
            }
        }
        
        .card {
            background: var(--bg-card);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--border);
        }
        
        .card h2 {
            font-size: 1.25rem;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
        }
        
        .form-group {
            margin-bottom: 1.25rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        input, select {
            width: 100%;
            padding: 0.75rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 1rem;
            transition: border-color 0.2s;
        }
        
        input:focus, select:focus {
            outline: none;
            border-color: var(--accent);
        }
        
        .input-with-suffix {
            position: relative;
        }
        
        .input-with-suffix input {
            padding-right: 3rem;
        }
        
        .input-suffix {
            position: absolute;
            right: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        .btn {
            background: var(--accent);
            color: var(--bg-primary);
            border: none;
            padding: 0.875rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s, transform 0.1s;
        }
        
        .btn:hover {
            background: var(--accent-dim);
        }
        
        .btn:active {
            transform: scale(0.98);
        }
        
        .results-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        
        .result-item {
            background: var(--bg-secondary);
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
        }
        
        .result-label {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
        }
        
        .result-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent);
        }
        
        .result-value.warning {
            color: var(--warning);
        }
        
        .result-value.danger {
            color: var(--danger);
        }
        
        .breakdown {
            margin-top: 1.5rem;
        }
        
        .breakdown-item {
            display: flex;
            justify-content: space-between;
            padding: 0.75rem 0;
            border-bottom: 1px solid var(--border);
        }
        
        .breakdown-item:last-child {
            border-bottom: none;
        }
        
        .breakdown-label {
            color: var(--text-secondary);
        }
        
        .breakdown-value {
            font-weight: 600;
        }
        
        .comparison {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
        }
        
        .comparison h3 {
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }
        
        .validator-select {
            margin-bottom: 1rem;
        }
        
        .apy-badge {
            display: inline-block;
            background: var(--accent);
            color: var(--bg-primary);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-left: 0.5rem;
        }
        
        .disclaimer {
            margin-top: 2rem;
            padding: 1rem;
            background: var(--bg-secondary);
            border-radius: 8px;
            font-size: 0.85rem;
            color: var(--text-secondary);
        }
        
        .chart-container {
            margin-top: 1.5rem;
            height: 200px;
            background: var(--bg-secondary);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
        }
        
        .compound-table {
            width: 100%;
            margin-top: 1rem;
            border-collapse: collapse;
        }
        
        .compound-table th, .compound-table td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        
        .compound-table th {
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 0.85rem;
        }
        
        .compound-table td {
            font-size: 0.95rem;
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
                <a href="/calculator.html" class="active">Calculator</a>
                <a href="/guides/">Guides</a>
            </nav>
        </header>
        
        <section class="hero">
            <h1>Staking ROI Calculator</h1>
            <p class="subtitle">Calculate your staking returns across Solana, Ethereum, and other networks. Compare validators and maximize your rewards.</p>
        </section>
        
        <div class="calculator-grid">
            <div class="card">
                <h2>Stake Details</h2>
                <div class="form-group">
                    <label for="network">Network</label>
                    <select id="network">
                        <option value="solana">Solana</option>
                        <option value="ethereum">Ethereum</option>
                        <option value="cosmos">Cosmos</option>
                        <option value="polygon">Polygon</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="validator">Validator (Optional)</label>
                    <select id="validator" class="validator-select">
                        <option value="">-- Network Average --</option>
                        <option value="parafi">ParaFi Technologies (0% comm, 6.13% APY)</option>
                        <option value="limechain">LimeChain (8% comm, 5.64% APY)</option>
                        <option value="solyrae">SoLyrae (5% comm, 5.89% APY)</option>
                        <option value="l0vd">L0vd (0% comm, 6.13% APY)</option>
                        <option value="jito">Jito (0% comm + MEV, ~6.5% APY)</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="stakeAmount">Stake Amount</label>
                    <div class="input-with-suffix">
                        <input type="number" id="stakeAmount" value="1000" min="1" step="1">
                        <span class="input-suffix" id="tokenSymbol">SOL</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="tokenPrice">Token Price</label>
                    <div class="input-with-suffix">
                        <input type="number" id="tokenPrice" value="175.00" min="0.01" step="0.01">
                        <span class="input-suffix">USD</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="commission">Validator Commission</label>
                    <div class="input-with-suffix">
                        <input type="number" id="commission" value="0" min="0" max="100" step="1">
                        <span class="input-suffix">%</span>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="stakingPeriod">Staking Period</label>
                    <select id="stakingPeriod">
                        <option value="1">1 Year</option>
                        <option value="2">2 Years</option>
                        <option value="3">3 Years</option>
                        <option value="5">5 Years</option>
                    </select>
                </div>
                
                <button class="btn" onclick="calculate()">Calculate Returns</button>
            </div>
            
            <div class="card">
                <h2>Your Returns</h2>
                <div class="results-grid">
                    <div class="result-item">
                        <div class="result-label">APY</div>
                        <div class="result-value" id="resultAPY">6.13%</div>
                    </div>
                    <div class="result-item">
                        <div class="result-label">Total Rewards</div>
                        <div class="result-value" id="resultRewards">61.3 SOL</div>
                    </div>
                    <div class="result-item">
                        <div class="result-label">Final Balance</div>
                        <div class="result-value" id="resultBalance">1,061 SOL</div>
                    </div>
                    <div class="result-item">
                        <div class="result-label">USD Value</div>
                        <div class="result-value" id="resultUSD">$185,675</div>
                    </div>
                </div>
                
                <div class="breakdown">
                    <div class="breakdown-item">
                        <span class="breakdown-label">Initial Stake</span>
                        <span class="breakdown-value" id="breakdownInitial">1,000 SOL</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-label">Gross Rewards</span>
                        <span class="breakdown-value" id="breakdownGross">+61.3 SOL</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-label">Commission (0%)</span>
                        <span class="breakdown-value" id="breakdownCommission">-0 SOL</span>
                    </div>
                    <div class="breakdown-item">
                        <span class="breakdown-label">Net Rewards</span>
                        <span class="breakdown-value" id="breakdownNet" style="color: var(--accent)">+61.3 SOL</span>
                    </div>
                </div>
                
                <div class="comparison">
                    <h3>Compound Growth Projection</h3>
                    <table class="compound-table">
                        <thead>
                            <tr>
                                <th>Period</th>
                                <th>Balance</th>
                                <th>Rewards</th>
                            </tr>
                        </thead>
                        <tbody id="compoundBody">
                            <!-- Populated by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <div class="disclaimer">
            <strong>Disclaimer:</strong> These calculations are estimates based on current APY and do not account for token price changes, network upgrades, or slashing events. Staking involves risk including potential loss of funds. Always do your own research before staking.
        </div>
        
        <footer>
            <p>© 2026 <a href="/">validator.com</a> — Compare and choose the best validators</p>
        </footer>
    </div>
    
    <script>
        const NETWORK_DATA = {
            solana: { token: 'SOL', avgApy: 5.89, defaultPrice: 175.00 },
            ethereum: { token: 'ETH', avgApy: 3.20, defaultPrice: 2450.00 },
            cosmos: { token: 'ATOM', avgApy: 14.50, defaultPrice: 8.50 },
            polygon: { token: 'MATIC', avgApy: 4.80, defaultPrice: 0.45 }
        };
        
        const VALIDATOR_DATA = {
            parafi: { apy: 6.13, commission: 0 },
            limechain: { apy: 5.64, commission: 8 },
            solyrae: { apy: 5.89, commission: 5 },
            l0vd: { apy: 6.13, commission: 0 },
            jito: { apy: 6.50, commission: 0 }
        };
        
        document.getElementById('network').addEventListener('change', function() {
            const network = this.value;
            const data = NETWORK_DATA[network];
            document.getElementById('tokenSymbol').textContent = data.token;
            document.getElementById('tokenPrice').value = data.defaultPrice;
            calculate();
        });
        
        document.getElementById('validator').addEventListener('change', function() {
            const validator = this.value;
            if (validator && VALIDATOR_DATA[validator]) {
                const data = VALIDATOR_DATA[validator];
                document.getElementById('commission').value = data.commission;
            }
            calculate();
        });
        
        ['stakeAmount', 'tokenPrice', 'commission', 'stakingPeriod'].forEach(id => {
            document.getElementById(id).addEventListener('input', calculate);
            document.getElementById(id).addEventListener('change', calculate);
        });
        
        function calculate() {
            const network = document.getElementById('network').value;
            const validator = document.getElementById('validator').value;
            const stakeAmount = parseFloat(document.getElementById('stakeAmount').value) || 0;
            const tokenPrice = parseFloat(document.getElementById('tokenPrice').value) || 0;
            const commission = parseFloat(document.getElementById('commission').value) || 0;
            const years = parseInt(document.getElementById('stakingPeriod').value) || 1;
            
            // Get APY
            let apy;
            if (validator && VALIDATOR_DATA[validator]) {
                apy = VALIDATOR_DATA[validator].apy;
            } else {
                apy = NETWORK_DATA[network].avgApy;
            }
            
            // Adjust for commission
            const netApy = apy * (1 - commission / 100);
            
            // Calculate rewards
            const dailyRate = netApy / 100 / 365;
            const dailyRewards = stakeAmount * dailyRate;
            const yearlyRewards = stakeAmount * netApy / 100;
            
            // Compound calculation
            const periods = years * 12; // monthly compounding
            const monthlyRate = netApy / 100 / 12;
            const finalBalance = stakeAmount * Math.pow(1 + monthlyRate, periods);
            const totalRewards = finalBalance - stakeAmount;
            const finalUSD = finalBalance * tokenPrice;
            
            // Update display
            document.getElementById('resultAPY').textContent = netApy.toFixed(2) + '%';
            document.getElementById('resultRewards').textContent = totalRewards.toFixed(1) + ' ' + NETWORK_DATA[network].token;
            document.getElementById('resultBalance').textContent = finalBalance.toFixed(0) + ' ' + NETWORK_DATA[network].token;
            document.getElementById('resultUSD').textContent = '$' + finalUSD.toLocaleString('en-US', { maximumFractionDigits: 0 });
            
            // Breakdown
            const grossRewards = stakeAmount * apy / 100;
            const commissionAmount = grossRewards * (commission / 100);
            
            document.getElementById('breakdownInitial').textContent = stakeAmount.toLocaleString() + ' ' + NETWORK_DATA[network].token;
            document.getElementById('breakdownGross').textContent = '+' + grossRewards.toFixed(1) + ' ' + NETWORK_DATA[network].token;
            document.getElementById('breakdownCommission').textContent = '-' + commissionAmount.toFixed(1) + ' ' + NETWORK_DATA[network].token;
            document.getElementById('breakdownNet').textContent = '+' + totalRewards.toFixed(1) + ' ' + NETWORK_DATA[network].token;
            
            // Compound table
            const compoundBody = document.getElementById('compoundBody');
            compoundBody.innerHTML = '';
            
            const periodsToShow = [1, 6, 12, 24, 36, 60];
            periodsToShow.forEach(months => {
                if (months <= periods) {
                    const balance = stakeAmount * Math.pow(1 + monthlyRate, months);
                    const rewards = balance - stakeAmount;
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${months} month${months > 1 ? 's' : ''}</td>
                        <td>${balance.toFixed(0)} ${NETWORK_DATA[network].token}</td>
                        <td>+${rewards.toFixed(0)} ${NETWORK_DATA[network].token}</td>
                    `;
                    compoundBody.appendChild(row);
                }
            });
        }
        
        // Initial calculation
        calculate();
    </script>
</body>
</html>
