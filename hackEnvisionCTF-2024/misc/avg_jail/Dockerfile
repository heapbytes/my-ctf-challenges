FROM python:3.11

RUN apt-get update && \
    apt-get install socat -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY src/chall.py /challenge/
WORKDIR /challenge

EXPOSE 1337
CMD socat -dd tcp-listen:1337,fork,reuseaddr,su=nobody exec:"python3 -u chall.py"
