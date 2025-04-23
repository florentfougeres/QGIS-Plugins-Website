FROM registry.gitlab.com/oslandia/qgis/pyqgis-4-checker/pyqgis-qt-checker:latest
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# Need to change 
WORKDIR /celery_task
RUN python3 -m ensurepip && python3 -m pip install celery
CMD ["celery -A plugins worker -Q qgis --loglevel=DEBUG"]
