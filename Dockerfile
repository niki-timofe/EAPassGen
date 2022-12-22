ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-alpine AS base
EXPOSE 8000

ENV VIRTUAL_ENV=/app/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

FROM base as build
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM base as final

WORKDIR /app

COPY --from=build /app ./

ENTRYPOINT ["gunicorn"]
CMD ["gensite:app", "-b", "0.0.0.0:8000"]