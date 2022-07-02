FROM python:3

RUN pip install flask && \
    pip install jsonify


EXPOSE 7600

# add startup script
COPY ./entrypoint.py /
RUN chmod +x /entrypoint.py

CMD [ "python", "./entrypoint.py" ]
