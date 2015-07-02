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

