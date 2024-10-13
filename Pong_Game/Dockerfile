# Using an official Python runtime as a parent image
FROM python:3.9-slim

# Setting working directory
WORKDIR /home/player

# Copying project files into the Docker image
COPY . /home/player

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:0
ENV HOME=/home/player

# Installing Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    

# Installing necessary packages
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    git \
    supervisor \
    websockify \
    fonts-liberation \
    net-tools \
    sudo \
    vim \
    && rm -rf /var/lib/apt/lists/*


# Cloning the noVNC repository and create the symlink to launch.sh
RUN git clone https://github.com/novnc/noVNC.git /usr/share/novnc \
    && ln -s /usr/share/novnc/utils/launch.sh /usr/bin/novnc
    

# Create user
RUN useradd -m -d /home/player -s /bin/bash player


# Setting proper permissions
RUN chmod -R 755 /home/player
RUN chown -R player:player /home/player
RUN mkdir -p /home/player/.cache/pip && chown -R player:player /home/player/.cache


# Copying the supervisord.conf file to /etc/
COPY supervisord.conf /etc/supervisord.conf

# Expose necessary ports
EXPOSE 5000 8000

# Run the startup script
CMD ["/home/player/startup.sh"]

