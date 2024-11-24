# Advanced PE File Import Scanner

This tool is designed for analyzing Windows Portable Executable (PE) files to extract and display the imported DLLs and functions they rely on. It is a valuable tool for digital forensics, reverse engineering, and malware analysis. By inspecting the imports of PE files, you can identify potentially suspicious or malicious behavior.

## Features

- Scans PE files for imported DLLs and functions.
- Displays the DLL names and function names (or ordinals) in a human-readable table format.
- Provides summary statistics, including the total number of unique DLLs and the total number of functions imported.
- Debugging output to help you understand the parsing process.

## Requirements

To run this tool, you'll need the following Python packages:

- `pefile`: A Python library for parsing PE files.
- `tabulate`: A Python library for displaying data in tabular format.

You can install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
