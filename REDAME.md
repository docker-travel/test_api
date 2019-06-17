
#客戶 docker node ssh tunnel 連線進 sever 的 SSH-container (走容器port:22) 2222:22 2375:2375
> ssh -R 2222:127.0.0.1:22  root@sddivid.tw -p 49154

> ssh -R 2375:127.0.0.1:2375  root@sddivid.tw -p 49154 ( 轉容器port:22 )

## server 端的 Flask API 建立 SSH-container 
> docker run -d -p { 可用 PORT }: 22 -p { 可用 PORT }: 2375 container
  
## 手機端APP 
### 透過 ssh 連到 客戶 server
> ssh   root@sddivid.tw -p { 可用PORT ( 對應 container 的 2222 port )}
### 透過http 連到 客戶 docker 
> curl  sddivid.tw/{ 可用PORT ( 對應 container 的 2375 port )}


這個8591 是container的8591 port 
透過http or ssh 連到 這個8591port