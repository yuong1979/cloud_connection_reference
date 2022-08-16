
#################################################################################
#################################################################################
############################ STREAMLIT APP ######################################
#################################################################################
#################################################################################

###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
###### ###### ###### Local (NOT WORKING) ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######

##### local #####
# docker build -t streamlitapp .
# docker run -p 8501:8501 streamlitapp
##### delete images and containers #####
# docker rmi -f $(docker images -aq)
# docker rm -vf $(docker ps -aq)

# FROM python:3.8
# WORKDIR /app
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
# EXPOSE 8501
# COPY . /app
# ENTRYPOINT ["streamlit", "run"]
# CMD ["app.py"]

###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######
###### ###### ###### Production ###### ###### ###### ###### ###### ##### ###
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ######

##### instructions to connect to environment variables on GCP #####
# https://youtu.be/JIE89dneaGo

# gcloud builds submit --tag gcr.io/testing-33c79/streamlitapp --project=testing-33c79
# gcloud run deploy streamlitapp --image gcr.io/testing-33c79/streamlitapp --platform managed --project=testing-33c79 --allow-unauthenticated --region us-east1

FROM python:3.8

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

EXPOSE 8080

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

CMD streamlit run --server.port 8080 --server.enableCORS false app.py