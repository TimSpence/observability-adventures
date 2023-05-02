py-webapp-hosting
=================

# Background
A naive example of a python web app hosted in gunicorn.

# Usage
**This is not a production-ready application**

Use this app to tune and benchmark in non-production environments.

## Docker

### Building
```
docker-compose build myapp
```
### Running
```
docker-compose up
```
### Testing
```
curl http://127.0.0.1:8000/
```

# Roadmap
- :ballot_box_with_check: move configuration out of build and mount into container instead
- :ballot_box_with_check: provide docker-compose.yml
- :white_medium_square: route requests with flask
- :ballot_box_with_check: pin versions to avoid accidental upgrades
