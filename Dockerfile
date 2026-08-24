# NOTE: this Dockerfile has not been rebuilt and smoke-tested since this update.
# See learners/setup.md ("Running in a sandbox") before relying on it for a workshop.

# Debian slim base. Claude Code's native installer does not depend on Node.js,
# so we don't need a Node base image here.
FROM debian:bookworm-slim

# Install Python and other necessary tools (curl and ca-certificates are
# required for the Claude Code installer below).
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set up a non-root user for security
RUN useradd -m -s /bin/bash researcher
USER researcher
WORKDIR /home/researcher/project

# Install Claude Code with the native installer.
RUN curl -fsSL https://claude.ai/install.sh | bash
ENV PATH="/home/researcher/.local/bin:${PATH}"

# Install the lesson's Python dependencies (--break-system-packages: Debian's
# system Python blocks a bare pip install; this is a throwaway container image,
# not a shared system, so that's an acceptable tradeoff here).
RUN python3 -m pip install --user --break-system-packages pandas matplotlib

# Default command
CMD ["bash"]
