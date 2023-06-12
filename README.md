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
#### Running with Grafana
Alternatively you can run the service with a Grafana integration:
```
docker-compose -f docker-compose.yml -f docker-compose-grafana-prometheus.yml up
```
and stop the services like this:
```
docker-compose -f docker-compose.yml -f docker-compose-grafana-prometheus.yml down
```
#### Running with Datadog
Alternatively you can run the service with a Grafana integration.  This will require a Datadog API key.

Copy `.env.example` to a new file named `.env`, uncomment the line containing `DD_API_KEY`, and add your key.

Start the services with this command:
```
docker-compose -f docker-compose-datadog.yml up
```
and stop the services like this:
```
docker-compose -f docker-compose-datadog.yml down
```
### Testing
**NOTE:** the service handles requests for these domains:
1. example.com
2. www.example.com

Be sure to add both domain names to `/etc/hosts` file or other domain name resolver.
```
curl http://example.com/
curl http://example.com/slow-endpoint
```

# Acknowledgements
- [Blueswen/gunicorn-monitoring](https://github.com/Blueswen/gunicorn-monitoring): high-quality example of integration with Grafana

# Roadmap
- :ballot_box_with_check: move configuration out of build and mount into container instead
- :ballot_box_with_check: provide docker-compose.yml
- :ballot_box_with_check: route requests with flask
- :ballot_box_with_check: pin versions to avoid accidental upgrades
- :ballot_box_with_check: add health check
- :ballot_box_with_check: add reverse proxy
- :ballot_box_with_check: add simulated slow upstream server
- :ballot_box_with_check: add simulated buggy endpoint
- :ballot_box_with_check: integrate Grafana
- :white_medium_square: add example with process control delegated to supervisord
