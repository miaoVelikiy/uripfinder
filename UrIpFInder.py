import urllib.request
import json


def get_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org?format=json", timeout=5) as response:
            data = json.loads(response.read().decode())
            return data.get("ip")
    except Exception as e:
        return f"Could not retrieve IP address: {e}"


def main():
    print("IP Finder")
    print("Press Q to show your IP address, or Ctrl+C to quit.\n")
    while True:
        key = input("> ").strip().lower()
        if key == "q":
            ip = get_ip()
            print(f"Your IP address is: {ip}\n")
        else:
            print("Press Q to show your IP address.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")