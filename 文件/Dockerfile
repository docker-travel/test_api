FROM alpine:3.5
MAINTAINER Arvind Rawat <arvindr226@gmail.com>

RUN apk --update add --no-cache openssh bash \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd \
  && rm -rf /var/cache/apk/*
RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config
RUN sed -ri 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]



{
  "ExposedPorts": {
    "27017/tcp": {},
    "28017/tcp": {}
  },
  "Image": "tutum/mongodb",
  "HostConfig": {
    "PortBindings": {
      "27017/tcp": [
        {
          "HostIp": "",
          "HostPort": "27017"
        }
      ],
      "28017/tcp": [
        {
          "HostIp": "",
          "HostPort": "28017"
        }
      ]
    }
  }
}
ƒ




RUN "apk","--update","add","--no-cache","openssh","bash","\ ",
  "&&","sed","-i","s/#PermitRootLogin.*/PermitRootLogin\ ","yes/","/etc/ssh/sshd_config","\ ",
  "&&","echo","'root:root'","|","chpasswd"," \ ",
  "&&","rm","-rf","/var/cache/apk/*"
RUN "sed","-ie","'s/#Port 22/Port 22/g'","/etc/ssh/sshd_config"
RUN "sed","-ri","'s/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g'","/etc/ssh/sshd_config"
RUN "sed","-ir","'s/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g'","/etc/ssh/sshd_config"
RUN "sed","-ir","'s/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g'","/etc/ssh/sshd_config"
RUN "sed","-ir","'s/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g'","/etc/ssh/sshd_config"
RUN "sed","-ir","'s/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g'","/etc/ssh/sshd_config"
RUN "/usr/bin/ssh-keygen","-A"
RUN "ssh-keygen","-t","rsa","-b","4096","-f" , "/etc/ssh/ssh_host_key"
