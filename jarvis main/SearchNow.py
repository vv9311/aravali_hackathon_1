import webbrowser

def searchGoogle(query):
    query = query.replace("google", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def searchYoutube(query):
    query = query.replace("youtube", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def searchWikipedia(query):
    query = query.replace("wikipedia", "")
    webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
