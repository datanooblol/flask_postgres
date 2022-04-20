FROM continuumio/miniconda3


COPY conda_requirements.txt .

RUN conda install -y --file conda_requirements.txt

COPY ./app /app

WORKDIR /app

# COPY pip_requirements.txt .

# RUN pip3 install -r pip_requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
