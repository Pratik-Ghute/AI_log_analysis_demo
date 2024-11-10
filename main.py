import argparse
from log_analysis import analyze_logs
from utils import save_to_file
import time

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze system logs.")
    parser.add_argument("log_input", type=str, help="Path to the log file or a single log entry")
    parser.add_argument("log_type", choices=["file", "single"], help="Specify whether the input is a log file or a single log")
    parser.add_argument("--output", choices=["terminal", "file"], default="file", help="Where to print the output: terminal or file")

    return parser.parse_args()

def main():
    args = parse_args()

    # Timestamp for output file
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_filename = f"output_{timestamp}.txt"

    if args.log_type == "file":
        with open(args.log_input, "r") as log_file:
            log_text = log_file.read()
    else:
        log_text = args.log_input

    # Analyze logs
    response = analyze_logs(log_text)

    # Output to terminal or file
    if args.output == "terminal":
        print(response)
    else:
        save_to_file(response, output_filename)

if __name__ == "__main__":
    main()
