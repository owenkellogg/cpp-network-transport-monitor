FROM ubuntu

WORKDIR /opt/app

RUN apt update
RUN apt install -y cmake ninja-build python3 python3-pip
RUN pip install conan
RUN conan profile detect

COPY . /opt/app

RUN conan install --build=missing .

