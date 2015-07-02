FROM ubuntu:14.04
MAINTAINER Ivar Refsdal <refsdal.ivar@gmail.com>

RUN apt-get -qq update
RUN apt-get -y install curl git vim ruby gem ruby-dev libcurl3-dev python-numpy \
                       libicu-dev python-pip python-dev build-essential unzip
RUN pip install polyglot

RUN git clone https://github.com/ivarref/hdo-transcript-search.git
WORKDIR /hdo-transcript-search/indexer
RUN gem install bundler
RUN bundle install
RUN bundle exec ruby -Ilib bin/hdo-transcript-indexer --download-and-convert-only

RUN polyglot download embeddings2.no ner2.no
RUN mkdir -p /root/polyglot_data
RUN ln -sf /embeddings2 /root/polyglot_data/embeddings2
RUN ln -sf /ner2 /root/polyglot_data/ner2

WORKDIR /hdo-transcript-search
ADD load_disk.py load_disk.py
ADD parse.py parse.py

RUN python load_disk.py Heikki Holmås && python parse.py | sort -g > heikki.txt; cat ./heikki.txt | tail -n 10
RUN python load_disk.py Anders Anundsen && python parse.py | sort -g > anundsen.txt; cat ./anundsen.txt | tail -n 10
RUN python load_disk.py Erna Solberg && python parse.py | sort -g > solberg.txt; cat ./solberg.txt | tail -n 10

ADD toplists.py toplists.py
RUN chmod +x ./toplists.py
RUN ./toplists.py

