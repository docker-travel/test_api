
sudo apt install  iptables
sudo sh -c "$(curl -fsSL https://get.docker.com)"
sudo usermod -aG docker $USER
docker run hello-world
sudo nano /lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375

systemctl daemon-reload
docker run -d -p  hello-world

ssh root@127.0.0.1 -p 2222


sed '/-H/s/ExecStart/"ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375"/g' testfile 
sed 's/thpaper is line2/bbb/' source > tmp.txt

sudo reboot
netstat -ltp
curl 127.0.0.1:4444/info
curl 127.0.0.1:2375/info
curl 127.0.0.1:9487/info
curl 127.0.0.1:5487/info
curl 127.0.0.1:8591/info
tcp        0      0 localhost:9487          0.0.0.0:*               LISTEN
sudo apt update
sudo apt install nginx
sudo ufw app list
systemctl status nginx
curl -4 icanhazip.com
sudo mkdir -p /var/www/example.com/html
sudo chown -R $USER:$USER /var/www/example.com/html
sudo chmod -R 755 /var/www/example.com
nano /var/www/example.com/html/index.html
sudo nano /etc/nginx/sites-available/example.com
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
sudo nano /etc/nginx/nginx.conf
sudo nginx -t
sudo systemctl restart nginx
nano /var/www/example.com/html/index.html
docker pull gotechnies/alpine-ssh
conta
docker run -d -p 2222:22 arvindr226/alpine-ssh
docker ps
docker stop cc2d64ab3782
docker run -d -p 2222:22 -p 4444:2375 arvindr226/alpine-ssh
ssh root@127.0.0.1 -p 2222
docker run hello-world
docker ps
docker run -it ubuntu bash
sudo apt-get install ssmtp mailutils
sudo cp /etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf.default
nano /etc/ssmtp/ssmtp.conf
sudo nano /etc/ssmtp/ssmtp.conf
echo "This is a test" | ssmtp sddivid@gmail.com
ls
history