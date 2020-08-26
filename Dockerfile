FROM rocker/binder:3.6.3

ARG NB_USER
ARG NB_UID

USER root
COPY . ${HOME}
RUN pip install --no-cache-dir -r ./dependencies/requirements.txt
RUN R -e 'source("./dependencies/installPackages.R")'
RUN chown -R ${NB_USER} ${HOME}

USER ${NB_USER}
