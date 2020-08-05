FROM rocker/shiny-verse:3.6.3

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jre && \
    apt-get install wget
    
# add requirements.txt, written this way to gracefully ignore a missing file
COPY . .

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN rm get-pip.py


RUN ([ -f requirements.txt ] \
    && pip3 install --no-cache-dir -r requirements.txt) \
        || pip3 install --no-cache-dir jupyter jupyterlab


USER root


# Set up the user environment

ENV NB_USER jovyan
ENV NB_UID 1000
ENV HOME /home/$NB_USER

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid $NB_UID \
    $NB_USER

COPY . $HOME
RUN chown -R $NB_UID $HOME

USER $NB_USER

# Launch the notebook server
WORKDIR $HOME
CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]
