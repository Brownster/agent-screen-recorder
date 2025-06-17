# Agent Screen Recorder

This repository contains a minimal prototype of a call center screen recording solution using a microservices architecture.

## Components

- **agent** - Lightweight screen capture agent that uploads screenshots to the storage service.
- **control_api** - REST API for registering agents and issuing start/stop commands.
- **storage_service** - Simple service that accepts uploaded screenshots and stores them.

## Running Tests

Install dependencies and run `pytest`:

```bash
pip install -r requirements.txt
pytest
```
