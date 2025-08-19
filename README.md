## Project Outline

### /
The root of this project contains a `Dockerfile`, `docker-compose.yml` and, `nginx.conf`

The `Dockerfile` provides a very simple setup for a custom `nginx` system.

The `nginx.conf` contains a complex `nginx` configuration that can interpret multiple different origin domain requests, and proxy them to different hosts or services that may exist on the machine.

Configuration is to have multiple services hosted on 1 machine, with multiple ports. `nginx` then makes use of the originating URL to determine to which service / port the user connection should be directed.

The `docker-compose.yml` utilizes Docker's advanced compose feature to spin up multiple containers that can be referenced within the `nginx.conf`. This allows for a simple demonstration of how the service would function.

### /server 
The `/server` directory of this project contains a `Dockerfile`, `docker-compose.yml`, and executable `run.sh`

The `Dockerfile` provides a simple `nc` based port listener by executing the `run.sh` script that simply calls netcat to echo some simulated information out to the user for testing.

The `docker-compose.yml` file provides a way to test a single instance of the `server` listener at once.

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
# ^C
curl gold-server.local
# ^C
curl silver-lining.local
# ^C
curl cupric.local
```

## Contributions
Further documentation and improvements to how the code may be written are welcome.

