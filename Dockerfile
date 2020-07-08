FROM debian

# Debian is similiar to Ubuntu
# Set env var so logging works.

ENV PYTHONUNBUFFERED = 1

# You can Run things, mostly dependencies.

RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install scikit-learn && \
  pip3 install category-encoders && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-robdbennett && \
  python3 -c "import lambdata_robdbennett; print(lambdata_robdbennett.TEST)"

