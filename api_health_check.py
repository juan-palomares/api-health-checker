"""
API Health Checker
Monitors multiple public APIs and report their status.
Runs automatically via GitHub Actions Scheduled workflows
"""

import requests
import sys
from datetime import datetime



# APIs to monitor

APIS_TO_CHECK = [
    {
        "name": "GitHub Status",
        "url": "https://api.github.com/status",
        "expected_status": 200
    },
    {
        "name": "JSONPlaceholder (Test API)",
        "url": "https://jsonplaceholder.typicode.com/posts/1",
        "expected_status": 200
    },
    {
        "name": "REST Countries API",
        "url": "https://restcountries.com/v3.1/name/usa",
        "expected_status": 200
    },
    {
        "name": "Open-Meteo Weather API",
        "url": "https://api.open-meteo.com/v1/forecast?latitude=34.0522&longitude=-118.2437&current_weather=true",
        "expected_status": 200
    },
]



def check_api(api_config):
    """
    Check if an API endpoint is responding correctly.

    Arg:
        api_config (dict): API configuration with name, url, and expected status

    Returns:
        bool: True if API is healthy, False otherwise
    """
    name = api_config["name"]
    url = api_config["url"]
    expected_status = api_config["expected_status"]

    try:
        response = requests.get(url, timeout=10)
        actual_status = response.status_code
        response_time = response.elapsed.total_seconds()

        if actual_status == expected_status:
            print(f"✅ Healthy | {name}")
            print(f"   Status: {actual_status} | Response Time: {response_time:.2f}s")
            print(f"   URL: {url}\n")
            return True
        else:
            print(f"⚠️ Warning | {name}")
            print(f"   Expected: {expected_status}, Got: {actual_status}")
            print(f"   URL: {url}\n")
            return False
        
    except requests.exceptions.Timeout:
        print(f"🚫 TIMEOUT | {name}")
        print(f"   URl: {url}")
        print(f"   Error: Request timed out after 10 seconds\n")
        return False
    
    except requests.exceptions.ConnectionError:
        print(f"🚫 OFFLINE | {name}")
        print(f"   URl: {url}")
        print(f"   Error: Could not connect to API\n")
        return False
    
    except Exception as e:
        print(f"🚫 ERROR | {name}")
        print(f"   URl: {url}")
        print(f"   Error: {str(e)}\n")
        return False
    

def main():
    """Run health checks on all configured APIs."""
    print("=" * 70)
    print(f"API Health Check Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 70)
    print()


    results = []
    for api_config in APIS_TO_CHECK:
        result = check_api(api_config)
        results.append(result)

    # Summary
    total_apis = len(results)
    healthy_apis = sum(results)
    unhealthy_apis = total_apis - healthy_apis

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total APIs Checked: {total_apis}")
    print(f"✅ Healthy: {healthy_apis}")
    print(f"❌ Unhealthy: {unhealthy_apis}")
    print()

    if all(results):
        print("🎉 ALL APIS ARE OPERATIONAL! 🎉")
        sys.exit(0)
    else:
        print("⚠️ Some APIs are experiencing issues ⚠️")
        sys.exit(1)



if __name__ == "__main__":
    main()