# Run Services locally in Docker Compose

## Requirements for running the services locally in Docker Compose

To run services locally in Docker Compose, you need to fulfil the following requirements:

- Recent version of `docker-compsose` that supports at least protocol version `2.1`. For installation instructions, click [here](https://docs.docker.com/compose/install/).
- Recent version of Docker.
- Access to the Workbench.
- Configured access to the Docker registry. For instructions, click [here](https://gard.telekom.de/gardwiki/display/SH/Docker).
- Enough RAM (about 250 MB per service).

## How the Docker Compose services work

The services in a Docker Compose group start with the same container name as the service names in Openshift.

In addition, there is a proxy container. From the perspective of the proxy, you can reach all services by their original hostname.

When you start the skill via `python manage.py -l run` and the the hostname starts and ends with `service`, the proxy is used within a `ZipkinCircuitbreakerSession`.

As an result, the dockerized local services are used without any change in the URL.

## Instructions for the Docker Compose usage

To use Docker Compose, proceed as follows:

1. As a base, use a copy of the file `contrib/docker_services/docker_compose` from the SDK.
2. Except for the proxy and the text service, remove the services from the file that your skill does **not** need.
3. To startup the compose group via `docker-compose up`, the `docker-compose.yml` file must be in the current working directory.
4. Start your skill with the global `-l` / `--local` argument `python manage.py -l run`.

To end the docker group, press `Ctrl` + `C`.

To retrieve new container versions, use `docker-compose pull`.

## Direct access

Every service has an expose port on localhost in the 808x area. This is defined in the `docker-compose.yml` file.

In addition, you can configure your browser to use the proxy `http://localhost:8888`. While running, this proxy also redirects external URLs.
A browser extension like [SwitchOmega for Chrome](https://github.com/FelisCatus/SwitchyOmega) might be useful for conditional proxy usage.