"""
Automated Financial Data Pipeline
Runs complete ETL process: Extract → Transform → Load → Analyze
"""

import subprocess
import sys
from datetime import datetime

def run_command(script_path, description):
    """Run a Python script and handle errors"""
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error in {description}:")
        print(e.stderr)
        return False

def main():
    """Run complete automated pipeline"""
    start_time = datetime.now()
    
    print("""
╔════════════════════════════════════════════════════════════╗
║     AUTOMATED FINANCIAL DATA PIPELINE                      ║
║     Extract → Process → Store → Analyze → Insights         ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    print(f"Pipeline started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Pipeline steps
    steps = [
        ("scripts/extract_data.py", "Data Extraction (Yahoo Finance API)"),
        ("scripts/process_data.py", "Data Processing (Technical Indicators)"),
        ("scripts/load_to_mongodb.py", "Load to MongoDB (Cloud Storage)"),
        ("scripts/generate_ai_insights.py", "AI Insights Generation")
    ]
    
    # Execute pipeline
    success_count = 0
    for script, description in steps:
        if run_command(script, description):
            success_count += 1
        else:
            print(f"\n⚠ Pipeline stopped due to error in: {description}")
            break
    
    # Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print(f"\n{'='*60}")
    print("PIPELINE SUMMARY")
    print(f"{'='*60}")
    print(f"Steps completed: {success_count}/{len(steps)}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Status: {'✓ SUCCESS' if success_count == len(steps) else '✗ FAILED'}")
    print(f"Completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    if success_count == len(steps):
        print("\n✓ All data successfully processed and insights generated!")
        print("✓ Check reports/ai_market_insights.md for AI commentary")

if __name__ == "__main__":
    main()