## Dockerfile that generates an instance of www.longjj.com
FROM ubuntu:16.04
LABEL maintainer="longjj"
ENV LANG C


RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:0000' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

#py3F
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev locales\
  && pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]



EXPOSE 5000 2375  22
CMD ["app.py"]
CMD ["/usr/sbin/sshd", "-D"]




