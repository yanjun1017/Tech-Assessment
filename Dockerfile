FROM jupyter/datascience-notebook:628fbcb24afd

MAINTAINER Yanjun Li, yanjun9876@gmail.com

WORKDIR /home/joyvan/Tech-Assessment 

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential python-dev
RUN apt-get install -y python python-distribute python-pip
RUN pip install pip --upgrade
RUN find . -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output {} \;
RUN find . -name '*.ipynb' -exec ipython trust {} \;
CMD jupyter notebook --no-browser --ip 0.0.0.0 --port 80 /notebooks
VOLUME /home/joyvan/Tech-Assessment 
