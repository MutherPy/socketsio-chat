FROM python:3.8.8
WORKDIR /socket_chat
ENV VIRTUAL_ENV=/virt
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD bash -c 'python main.py'
