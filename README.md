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
```

Usage

    Clone or download this repository.
    Install the dependencies using pip install -r requirements.txt.
    Run the script with the path to the PE file you want to analyze.
```bash
python pe_import_scanner.py <path_to_pe_file>
```
Example:

```bash
python pe_import_scanner.py sample.exe
```
The tool will display the imported DLLs and functions in a formatted table.
Output

The script will provide the following:

    List of imported DLLs and functions in the PE file.
    Summary showing the total number of unique DLLs and the total number of functions.
    Debugging output to help trace errors or unexpected behaviors.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    pefile: A powerful library for working with PE files.
    tabulate: A great library for formatting tabular data.

