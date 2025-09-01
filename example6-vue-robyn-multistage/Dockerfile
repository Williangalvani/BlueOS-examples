# Stage 1: Build the frontend
# The platform is hardcoded because bun does not support armv7. The result of this build is architecture agnostic.
FROM --platform=amd64 oven/bun:1 AS frontend_amd64
WORKDIR /frontend
COPY ./frontend /frontend
RUN bun install
RUN bun run build


# Stage 2: Build the backend
FROM python:3.11-slim-bookworm AS backend
RUN apt update && apt install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*
WORKDIR /backend

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Necessary for running uv sync
ENV PATH="/root/.local/bin/:$PATH"

# This avoids this layer rebuilding when the backend code changes
COPY ./backend/pyproject.toml ./backend/uv.lock ./

RUN pip install . --extra-index-url https://piwheels.org/simple
COPY ./backend .

COPY --from=frontend_amd64 /frontend/dist /frontend

ENV PATH="/backend/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

LABEL version="1.0.0"
LABEL permissions='{\
    "ExposedPorts": {\
    "80/tcp": {}\
    },\
    "HostConfig": {\
    "PortBindings": {\
        "80/tcp": [\
        {\
            "HostPort": ""\
        }\
        ]\
    }\
    }\
}'
LABEL authors='[\
    {\
        "name": "Nicole Schmidt",\
        "email": "nicole@bluerobotics.com"\
    }\
]'
LABEL company='{\
        "about": "",\
        "name": "Blue Robotics",\
        "email": "support@bluerobotics.com"\
    }'
LABEL type="example"
LABEL readme='https://raw.githubusercontent.com/nicoschmdt/BlueOS-examples/{tag}/example6-vue-robyn-multistage/README.md'
LABEL links='{\
        "website": "https://github.com/nicoschmdt/BlueOS-examples/",\
        "support": "https://github.com/nicoschmdt/BlueOS-examples/"\
    }'
LABEL requirements="core >= 1.3"


CMD ["python", "main.py"]
