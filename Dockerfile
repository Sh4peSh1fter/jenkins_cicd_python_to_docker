FROM jenkins/jenkins:lts-jdk11
# MAINTAINER sean_s
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml

COPY jenkins_plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
COPY casc.yaml /var/jenkins_home/casc.yaml

# RUN curl http://host.docker.internal:8080/jnlpJars/jenkins-cli.jar --output jenkins-cli.jar
COPY jenkins-cli.jar /jenkins-cli.jar
RUN mkdir /var/jenkins_home/test
COPY test.xml /var/jenkins_home/test/config.xml
# RUN java -jar jenkins-cli.jar -s http://127.0.0.1:8080 create-job test < /var/jenkins_home/test/config.xml

USER root

RUN apt-get update && \
    apt-get -y install python3