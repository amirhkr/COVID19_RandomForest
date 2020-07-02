FROM jupyter/scipy-notebook
WORKDIR /COVID19_RandomForest

USER root
RUN sudo apt-get update
RUN sudo apt-get install -y wget htop vim unzip procps

# Copy host env to docker env
COPY . .
WORKDIR .

USER jovyan
# Instantiate conda from env
RUN conda env create -f env.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "COVID19_RandomForest", "/bin/bash", "-c"]

# Run jupyterlab
# CMD ["conda", "run", "-n", "COVID19_RandomForest", "jupyter", "lab", "--allow-root", "--port=8008", "--ip=0.0.0.0", "--no-browser"]

