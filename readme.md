# .env File Comparator

This Python script compares two `.env` files to identify any differences in their values.

## Prerequisites

- Python 3.4 or higher
- `python-dotenv` package

## Installation

### Step 1: Install Python

Ensure Python 3.4 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install pip

`pip` is usually included with Python 3.4 and later. If you need to install `pip` manually, follow these steps:

1. Download the `get-pip.py` script:

    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```

2. Run the script:

    ```bash
    python get-pip.py
    ```

    If you have multiple versions of Python, you may need to use `python3` instead of `python`:

    ```bash
    python3 get-pip.py
    ```

3. Verify the installation:

    ```bash
    pip --version
    ```

### Step 3: Install `python-dotenv`

Install the `python-dotenv` package using `pip`:

```bash
pip install python-dotenv
