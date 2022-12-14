FROM python:3.9

ARG project_dir=/workspace
WORKDIR $project_dir
COPY ./ $project_dir

# dbが立ち上がるまで待機する機能の追加
# https://github.com/ufoscout/docker-compose-wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=/root/.local/bin:$PATH \
    POETRY_VIRTUALENVS_PATH=$project_dir \
    POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry install --no-interaction

RUN echo 'poetry shell' >> ~/.bashrc

CMD /wait && poetry run python3 -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
