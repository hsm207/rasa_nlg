FROM rasa/rasa:2.8.4-full

USER root
RUN apt update && \
    apt install -y git \
        make \
        wget

RUN pip install black \
    fastapi==0.68.1 \
    uvicorn[standard] \
    ipywidgets \
    jupyterlab \
    transformers[torch]==4.10.0