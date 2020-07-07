# Use the anaconda3 image as parent image
FROM continuumio/anaconda3

# Update
RUN apt-get install -y apt-utils
RUN apt-get update
RUN apt-get upgrade -y

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

# set common aliases
RUN alias kasim4=KaSim
RUN alias kasa=KaSa
RUN alias bng2=BNG2.pl
RUN alias nfsim=NFsim

# Set the working directory
RUN mkdir /opt/notebooks
WORKDIR /opt/notebooks

# Set jupyter configuration
RUN jupyter notebook --generate-config
RUN wget https://raw.githubusercontent.com/glucksfall/pleiades/master/jupyter_notebook_config.json --directory-prefix=/root/.jupyter

# Initiate jupyter server at run time
CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
