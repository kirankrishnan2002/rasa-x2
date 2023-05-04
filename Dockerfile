# Extend the official Rasa SDK image
ARG DOCKER_IMAGE_TAG
FROM rasa/rasa-sdk:2.8.6

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
#COPY actions/actions_req.txt ./actions
COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
#RUN pip install -r ./actions/actions_req.txt
RUN pip install -r requirements-actions.txt
#DOCKER_IMAGE_TAG = "v1.0.0"

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
