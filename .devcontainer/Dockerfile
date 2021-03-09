# Dockerfile for Python package development
FROM buildpack-deps:focal

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

# Install Python 2.7 & Python 3.6+
# (Python 3.8 is included in the base image)
RUN apt update \
    && apt install --no-install-recommends -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt install --no-install-recommends -y \
    python3-pip \
    python2.7 \
    python3.6 \
    python3.7 \
    # python3.8 \
    python3.9

# Install Python packages for package development
RUN pip3 install \
    sphinx==3.5.2 \
    myst-parser \
    tox
