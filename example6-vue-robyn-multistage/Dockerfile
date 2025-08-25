# Stage 1: Build the frontend
# The platform is hardcoded because bun does not support armv7. The result of this build is architecture agnostic.
FROM --platform=amd64 oven/bun:1 AS frontend
WORKDIR /app

# Copy necessary files for bun install
COPY bun.lock package.json vite.config.js ./
RUN bun install

# Copy frontend files for build
COPY ./src ./src
COPY index.html ./
RUN bun run build

# Stage 2: Build the backend
FROM python:3.12-slim-bookworm AS backend
WORKDIR /app

RUN apt update && apt install -y curl

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Necessary for running uv sync
ENV PATH="/root/.local/bin/:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv sync

COPY --from=frontend /app ./
COPY . .

ENV PATH="/app/.venv/bin:$PATH" \
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


CMD ["python", "-m", "main"]
