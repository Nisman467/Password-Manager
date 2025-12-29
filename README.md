# 🔐 Password Manager (Python GUI)

This is a **Python learning project** — a GUI-based password manager.

## Features
- Master password login
- Add / View / Update / Delete passwords
- Encrypted password storage
- SQLite database
- GUI built with tkinter

## Requirements
- Python 3.13
- Windows 11 (for .exe build)

Install dependency:
pip install -r requirements.txt

## Run the application
python gui.py

## Build .exe file (Windows)
Use PyInstaller:
pyinstaller --onefile gui.py

After building, the `.exe` file will be created inside the `dist/` folder.

⚠️ The `.exe` file is NOT included in this repository.  
Build it locally using the command above.

## Notes
Do NOT upload:
- master.hash
- database (.db) files
- encryption keys
- dist/ folder or .exe file

## License
MIT License  
This project is for learning purposes only.
