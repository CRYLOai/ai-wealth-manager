# eval/metrics.py
# It creates the /figures folder (if missing) and writes an empty PNG.
import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sample", default="dataset/sample/sample.parquet",
                   help="Path to tiny sample data (placeholder)")
    p.add_argument("--out", default="figures/fig1_drawdowns.png",
                   help="Path to output figure")
    args = p.parse_args()

    # Ensure output folder exists
    Path("figures").mkdir(exist_ok=True)

    # TODO: We will replace this with real calculation & plotting later.
    # For now we just create an empty file so the pipeline completes.
    Path(args.out).touch()

    print("Placeholder metrics run complete.")
    print(f"Sample used: {args.sample}")
    print(f"Figure written: {args.out}")

if __name__ == "__main__":
    main()
