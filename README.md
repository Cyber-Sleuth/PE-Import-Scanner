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

python enum_imports.py samples.exe   
______ _____   _____                           _     _____
| ___ \  ___| |_   _|                         | |   /  ___|
| |_/ / |__     | | _ __ ___  _ __   ___  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/|  __|    | || '_ ` _ \| '_ \ / _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |   | |___   _| || | | | | | |_) | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|   \____/   \___/_| |_| |_| .__/ \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
                             | |
                             |_|      By Cyber Sleuth
    
[INFO] Analyzing PE file imports...
[DEBUG] Checking file: Obsidian-1.7.4.exe
[DEBUG] Found DLL: KERNEL32.dll
[DEBUG] Found function: SetEnvironmentVariableW
[DEBUG] Found function: SetFileAttributesW
[DEBUG] Found function: Sleep
[DEBUG] Found function: GetTickCount
[DEBUG] Found function: GetFileSize
[DEBUG] Found function: GetModuleFileNameW
[DEBUG] Found function: GetCurrentProcess
[DEBUG] Found function: CopyFileW
[DEBUG] Found function: SetCurrentDirectoryW
[DEBUG] Found function: GetFileAttributesW
[DEBUG] Found function: GetWindowsDirectoryW
[DEBUG] Found function: GetTempPathW
[DEBUG] Found function: GetCommandLineW
[DEBUG] Found function: GetVersion
[DEBUG] Found function: SetErrorMode
[DEBUG] Found function: lstrlenW
[DEBUG] Found function: lstrcpynW
[DEBUG] Found function: GetDiskFreeSpaceW
[DEBUG] Found function: ExitProcess
[DEBUG] Found function: GetShortPathNameW
[DEBUG] Found function: CreateThread
[DEBUG] Found function: GetLastError
[DEBUG] Found function: CreateDirectoryW
[DEBUG] Found function: CreateProcessW
[DEBUG] Found function: RemoveDirectoryW
[DEBUG] Found function: lstrcmpiA
[DEBUG] Found function: CreateFileW
[DEBUG] Found function: GetTempFileNameW
[DEBUG] Found function: WriteFile
[DEBUG] Found function: lstrcpyA
[DEBUG] Found function: MoveFileExW
[DEBUG] Found function: lstrcatW
[DEBUG] Found function: GetSystemDirectoryW
[DEBUG] Found function: GetProcAddress
[DEBUG] Found function: GetModuleHandleA
[DEBUG] Found function: GetExitCodeProcess
[DEBUG] Found function: WaitForSingleObject
[DEBUG] Found function: lstrcmpiW
[DEBUG] Found function: MoveFileW
[DEBUG] Found function: GetFullPathNameW
[DEBUG] Found function: SetFileTime
[DEBUG] Found function: SearchPathW
[DEBUG] Found function: CompareFileTime
[DEBUG] Found function: lstrcmpW
[DEBUG] Found function: CloseHandle
[DEBUG] Found function: ExpandEnvironmentStringsW
[DEBUG] Found function: GlobalFree
[DEBUG] Found function: GlobalLock
[DEBUG] Found function: GlobalUnlock
[DEBUG] Found function: GlobalAlloc
[DEBUG] Found function: FindFirstFileW
[DEBUG] Found function: FindNextFileW
[DEBUG] Found function: DeleteFileW
[DEBUG] Found function: SetFilePointer
[DEBUG] Found function: ReadFile
[DEBUG] Found function: FindClose
[DEBUG] Found function: lstrlenA
[DEBUG] Found function: MulDiv
[DEBUG] Found function: MultiByteToWideChar
[DEBUG] Found function: WideCharToMultiByte
[DEBUG] Found function: GetPrivateProfileStringW
[DEBUG] Found function: WritePrivateProfileStringW
[DEBUG] Found function: FreeLibrary
[DEBUG] Found function: LoadLibraryExW
[DEBUG] Found function: GetModuleHandleW
[DEBUG] Found DLL: USER32.dll
[DEBUG] Found function: GetSystemMenu
[DEBUG] Found function: SetClassLongW
[DEBUG] Found function: EnableMenuItem
[DEBUG] Found function: IsWindowEnabled
[DEBUG] Found function: SetWindowPos
[DEBUG] Found function: GetSysColor
[DEBUG] Found function: GetWindowLongW
[DEBUG] Found function: SetCursor
[DEBUG] Found function: LoadCursorW
[DEBUG] Found function: CheckDlgButton
[DEBUG] Found function: GetMessagePos
[DEBUG] Found function: LoadBitmapW
[DEBUG] Found function: CallWindowProcW
[DEBUG] Found function: IsWindowVisible
[DEBUG] Found function: CloseClipboard
[DEBUG] Found function: SetClipboardData
[DEBUG] Found function: EmptyClipboard
[DEBUG] Found function: OpenClipboard
[DEBUG] Found function: ScreenToClient
[DEBUG] Found function: GetWindowRect
[DEBUG] Found function: GetDlgItem
[DEBUG] Found function: GetSystemMetrics
[DEBUG] Found function: SetDlgItemTextW
[DEBUG] Found function: GetDlgItemTextW
[DEBUG] Found function: MessageBoxIndirectW
[DEBUG] Found function: CharPrevW
[DEBUG] Found function: CharNextA
[DEBUG] Found function: wsprintfA
[DEBUG] Found function: DispatchMessageW
[DEBUG] Found function: PeekMessageW
[DEBUG] Found function: ReleaseDC
[DEBUG] Found function: EnableWindow
[DEBUG] Found function: InvalidateRect
[DEBUG] Found function: SendMessageW
[DEBUG] Found function: DefWindowProcW
[DEBUG] Found function: BeginPaint
[DEBUG] Found function: GetClientRect
[DEBUG] Found function: FillRect
[DEBUG] Found function: DrawTextW
[DEBUG] Found function: EndDialog
[DEBUG] Found function: RegisterClassW
[DEBUG] Found function: SystemParametersInfoW
[DEBUG] Found function: CreateWindowExW
[DEBUG] Found function: GetClassInfoW
[DEBUG] Found function: DialogBoxParamW
[DEBUG] Found function: CharNextW
[DEBUG] Found function: ExitWindowsEx
[DEBUG] Found function: DestroyWindow
[DEBUG] Found function: GetDC
[DEBUG] Found function: SetTimer
[DEBUG] Found function: SetWindowTextW
[DEBUG] Found function: LoadImageW
[DEBUG] Found function: SetForegroundWindow
[DEBUG] Found function: ShowWindow
[DEBUG] Found function: IsWindow
[DEBUG] Found function: SetWindowLongW
[DEBUG] Found function: FindWindowExW
[DEBUG] Found function: TrackPopupMenu
[DEBUG] Found function: AppendMenuW
[DEBUG] Found function: CreatePopupMenu
[DEBUG] Found function: EndPaint
[DEBUG] Found function: CreateDialogParamW
[DEBUG] Found function: SendMessageTimeoutW
[DEBUG] Found function: wsprintfW
[DEBUG] Found function: PostQuitMessage
[DEBUG] Found DLL: GDI32.dll
[DEBUG] Found function: SelectObject
[DEBUG] Found function: SetBkMode
[DEBUG] Found function: CreateFontIndirectW
[DEBUG] Found function: SetTextColor
[DEBUG] Found function: DeleteObject
[DEBUG] Found function: GetDeviceCaps
[DEBUG] Found function: CreateBrushIndirect
[DEBUG] Found function: SetBkColor
[DEBUG] Found DLL: SHELL32.dll
[DEBUG] Found function: SHGetSpecialFolderLocation
[DEBUG] Found function: ShellExecuteExW
[DEBUG] Found function: SHGetPathFromIDListW
[DEBUG] Found function: SHBrowseForFolderW
[DEBUG] Found function: SHGetFileInfoW
[DEBUG] Found function: SHFileOperationW
[DEBUG] Found DLL: ADVAPI32.dll
[DEBUG] Found function: AdjustTokenPrivileges
[DEBUG] Found function: RegCreateKeyExW
[DEBUG] Found function: RegOpenKeyExW
[DEBUG] Found function: SetFileSecurityW
[DEBUG] Found function: OpenProcessToken
[DEBUG] Found function: LookupPrivilegeValueW
[DEBUG] Found function: RegEnumValueW
[DEBUG] Found function: RegDeleteKeyW
[DEBUG] Found function: RegDeleteValueW
[DEBUG] Found function: RegCloseKey
[DEBUG] Found function: RegSetValueExW
[DEBUG] Found function: RegQueryValueExW
[DEBUG] Found function: RegEnumKeyW
[DEBUG] Found DLL: COMCTL32.dll
[DEBUG] Found function: ImageList_Create
[DEBUG] Found function: ImageList_AddMasked
[DEBUG] Found function: ImageList_Destroy
[DEBUG] Found function: ord(17)
[DEBUG] Found DLL: ole32.dll
[DEBUG] Found function: OleUninitialize
[DEBUG] Found function: OleInitialize
[DEBUG] Found function: CoTaskMemFree
[DEBUG] Found function: CoCreateInstance
[DEBUG] Total imports found: 165

[RESULT] Imports found:
+--------------+----------------------------+
|     DLL      |          Function          |
+--------------+----------------------------+
| KERNEL32.dll |  SetEnvironmentVariableW   |
| KERNEL32.dll |     SetFileAttributesW     |
| KERNEL32.dll |           Sleep            |
| KERNEL32.dll |        GetTickCount        |
| KERNEL32.dll |        GetFileSize         |
| KERNEL32.dll |     GetModuleFileNameW     |
| KERNEL32.dll |     GetCurrentProcess      |
| KERNEL32.dll |         CopyFileW          |
| KERNEL32.dll |    SetCurrentDirectoryW    |
| KERNEL32.dll |     GetFileAttributesW     |
| KERNEL32.dll |    GetWindowsDirectoryW    |
| KERNEL32.dll |        GetTempPathW        |
| KERNEL32.dll |      GetCommandLineW       |
| KERNEL32.dll |         GetVersion         |
| KERNEL32.dll |        SetErrorMode        |
| KERNEL32.dll |          lstrlenW          |
| KERNEL32.dll |         lstrcpynW          |
| KERNEL32.dll |     GetDiskFreeSpaceW      |
| KERNEL32.dll |        ExitProcess         |
| KERNEL32.dll |     GetShortPathNameW      |
| KERNEL32.dll |        CreateThread        |
| KERNEL32.dll |        GetLastError        |
| KERNEL32.dll |      CreateDirectoryW      |
| KERNEL32.dll |       CreateProcessW       |
| KERNEL32.dll |      RemoveDirectoryW      |
| KERNEL32.dll |         lstrcmpiA          |
| KERNEL32.dll |        CreateFileW         |
| KERNEL32.dll |      GetTempFileNameW      |
| KERNEL32.dll |         WriteFile          |
| KERNEL32.dll |          lstrcpyA          |
| KERNEL32.dll |        MoveFileExW         |
| KERNEL32.dll |          lstrcatW          |
| KERNEL32.dll |    GetSystemDirectoryW     |
| KERNEL32.dll |       GetProcAddress       |
| KERNEL32.dll |      GetModuleHandleA      |
| KERNEL32.dll |     GetExitCodeProcess     |
| KERNEL32.dll |    WaitForSingleObject     |
| KERNEL32.dll |         lstrcmpiW          |
| KERNEL32.dll |         MoveFileW          |
| KERNEL32.dll |      GetFullPathNameW      |
| KERNEL32.dll |        SetFileTime         |
| KERNEL32.dll |        SearchPathW         |
| KERNEL32.dll |      CompareFileTime       |
| KERNEL32.dll |          lstrcmpW          |
| KERNEL32.dll |        CloseHandle         |
| KERNEL32.dll | ExpandEnvironmentStringsW  |
| KERNEL32.dll |         GlobalFree         |
| KERNEL32.dll |         GlobalLock         |
| KERNEL32.dll |        GlobalUnlock        |
| KERNEL32.dll |        GlobalAlloc         |
| KERNEL32.dll |       FindFirstFileW       |
| KERNEL32.dll |       FindNextFileW        |
| KERNEL32.dll |        DeleteFileW         |
| KERNEL32.dll |       SetFilePointer       |
| KERNEL32.dll |          ReadFile          |
| KERNEL32.dll |         FindClose          |
| KERNEL32.dll |          lstrlenA          |
| KERNEL32.dll |           MulDiv           |
| KERNEL32.dll |    MultiByteToWideChar     |
| KERNEL32.dll |    WideCharToMultiByte     |
| KERNEL32.dll |  GetPrivateProfileStringW  |
| KERNEL32.dll | WritePrivateProfileStringW |
| KERNEL32.dll |        FreeLibrary         |
| KERNEL32.dll |       LoadLibraryExW       |
| KERNEL32.dll |      GetModuleHandleW      |
|  USER32.dll  |       GetSystemMenu        |
|  USER32.dll  |       SetClassLongW        |
|  USER32.dll  |       EnableMenuItem       |
|  USER32.dll  |      IsWindowEnabled       |
|  USER32.dll  |        SetWindowPos        |
|  USER32.dll  |        GetSysColor         |
|  USER32.dll  |       GetWindowLongW       |
|  USER32.dll  |         SetCursor          |
|  USER32.dll  |        LoadCursorW         |
|  USER32.dll  |       CheckDlgButton       |
|  USER32.dll  |       GetMessagePos        |
|  USER32.dll  |        LoadBitmapW         |
|  USER32.dll  |      CallWindowProcW       |
|  USER32.dll  |      IsWindowVisible       |
|  USER32.dll  |       CloseClipboard       |
|  USER32.dll  |      SetClipboardData      |
|  USER32.dll  |       EmptyClipboard       |
|  USER32.dll  |       OpenClipboard        |
|  USER32.dll  |       ScreenToClient       |
|  USER32.dll  |       GetWindowRect        |
|  USER32.dll  |         GetDlgItem         |
|  USER32.dll  |      GetSystemMetrics      |
|  USER32.dll  |      SetDlgItemTextW       |
|  USER32.dll  |      GetDlgItemTextW       |
|  USER32.dll  |    MessageBoxIndirectW     |
|  USER32.dll  |         CharPrevW          |
|  USER32.dll  |         CharNextA          |
|  USER32.dll  |         wsprintfA          |
|  USER32.dll  |      DispatchMessageW      |
|  USER32.dll  |        PeekMessageW        |
|  USER32.dll  |         ReleaseDC          |
|  USER32.dll  |        EnableWindow        |
|  USER32.dll  |       InvalidateRect       |
|  USER32.dll  |        SendMessageW        |
|  USER32.dll  |       DefWindowProcW       |
|  USER32.dll  |         BeginPaint         |
|  USER32.dll  |       GetClientRect        |
|  USER32.dll  |          FillRect          |
|  USER32.dll  |         DrawTextW          |
|  USER32.dll  |         EndDialog          |
|  USER32.dll  |       RegisterClassW       |
|  USER32.dll  |   SystemParametersInfoW    |
|  USER32.dll  |      CreateWindowExW       |
|  USER32.dll  |       GetClassInfoW        |
|  USER32.dll  |      DialogBoxParamW       |
|  USER32.dll  |         CharNextW          |
|  USER32.dll  |       ExitWindowsEx        |
|  USER32.dll  |       DestroyWindow        |
|  USER32.dll  |           GetDC            |
|  USER32.dll  |          SetTimer          |
|  USER32.dll  |       SetWindowTextW       |
|  USER32.dll  |         LoadImageW         |
|  USER32.dll  |    SetForegroundWindow     |
|  USER32.dll  |         ShowWindow         |
|  USER32.dll  |          IsWindow          |
|  USER32.dll  |       SetWindowLongW       |
|  USER32.dll  |       FindWindowExW        |
|  USER32.dll  |       TrackPopupMenu       |
|  USER32.dll  |        AppendMenuW         |
|  USER32.dll  |      CreatePopupMenu       |
|  USER32.dll  |          EndPaint          |
|  USER32.dll  |     CreateDialogParamW     |
|  USER32.dll  |    SendMessageTimeoutW     |
|  USER32.dll  |         wsprintfW          |
|  USER32.dll  |      PostQuitMessage       |
|  GDI32.dll   |        SelectObject        |
|  GDI32.dll   |         SetBkMode          |
|  GDI32.dll   |    CreateFontIndirectW     |
|  GDI32.dll   |        SetTextColor        |
|  GDI32.dll   |        DeleteObject        |
|  GDI32.dll   |       GetDeviceCaps        |
|  GDI32.dll   |    CreateBrushIndirect     |
|  GDI32.dll   |         SetBkColor         |
| SHELL32.dll  | SHGetSpecialFolderLocation |
| SHELL32.dll  |      ShellExecuteExW       |
| SHELL32.dll  |    SHGetPathFromIDListW    |
| SHELL32.dll  |     SHBrowseForFolderW     |
| SHELL32.dll  |       SHGetFileInfoW       |
| SHELL32.dll  |      SHFileOperationW      |
| ADVAPI32.dll |   AdjustTokenPrivileges    |
| ADVAPI32.dll |      RegCreateKeyExW       |
| ADVAPI32.dll |       RegOpenKeyExW        |
| ADVAPI32.dll |      SetFileSecurityW      |
| ADVAPI32.dll |      OpenProcessToken      |
| ADVAPI32.dll |   LookupPrivilegeValueW    |
| ADVAPI32.dll |       RegEnumValueW        |
| ADVAPI32.dll |       RegDeleteKeyW        |
| ADVAPI32.dll |      RegDeleteValueW       |
| ADVAPI32.dll |        RegCloseKey         |
| ADVAPI32.dll |       RegSetValueExW       |
| ADVAPI32.dll |      RegQueryValueExW      |
| ADVAPI32.dll |        RegEnumKeyW         |
| COMCTL32.dll |      ImageList_Create      |
| COMCTL32.dll |    ImageList_AddMasked     |
| COMCTL32.dll |     ImageList_Destroy      |
| COMCTL32.dll |          ord(17)           |
|  ole32.dll   |      OleUninitialize       |
|  ole32.dll   |       OleInitialize        |
|  ole32.dll   |       CoTaskMemFree        |
|  ole32.dll   |      CoCreateInstance      |
+--------------+----------------------------+

[SUMMARY] Total DLLs: 7
Total Functions: 165
