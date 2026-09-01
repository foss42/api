# MQTT test rig

A self-contained, local MQTT broker (Eclipse Mosquitto + a small test
publisher) for exercising API Dash's MQTT client -- QoS 1/2, retained messages,
wildcards, TLS, auth and MQTT v5. It is **not** part of the hosted Open Source
APIs; it only runs locally via Docker.

## Setup & run the broker

```bash
docker compose -f mqtt/docker-compose.yml up --build
```

Listeners: `1883` (plain, anonymous), `9001` (WebSocket), `8883` (TLS,
self-signed), `1884` (auth -- `testuser` / `testpass`).

## Run the tests

```bash
pip install -r mqtt/requirements-dev.txt
pytest mqtt/tests
```

The suite **skips gracefully** when paho-mqtt is missing or no broker is
reachable on `localhost:1883`.

See [`docs/mqtt/`](../docs/mqtt/) for the per-feature pages.
