# FROM condaforge/mambaforge:latest
# COPY ./ /tmp/hello_planet

# RUN mamba install --yes python=3.8 \
#     && pip install -e /tmp/hello_planet

# ENTRYPOINT [ "data_harvest", "ooi", "run" ]

FROM prefecthq/prefect:2-python3.10

COPY ./ /tmp/hello_planet

RUN pip install -e /tmp/hello_planet

# RUN mv /tmp/hello_planet/flow_configs /opt/flow_configs
