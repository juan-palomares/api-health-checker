# API Health Checker 🏥

![Health Check Status](https://github.com/juan-palomares/api-health-checker/actions/workflows/health-check.yml/badge.svg)

Automated API health monitoring system with scheduled CI/CD workflows using GitHub Actions.

## 🎯 Features

- **Automated Monitoring**: Checks API health every 6 hours via GitHub Actions scheduled workflows
- **Multiple API Support**: Monitor multiple endpoints simultaneously
- **Detailed Reporting**: Response time tracking, status code verification, error categorization
- **Smart Error Handling**: Timeout detection, connection errors, unexpected status codes
- **Manual Triggering**: Run health checks on-demand via GitHub Actions UI
- **Unit Tested**: Comprehensive test suite with mocked API responses

## 🔍 Monitored APIs

Currently monitoring:
- GitHub Status API
- JSONPlaceholder (Test API)
- REST Countries API
- Open-Meteo Weather API

## 🛠️ Technologies

- **Python 3.11**
- **requests** library for HTTP calls
- **unittest** for testing with mocks
- **GitHub Actions** for scheduled automation
- **Cron scheduling** for periodic execution

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/juan-palomares/api-health-checker.git
cd api-health-checker

# Install dependencies
pip install -r requirements.txt

# Run health check
python api_health_check.py

```

## 🧪 Running Tests

Bash
```
python -m unittest test_api_health_check.py -v
```
## 🔄 CI/CD Automation

The health checker runs automatically:

    Every 6 hours via GitHub Actions cron schedule
    On every push to the main branch
    Manually via the Actions tab (workflow_dispatch)

Cron Schedule

YAML
```
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours at minute 0
```
## 📊 Sample Output
```
text

======================================================================
API Health Check Report
Generated: 2024-01-15 10:30:45 UTC
======================================================================

✅ HEALTHY  | GitHub Status
   Status: 200 | Response Time: 0.45s
   URL: https://api.github.com/status

✅ HEALTHY  | JSONPlaceholder (Test API)
   Status: 200 | Response Time: 0.32s
   URL: https://jsonplaceholder.typicode.com/posts/1

======================================================================
SUMMARY
======================================================================
Total APIs Checked: 4
✅ Healthy: 4
❌ Unhealthy: 0

🎉 All APIs are operational!
```
## 🚀 How to Add More APIs

Edit the APIS_TO_CHECK list in api_health_check.py:
```
Python

APIS_TO_CHECK = [
    {
        "name": "Your API Name",
        "url": "https://your-api.com/endpoint",
        "expected_status": 200
    }
]
```
## 📚 What I Learned

    Scheduled CI/CD workflows using GitHub Actions cron syntax
    API monitoring best practices (timeouts, error handling, response time tracking)
    Mocking external dependencies in unit tests
    Exit codes for CI/CD success/failure signaling
    Automated health checks for production systems

## 🎯 DevOps Concepts Demonstrated

✅ Scheduled Automation - Cron-based workflows
✅ API Testing - Endpoint health verification
✅ Error Handling - Timeout, connection, HTTP error detection
✅ Monitoring & Alerting - Automated status reporting
✅ CI/CD Integration - Continuous health monitoring
✅ Unit Testing - Mocked dependencies for reliable tests
📧 Contact

Juan Palomares
GitHub: @juan-palomares