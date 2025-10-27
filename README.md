# CRYLO Research on AI Wealth Management for Digital Assets
This repo hosts the public methods, evaluation code, and dataset artifacts that support CRYLO’s research releases.

## CRYLO Research: Methods & Evaluation Kit
Guardrailed, non-custodial crypto-portfolio research: methods, evaluation code, and dataset artifacts.

**Website:** https://www.crylo.ai/research  
**This repo:** public methods, baselines, a minimal reproduction kit, and dataset schema/sample.  
**Latest release:** v1.0.0 • DOI: 

---

## Table of contents
- [Problem & Motivation](#problem--motivation)
- [Research Objectives & Questions](#research-objectives--questions)
- [Novelty vs. Prior Work](#novelty-vs-prior-work)
- [Value of the Pilot Study](#value-of-the-pilot-study)
- [Repository Layout](#repository-layout)
- [Quick start](#quick-start)
- [Reproducibility & Data](#reproducibility--data)
- [Scope & Privacy](#scope--privacy)
- [How to cite](#how-to-cite)
- [Licensing](#licensing)
- [Authors & Affiliations](#authors--affiliations)
- [Releases, DOI & Versioning](#releases-doi--versioning)
- [Contact](#contact)

---

## Problem & Motivation
Access to professional crypto-asset management remains difficult for many investors. Complexity, high volatility, and the lack of standardized evaluation frameworks make informed decisions hard. CRYLO aims to reduce these barriers by delivering a **fully automated, AI-assisted portfolio construction and monitoring framework** for digital assets, with an emphasis on **risk-first controls** and **user-retained custody**.

Unlike single-function trading platforms, our research combines **machine learning (ML)**, **risk–return optimization**, and **real-time market data** to manage diversified portfolios, covering all web3 investment options. ML-based return signals are incorporated directly into the construction process so that allocations can respond dynamically to evolving market regimes.

## Research Objectives & Questions
With our academic partner, the Institute for Financial Services Zug IFZ at Lucerne University of Applied Sciences and Arts , we plan to evaluate—on scientific grounds—whether **ML-based return forecasts** can improve **risk-adjusted performance** of crypto portfolios versus traditional models. And thus goes beyond traditional approaches such as those of Markowitz (1952) or Black and Litterman (1992). Although recent academic research (e.g., Chen et al., 2021; Filippou et al., 2024) has addressed ML-based return forecasts for cryptocurrencies, little attention has been paid to the use of these findings in practical portfolio optimization, particularly in relation to all web3 investment options. We differentiate ourselves by incorporating ML-based forecasting models into portfolio optimization to improve portfolio performance.

### Key questions:
- **Which ML families** are suitable for return forecasting in digital assets?  
- **Which features/factors** are empirically predictive in this domain?  
- **How do ML-guided portfolios perform out-of-sample** relative to classical approaches?  
- **What constitutes a robust backtesting framework** for this asset class (costs, slippage, outages, depegs, stress scenarios)?

## Novelty vs. Prior Work
Many robo-advisors do not yet offer **ML-optimized** crypto portfolios; crypto fintechs often rely on simple momentum/diversification rules; and traditional providers rarely perform **automated, ML-based portfolio optimization** end-to-end. Recent academic papers explore ML for crypto forecasts, but **practical integration into portfolio construction** and **guardrail evaluation** is limited. Our work focuses on **operationalizing** these insights: ML forecasts inform allocation decisions within a **constraints-aware, risk-first** framework designed for real investors.

> We publish **mechanisms and evaluation** (not proprietary thresholds or model weights). Results are documented with baselines, metrics, and limitations.

## Value of the Pilot Study
This pilot assesses **technical and economic feasibility** of combining ML signals with portfolio optimization and guardrails. Outcomes we seek:
- A **validated evaluation pipeline** and minimal reference implementation for a later MVP.  
- A deeper synthesis of the literature and a practical selection of forecasting methods.  
- **Out-of-sample, risk-adjusted performance** estimates under realistic frictions.  
- Dual applicability: **B2B licensing** for institutions and **retail access** to professionally managed strategies—supporting financial inclusion.

## Repository Layout
/paper/ # Methods paper (PDF + source)<br>
/eval/ # Metrics & baselines (code)<br>
/repro/ # One-command reproduction scripts & env spec<br>
/dataset/ # Dataset card (README), schema, tiny sample (not full data)<br>
/figures/ # Generated figures (after running repro)<br>
LICENSE # Apache-2.0 for code<br>
LICENSE-DOCS-DATA # CC BY 4.0 for docs & sample data<br>
CITATION.cff # GitHub “Cite this repository” metadata<br>
README.md

---

## Quick start
Run these commands locally to set up the environment and regenerate figures.

```bash
# 1) Create env (conda)
conda env create -f repro/environment.yml && conda activate crylo-research
# or: python venv
python -m venv .venv && source .venv/bin/activate
pip install -r repro/requirements.txt

# 2) Reproduce core figures
bash repro/repro.sh
```

---

## Reproducibility & Data
- We include a tiny sample under /dataset/sample/ for quick checks.
- Full datasets will be hosted via Zenodo DOIs and referenced from /dataset/README.md.
- The evaluation code targets deterministic runs (fixed seeds) and includes basic leakage and alignment checks.

## Scope & Privacy
No client data is included. We use public-market data and synthetic labels for evaluation tasks. We disclose mechanisms, constraints, and metrics—but do not disclose proprietary thresholds, model weights, or feature recipes that would enable cloning.

## How to cite
Once the DOI is minted (via Zenodo), GitHub will show a “Cite this repository” button powered by CITATION.cff.

**Temporary citation:**
> CRYLO Research (2025). *Methods & Evaluation Kit*. Version v1.0.0. DOI: *pending*. Available at: (https://github.com/CRYLOai/ai-wealth-manager)

## Licensing
- **Code:** Apache-2.0 license.
- **Documentation & sample data:** CC BY 4.0.
- Please review third-party licenses if you adapt or extend this work.

## Authors & Affiliations
- **CRYLO Research** (Organization)
- Marcel Isler (https://orcid.org/0009-0003-5361-6642)
- Almagul Kondybayeva
- Prof. Dr. Jürg Fausch, Institute for Financial Services Zug IFZ at Lucerne University of Applied Sciences and Arts

## Releases, DOI & Versioning
1. GitHub release v1.0.0
2. DOI
3. Updated CITATION.cff with the version DOI, plus version and date-released

## Contact
Research inquiries: <research@crylo.ai>
