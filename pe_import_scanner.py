import pefile
import argparse
from tabulate import tabulate

def display_banner():
    banner = r"""
______ _____   _____                           _     _____                                 
| ___ \  ___| |_   _|                         | |   /  ___|                                
| |_/ / |__     | | _ __ ___  _ __   ___  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/|  __|    | || '_ ` _ \| '_ \ / _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |   | |___   _| || | | | | | |_) | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|   \____/   \___/_| |_| |_| .__/ \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
                             | |                                                           
                             |_|      By Cyber Sleuth                                                     
    """
    print(banner)

def parse_pe_file(file_path):
    print(f"[DEBUG] Checking file: {file_path}")
    try:
        pe = pefile.PE(file_path)
        if not hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            print("[INFO] No imports found in the PE file.")
            return []

        imports = []
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            try:
                dll_name = entry.dll.decode('utf-8') if entry.dll else "Unknown DLL"
            except (UnicodeDecodeError, AttributeError):
                dll_name = "Unknown DLL"

            print(f"[DEBUG] Found DLL: {dll_name}")  # Debugging line
            for imp in entry.imports:
                try:
                    function_name = imp.name.decode('utf-8') if imp.name else f"ord({imp.ordinal})"
                except (UnicodeDecodeError, AttributeError):
                    function_name = f"ord({imp.ordinal})"

                print(f"[DEBUG] Found function: {function_name}")  # Debugging line
                imports.append({"DLL": dll_name, "Function": function_name})

        print(f"[DEBUG] Total imports found: {len(imports)}")
        return imports

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except pefile.PEFormatError:
        print(f"[ERROR] Invalid PE file format: {file_path}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {str(e)}")
    return []

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="Advanced PE File Import Scanner")
    parser.add_argument("file", help="Path to the PE file to analyze")
    args = parser.parse_args()

    print("[INFO] Analyzing PE file imports...")
    imports = parse_pe_file(args.file)

    if imports:
        print("\n[RESULT] Imports found:")
        print(tabulate(imports, headers="keys", tablefmt="pretty"))
        print(f"\n[SUMMARY] Total DLLs: {len(set(i['DLL'] for i in imports))}")
        print(f"Total Functions: {len(imports)}")
    else:
        print("[INFO] No imports to display.")

if __name__ == "__main__":
    main()
