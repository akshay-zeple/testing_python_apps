# FROM image
# ADD /my/Test.java  /a/b/c/Test.java
# RUN apt-get install java
# ENV JAVA_HOME=/some/path
# WORKDIR /a/b/c
# EXPOSE 8050
# ENTRYPOINT sleep 5

# FROM alpine
# ENTRYPOINT date

# FROM alpine
# RUN apk add openjdk8
# ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/bin
# WORKDIR /usr/share/udemy
# ADD Test.java Test.java
# ENTRYPOINT javac Test.java && java Test 5


FROM ubuntu
RUN apt-get update && apt-get install -y python3
WORKDIR /akshay/testproject
ADD generate_random_number.py generate_random_number.py
ENTRYPOINT python3 generate_random_number.py
