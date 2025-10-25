# CRYLO Research on AI Wealth Management for Digital Assets
This repo hosts the public methods, evaluation code, and dataset artifacts that support CRYLO’s research releases.

## CRYLO is Building a Web3 Wealth Manager
CRYLO.ai is becoming the first digital wealth management platform for cryptocurrencies, tokens, and other web3 protocols such as DeFi, NFTs and so on. This is part of our proof of concept for an AI-powered digital wealth manager. It goes through the entire wealth management process for digital assets. Finally, we want to democratize Wall Street, UBS, Blackrock and many others. The goal of this project is to prove that AI can beat any human trader at a massively lower cost and make professional wealth management accessible to the general public and not just to the wealthy.

This system uses 13+ artificial intelligence and machine learning algorithms as an orchestra. To find out more, read: (https://www.crylo.ai/news/what-is-crylo). Also consider going through our White Paper: (https://www.crylo.ai/about-crylo/technology).

**Note:** CRYLO is using third party APIs to collect data and to exchange FIAT/token.

## Would you like to contribute?
We are currently working on the MVP and are always looking for people to help us turn this idea into reality. Contact us on our website for investors relations (https://www.crylo.ai/about-crylo/investor-relations). If you just want to watch how we grow and stay informed about this project, then sign up on our website (https://www.crylo.ai).

**What’s here**
- **Methods paper (PDF):** `/paper/methods-paper.pdf`
- **Evaluation code & baselines:** `/eval/`
- **Dataset (schema + tiny sample):** `/dataset/` (full release via DOI)
- **Reproduce figures:** `/repro/repro.sh`

**Latest release:** v1.0.0 • DOI: _pending_  
**Website:** https://www.crylo.ai/research

## Quick start
```bash
# 1) Create env
conda env create -f repro/environment.yml && conda activate crylo-research
# 2) Reproduce core figures
bash repro/repro.sh
