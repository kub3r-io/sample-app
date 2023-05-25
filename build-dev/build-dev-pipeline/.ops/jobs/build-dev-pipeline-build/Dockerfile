############################
# Final container
############################
FROM registry.cto.ai/official_images/pipeline-base
WORKDIR /ops

ADD --chown=ops:9999 . .
RUN mv docker.sh $(which docker)

RUN bash -c "./dependencies.sh"

USER ops
ENV USER ops
ENV HOME /ops
ENV XDG_RUNTIME_DIR=/run/ops/9999
