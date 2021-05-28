FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
	sudo \
	wget \
	vim 
WORKDIR /opt
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh && \
	sh /opt/Miniconda3-py39_4.9.2-Linux-x86_64.sh -b -p /opt/miniconda3 && \
	rm -f Miniconda3-py39_4.9.2-Linux-x86_64.sh

ENV PATH /opt/miniconda3/bin:$PATH

RUN pip install --upgrade pip && \
	conda config --add channels defaults && \
	conda config --add channels conda-forge && \
	conda config --add channels bioconda && \
	conda install biopython && \
	conda install rdkit && \
	conda install scikit-learn && \
	conda install lightgbm && \
	conda install optuna && \
	conda install pytorch && \
	conda install xgboost && \
	conda install xlrd && \
	conda install openpyxl && \
	conda install -c rdkit -c mordred-descriptor mordred && \
	conda install -c conda-forge networkx=2.5

WORKDIR /