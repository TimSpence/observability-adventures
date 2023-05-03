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
**NOTE:** the service handles requests for these domains:
1. example.com
2. www.example.com

Be sure to add both domain names to `/etc/hosts` file or other domain name resolver.
```
curl http://example.com/
```

# Roadmap
- :ballot_box_with_check: move configuration out of build and mount into container instead
- :ballot_box_with_check: provide docker-compose.yml
- :ballot_box_with_check: route requests with flask
- :ballot_box_with_check: pin versions to avoid accidental upgrades
- :ballot_box_with_check: add health check
- :ballot_box_with_check: add reverse proxy
- :white_medium_square: add simulated slow upstream server
- :white_medium_square: add example with process control delegated to supervisord
