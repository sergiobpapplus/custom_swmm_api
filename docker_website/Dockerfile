FROM python:3.10-slim-bullseye
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y\
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends pandoc proj-bin

RUN apt-get install git -y

# RUN  update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN pip3 install --upgrade pip

RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install tqdm
RUN pip3 install networkx
RUN pip3 install fastparquet
RUN pip3 install matplotlib
RUN pip3 install Shapely
RUN pip3 install pyproj
RUN pip3 install Rtree
RUN pip3 install geopandas
RUN pip3 install ipython!=8.7.0  # jupyter syntax highlighting
RUN pip3 install ipykernel  # jupyter autorun for docs
RUN pip3 install sphinx
RUN pip3 install nbsphinx
RUN pip3 install myst-parser  # recommonmark  # markdown
RUN pip3 install SWMM_xsections_shape_generator
RUN pip3 install pydata_sphinx_theme
RUN pip3 install pyswmm
RUN pip3 install python-semantic-release

RUN useradd -ms /bin/bash mp;
RUN chmod g+rw /home && \
    mkdir -p /home/mp && \
    chown -R mp:mp /home/mp

ENV HOME /home/mp
WORKDIR /home/mp

ENV SHELL /bin/bash

USER mp

ENV PATH /home/mp/.local/bin/:$PATH