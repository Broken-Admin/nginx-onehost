## Project Outline

### NGINX Documentation
See [here](https://nginx.org/en/docs/http/server_names.html) for official NGINX documentation regarding server names.

### `/`
The root of this project contains a `Dockerfile`, `docker-compose.yml` and, `nginx.conf`

The `Dockerfile` provides a very simple setup for a custom `nginx` system.

The `nginx.conf` contains a complex `nginx` configuration that can interpret multiple different origin domain requests, and proxy them to different hosts or services that may exist on the machine.

Configuration is to have multiple services hosted on 1 machine, with multiple ports. `nginx` then makes use of the originating URL to determine to which service / port the user connection should be directed.

The `docker-compose.yml` utilizes Docker's advanced compose feature to spin up multiple containers that can be referenced within the `nginx.conf`. This allows for a simple demonstration of how the service would function.

### `/server` 
The `/server` directory of this project contains a `Dockerfile`, `docker-compose.yml`, and executable `server.py`

The `Dockerfile` provides a simple `python3` based port listener by executing the `server.py` script that provides "Hello, world!" as output to the user for testing.

The `docker-compose.yml` file provides a way to test a single instance of the `server` listener at once.

The `server.py` script provides a very simple HTTP server utilizing Python's built-in http.server module.

## Running the project

Prior to running the project it is necessary to update the user's `/etc/hosts/` file with the following:
```
127.0.0.1 gold-server.local 
127.0.0.1 silver-lining.local
127.0.0.1 cupric.local
```
These lines will update the local DNS server to resolve the provided domains to the localhost.

In order to run the project, simply navigate to the root of the project on a Docker-compatible machine, and run `docker compose up --build`.

It is then possible to run the following commands, and watch the output of the terminal you ran `docker compose` in.
```bash
curl localhost
# - Hello, world!
# docker compose shows logs from local
curl gold-server.local
# - Hello, world!
# docker compose shows logs from gold
curl silver-lining.local
# - Hello, world!
# docker compose shows logs from silver
curl cupric.local
# - Hello, world!
# docker compose shows logs from copper
```

## Contributions
Further documentation and improvements to how the code may be written are welcome.

