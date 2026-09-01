# gRPC test rig

A self-contained, local gRPC test server (`apidash.test.TestService`) for
exercising API Dash's gRPC client -- reflection, unary, all three streaming
modes, metadata, auth-via-metadata and error codes. It is **not** part of the
hosted Open Source APIs; it only runs locally via Docker.

## Setup & run the server

```bash
docker compose -f grpc/docker-compose.yml up --build
```

Serves on `localhost:9000` (plaintext) and `localhost:9001` (TLS, self-signed).

## Run the tests

```bash
pip install -r grpc/requirements-dev.txt
pytest grpc/tests
```

The suite generates the Protobuf stubs on the fly and **skips gracefully** when
grpcio/-tools are missing or no server is reachable on `localhost:9000`.

See [`docs/grpc/`](../docs/grpc/) for the per-feature pages.
