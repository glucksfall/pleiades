# Use the anaconda3 image as parent image
FROM continuumio/anaconda3

# set shell
RUN export SHELL=/bin/bash

# Update
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update
RUN apt-get install -y dialog apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y htop git gcc

# Install pleiades
RUN python3 -m pip install pleiades

# Install pyvipr
RUN python3 -m pip install pyvipr

# Install jupyter notebook extensions
RUN python3 -m pip install jupyter_nbextensions_configurator nbserverproxy

# Install simulators
RUN conda install -c alubbock kappa
RUN conda install -c alubbock bionetgen
RUN conda install -c alubbock nfsim
RUN conda install -c alubbock stochkit

RUN export KAPPAPATH=/opt/conda/bin
RUN export BNGPATH=/opt/conda/bin
RUN export STOCHKITPATH=/opt/conda/bin

# set common aliases
RUN alias kasim4=KaSim
RUN alias kasa=KaSa
RUN alias bng2=BNG2.pl
RUN alias nfsim=NFsim

# Download the Atlas tutorial
RUN mkdir -p /opt/notebooks/Atlas-tutorial
WORKDIR /opt/notebooks/Atlas-tutorial
RUN git init
RUN git remote add -f origin https://github.com/networkbiolab/atlas
RUN git config core.sparseCheckout true
RUN echo "tutorial" >> .git/info/sparse-checkout
RUN git pull origin master
RUN mv tutorial/* .
RUN rm -rf tutorial .git

# Set the working directory
WORKDIR /opt/notebooks

# Set jupyter configuration
RUN jupyter notebook --generate-config
RUN wget https://raw.githubusercontent.com/glucksfall/pleiades/master/jupyter_notebook_config.json --directory-prefix=/root/.jupyter

# Initiate jupyter server at runtime
CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
