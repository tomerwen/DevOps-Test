FROM openjdk:8-jre-alpine

EXPOSE 8080

COPY./target/helloworld-0.0.1-SNAPSHOT.jar /usr/app/
WORKDIR /usr/app

CMD java -jar helloworld-0.0.1-SNAPSHOT.jar
