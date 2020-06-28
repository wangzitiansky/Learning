# limit_conn

### 指令基本信息

+ 生效阶段

NGX_HTTP_PREACCESS_PHASE阶段

+ 定义共享内存

```c
limit_conn_zone key值 zone=名字:大小
在http模块生效
```

+ 限制并发连接数

```c
limit_conn zone number;
http server location模块均生效
```

+ 限制日志级别

```c
limit_conn_log_level info | notice | warn | error
http, server, location 模块均生效
```

+ 限制向用户发送的错误码

### 示例

```c
limit_conn_zone $binary_remote_addr zone=addr:10m; # 定义一个用于限制连接的共享内存

server {
	server_name limit.taohui.tech;
	root html/;
	error_log logs/myerror.log info;
	
	location /{
		limit_conn_status 500;
		limit_conn_log_level  warn;
		limit_rate 50;      # 返回速率
		limit_conn addr 1;  # 限制连接的数量
	}
}
```

开启两个连接，发现一个可以正常访问，另一个访问结果是500

```bash
~ » curl localhost                                      sky@sky-virtual-machine
<html>
<head><title>500 Internal Server Error</title></head>
<body>
<center><h1>500 Internal Server Error</h1></center>
<hr><center>nginx/1.19.0</center>
</body>
</html>

```

```bash
~ » curl localhost                                                                        sky@sky-virtual-machine
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

```

查看myerror.log中打印出来的日志

```bash
2020/06/28 09:07:29 [warn] 58604#0: *17 limiting connections by zone "addr", client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.1", host: "localhost"
```
