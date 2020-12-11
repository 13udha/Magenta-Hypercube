# Running services locally in Docker Compose

## Requirements

- A recent version of `docker-compsose` that supports at least protocol version `2.1`.
  [installation instructions](https://docs.docker.com/compose/install/)
- A recent version of Docker
- Access to the Workbench.
- Configured access to the Docker registry. [Instructions](https://gard.telekom.de/gardwiki/display/SH/Docker)
- Some RAM to spare (about 250 MB per service)

## How it works

The services will be started in a Docker compose group with the same conatiner name as the service names in Openshift.
Additionally there is proxy container.
From the perspective of the proxy all services can be reached by their original hostname.
When the skill is started with `python manage.py -l run` on every request within a `ZipkinCircuitbreakerSession` the proxy
is used if the hostname starts and ends with `service`.

As a result the dockerized local services will be used without any change in the URL.

## Instructions

- Use a copy of the file `contrib/docker_services/docker_compose` from the SDK as a base.
- Remove the services from the file that your skill does *not* need. Make sure to keep the proxy and the text service.
- Startup the compose group with `docker-compose up`. This requires `docker-compose.yml` to be in the current working directory.
- Start your skill with the global `-l` / `--local` argument: `python manage.py -l run`

To end the docker group press `Ctrl` + `C`.

To retrieve new container versions use `docker-compose pull`

## Direct access

Every service has an expose port on localhost in the 808x area which is defined in the `docker-compose.yml` file.

You can also configure your browser to use the proxy ´http://localhost:8888`. The proxy will also redirect external URLs while running.
A browser extension like [SwitchOmega for Chrome](https://github.com/FelisCatus/SwitchyOmega) might be useful for conditional proxy usage.
