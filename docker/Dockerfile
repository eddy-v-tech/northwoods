FROM python:3.9
ADD docker/requirements.txt /
RUN pip install -r requirements.txt
COPY ../app /
RUN ls
ENTRYPOINT [ "python", "babysitting_calc_app.py" ]