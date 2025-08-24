![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# JOKER - Pranks App (Educational Project)

> **⚠ WARNING: For educational purposes only! Use only on devices you own with explicit permission.**

## 📖 Overview

JOKER is a Python-based application demonstrating system integration capabilities. It is still in early development and currently can only send realistic Windows notifications and explore random folders.

## ⚠ Disclaimer

**THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.** The author is not responsible for:

- Any damages caused by misuse or illegal use
- Legal consequences of unauthorized usage  
- System instability or data loss
- Violation of local laws and regulations

**Use only for educational purposes on your own devices!**

## Features

-  **System Notifications** - Realistic Windows security alerts
-  **Random Folder Explorer** - Discovers and opens random directories
-  **Modern GUI** - Built with Flet framework
-  **Multi-threading** - Non-blocking user interface

##  Compatibility

###  Tested & Working
- **Windows 10** (22H2+) - Full functionality
- **Windows 11** (All versions) - Optimal performance
- **Python 3.8-3.13** - Cross-version compatible

### ⚠ Limitations
- **Admin folders** require elevated privileges
- **Antivirus software** may flag as false positive
- **Non-Windows OS** not supported (uses Windows APIs)

### 📋 Requirements
```bash
# Core dependencies
flet >= 0.22.0
pyinstaller >= 6.0.0
pillow >= 10.0.0


# Joker app

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).
