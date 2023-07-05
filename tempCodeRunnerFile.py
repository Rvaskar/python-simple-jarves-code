def search_web(query):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Path to your Chrome browser
    webbrowser.get(chrome_path).open(query)