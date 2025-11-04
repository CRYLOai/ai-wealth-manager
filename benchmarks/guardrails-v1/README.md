# Benchmark: Guardrails v1
**Task:** Compare risk-first portfolios vs. baselines (buy & hold, equal-weight).  
**Data slices:** 2019–2025 (OOS windows).  
**Metrics:** AR, AV, Sharpe, Sortino, Max Drawdown, ES(95), Turnover.

## Leaderboard
- Download CSV: [`leaderboard.csv`](./leaderboard.csv)
- Figures: [`fig1_drawdowns.png`](./figures/fig1_drawdowns.png)

## Method summary
- Mechanisms disclosed; thresholds/weights redacted.
- Costs/funding included; outages/depegs simulated.

## Reproduce
```bash
conda env create -f repro/environment.yml && conda activate crylo-research
bash repro/repro.sh
```
## Citation
CRYLO Research (2025). *Guardrails v1 Benchmark*. DOI: pending.
