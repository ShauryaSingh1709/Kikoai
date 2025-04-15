import requests

def get_weather():
    try:
        res = requests.get("https://wttr.in/?format=3")
        if res.status_code == 200:
            return f"Aaj ka weather: {res.text}"
        else:
            return "Weather check nahi ho paaya."
    except:
        return "Weather service down hai."
