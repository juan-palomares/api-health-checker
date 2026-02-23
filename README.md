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