
FROM ubuntu:16.04

# Update the repository sources list
# Install base packages: git, python2/3, java
RUN apt-get update && apt-get install -y \
    libncurses5-dev \
    libncursesw5-dev \
    libcurl4-openssl-dev \
    libfreetype6-dev \
    zlib1g-dev \
    python \
    python-setuptools \
    python-pip \
    python3 \
    python3-setuptools \
    python3-pip \
    git \
    wget \
    unzip \
    ghostscript \
    pkg-config \
    libboost-dev \
    default-jre \
    apt-transport-https \
&& rm -rf /var/lib/apt/lists/*

# Make directory for all softwares
RUN mkdir /software
WORKDIR /software
ENV PATH="/software:${PATH}"

RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip
RUN unzip Trimmomatic-0.38.zip && rm Trimmomatic-0.38.zip

RUN mkdir -p demo-pipeline/src
COPY /src demo-pipeline/src
ENV PATH="/software/demo-pipeline:/software/demo-pipeline/src:${PATH}"

ENTRYPOINT ["/bin/bash", "-c"]