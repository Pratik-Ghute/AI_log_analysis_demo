# Log Analysis System

## Overview
This project provides a system for analyzing system logs using a Hugging Face-based large language model. The system processes log entries to detect anomalies, errors, and issues, then provides concise explanations and recommendations for resolution.

The core features include:
- Token counting for efficient handling of large logs.
- Log entry analysis using a pre-trained language model.
- Option to process either a full log file or a single log entry.
- Output can be printed to the terminal or saved to a file with a timestamp.

## Prerequisites
- Python 3.7 or higher
- Hugging Face account (for the model token)

## Dependencies
Before running the program, install the required dependencies by running the following:

```bash
pip install -r requirements.txt
```
Required Python packages:
huggingface_hub: To interact with Hugging Face models.
transformers: For tokenization and model inference.
argparse: For handling command-line arguments.
Setup
Get a Hugging Face Token: To use the Hugging Face model, you need an API token. You can get it by logging into Hugging Face and navigating to Settings -> Access Tokens. Copy your token and paste it into the config.py file in the HUGGINGFACE_TOKEN variable.

Use Inference Endpoints or Download the Model (To run on local server): The model used in this project is meta-llama/Meta-Llama-3-8B-Instruct. The first time you run the program, it will automatically download the necessary model weights from Hugging Face.

Directory Structure: The project consists of the following files:

plaintext
Copy code
log_analysis/
│
├── main.py                 # Main entry point that handles input arguments
├── config.py               # Configuration file for settings and constants
├── log_analysis.py         # Core logic for log analysis
├── tokenization.py         # Token counting and log splitting logic
├── utils.py                # Utility functions like file writing
└── requirements.txt        # File for listing dependencies
How to Run the Program
Command-Line Arguments
The program takes three command-line arguments:

log_input – The path to a log file or a single log entry string.
log_type – Specify whether the input is a full log file (file) or a single log entry (single).
--output – Optional argument to specify the output method: either terminal or file (default: file). If set to file, the output will be saved in a .txt file with a timestamp.
Running the Program
You can run the program as follows:

For a Log File:

If you want to analyze a full log file, provide the path to the log file and specify file as the log type:

bash
Copy code
```bash
python main.py path/to/logfile.log file --output terminal 
```
This will process the log file and print the output to the terminal.

For a Single Log Entry:

If you only have a single log entry to analyze, provide the log entry as a string and specify single as the log type:

```bash
python main.py "Your single log entry" single --output file
```
This will process the single log entry and save the result in a .txt file.

Custom Output File:

By default, the output will be saved in a file with the name output_<timestamp>.txt. You can change the output file format or name by modifying the code in main.py.

Example Output
Once the program processes the log data, it will output a response like this:

Error Description: Network connectivity issue detected.
Possible Cause: The server may have experienced a network timeout or loss of connection.
Recommended Solution: Check the network connection, reboot the server, or contact the network administrator for further assistance.
If the output is too large, it will be split into smaller chunks and processed sequentially.

Troubleshooting
Output file permission issues: Ensure that the directory has write permissions for output files.
Feel free to open an issue for any problems or improvements you find! 
