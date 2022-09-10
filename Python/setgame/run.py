import re
import requests

if __name__ == "__main__":
    print(re.findall("board\.initSets\((.)", str(requests.get("https://www.setgame.com/set/puzzle").content)))