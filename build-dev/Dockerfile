############################
# Final container
############################
FROM registry.cto.ai/official_images/python:2-3.7-buster-slim

WORKDIR /ops

ADD --chown=ops:9999 requirements.txt .

RUN pip3 install -r requirements.txt

ADD --chown=ops:9999 . .

##############################################################################
# As a security best practice the container will always run as non-root user.
##############################################################################
USER ops
