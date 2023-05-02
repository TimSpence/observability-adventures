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
docker build --no-cache --tag myapp .
```
### Running
```
docker run -ti --rm --name myapp -p 8000:8000 myapp
```
### Testing
```
curl http://127.0.0.1:8000/
```

# Roadmap
- :white_medium_square: move configuration out of build and mount into container instead
- :white_medium_square: provide docker-compose.yml
- :white_medium_square: route requests with flask
- :white_medium_square: pin versions to avoid accidental upgrades
