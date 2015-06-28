FROM ubuntu:14.04
MAINTAINER Ivar Refsdal <refsdal.ivar@gmail.com>

RUN apt-get -qq update
RUN apt-get -y install curl git vim ruby gem ruby-dev libcurl3-dev

RUN curl -sk https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
RUN git clone https://github.com/torch/distro.git ~/torch --recursive
RUN cd ~/torch; ./install.sh

RUN /root/torch/install/bin/luarocks install nngraph
RUN /root/torch/install/bin/luarocks install optim

RUN git clone https://github.com/karpathy/char-rnn.git

RUN git clone https://github.com/ivarref/hdo-transcript-search.git
WORKDIR /hdo-transcript-search/indexer
RUN gem install bundler
RUN bundle install
RUN bundle exec ruby -Ilib bin/hdo-transcript-indexer --download-and-convert-only

WORKDIR /hdo-transcript-search
ADD load_disk.py load_disk.py
RUN python load_disk.py Heikki Holmås

RUN mkdir -p /char-rnn/data/hdo
RUN cp -v ./input.txt /char-rnn/data/hdo/.

WORKDIR /char-rnn
VOLUME ["/opt/cv"]
ENV TERM screen-256color
RUN /root/torch/install/bin/th train.lua -checkpoint_dir /opt/cv -data_dir data/hdo -gpuid -1 -rnn_size 512 -num_layers 2 -dropout 0.5

ADD find_lowest_checkpoint.py find_lowest_checkpoint.py
RUN chmod +x ./find_lowest_checkpoint.py

