# hunter
User Guide: Hunter
Overview:

This Python script is designed to perform a username search across specified websites to identify if a particular username exists on those sites. It uses asynchronous requests for efficient concurrent URL queries.
Requirements:

    Python 3.x installed on your system.
    requests, asyncio, aiohttp Python libraries.
    websites.txt file containing URLs where the username needs to be searched. Ensure proper formatting in the file.

Setup:

    Python Installation: Install Python from python.org if not already installed.
    Library Installation: Run the following commands in your terminal:

    pip install requests
    pip install aiohttp

    Input File Preparation: Create a websites.txt file with each line representing a URL where the script will search for the specified username. Replace {username} in the URL with the placeholder for the username.

Usage:

    Running the Script:

    python hunter.py

    Authorization Prompt:
        Upon running, the tool will ask for authorization to proceed. Type 'yes' if authorized, 'no' to exit the tool.
        Only use this tool for ethical and legal purposes.

    Enter Username:
        If authorized, enter the username you want to search across the specified websites when prompted.

Output:

    The script will start searching for the entered username on the provided websites.
    It will display positive matches where the username is found and log any errors encountered during the search process.
    Results will be logged in the console indicating if the username was detected on each URL.

Caution:

    Ethical Usage: This tool is intended for ethical purposes only. Ensure you have legal permission to perform username searches on the specified websites.
    Data Privacy: Respect privacy and avoid misuse of information obtained through this tool.

Troubleshooting:

    Invalid URLs: Ensure all URLs in the websites.txt file are correctly formatted and contain the placeholder {username}.
