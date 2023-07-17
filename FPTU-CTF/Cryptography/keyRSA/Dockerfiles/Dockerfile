FROM python:3.10

RUN pip install pycryptodome
RUN useradd -m ctf

COPY ./enc.py /home/ctf/enc.py
RUN chmod +x /home/ctf/enc.py

RUN chown -R root:root /home/ctf
RUN chmod -R 755 /home/ctf

WORKDIR /home/ctf

CMD ["python3","enc.py"]

EXPOSE 5000
