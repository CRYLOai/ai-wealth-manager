#!/usr/bin/env bash
set -e
python eval/metrics.py --sample dataset/sample/sample.parquet --out figures/fig1_drawdowns.png
echo "Reproduction finished. See /figures"
