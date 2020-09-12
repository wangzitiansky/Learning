# 编译Nginx

### 下载Nginx源代码

先将`Nginx`的源代码下载下来
```bash
wget http://nginx.org/download/nginx-1.19.2.tar.gz
```

将`Nginx`的源代码解压缩
```bash
tar -xzf nginx-1.19.2.tar.gz
```

进入`Nginx`目录
```bash
cd nginx-1.19.2/
```

查看各个目录
```bash
root@iZ2zeeq1jai7e7ypku5kakZ:~/geek/nginx-1.19.2# ll
total 800
drwxr-xr-x 8 1001 1001   4096 Aug 11 22:52 ./
drwxr-xr-x 3 root root   4096 Sep 12 10:27 ../
drwxr-xr-x 6 1001 1001   4096 Sep 12 10:27 auto/
-rw-r--r-- 1 1001 1001 305589 Aug 11 22:52 CHANGES
-rw-r--r-- 1 1001 1001 466546 Aug 11 22:52 CHANGES.ru
drwxr-xr-x 2 1001 1001   4096 Sep 12 10:27 conf/ # 示例文件
-rwxr-xr-x 1 1001 1001   2502 Aug 11 22:52 configure* # 生成中间文件
drwxr-xr-x 4 1001 1001   4096 Sep 12 10:27 contrib/ # 里面有 vim 高亮工具
drwxr-xr-x 2 1001 1001   4096 Sep 12 10:27 html/ # 提供了标准 HTML 文件
-rw-r--r-- 1 1001 1001   1397 Aug 11 22:52 LICENSE
drwxr-xr-x 2 1001 1001   4096 Sep 12 10:27 man/ # Linux 的帮助文件
-rw-r--r-- 1 1001 1001     49 Aug 11 22:52 README
drwxr-xr-x 9 1001 1001   4096 Sep 12 10:27 src/ # 源代码
```

配置vim查看配置文件时的语法高亮
```bash
cp -r contrib/vim/* ~/.vim/
```

### 安装依赖

安装所需的第三方依赖
```bash
apt-get install libpcre3 libpcre3-dev
apt-get install zlib1g-dev
```

### Configure

`configure` 生成中间文件 这里的路径是nginx编译好之后的路径
```bash
./configure --prefix=/root/geek/nginx
```

`objs` 文件中的 `ngx_modules.c` 决定编译时候哪些模块会被编译进 Nginx

```c
#include <ngx_config.h>
#include <ngx_core.h>



extern ngx_module_t  ngx_core_module;
extern ngx_module_t  ngx_errlog_module;
extern ngx_module_t  ngx_conf_module;
extern ngx_module_t  ngx_regex_module;
extern ngx_module_t  ngx_events_module;
extern ngx_module_t  ngx_event_core_module;
extern ngx_module_t  ngx_epoll_module;
extern ngx_module_t  ngx_http_module;
extern ngx_module_t  ngx_http_core_module;
extern ngx_module_t  ngx_http_log_module;
extern ngx_module_t  ngx_http_upstream_module;
extern ngx_module_t  ngx_http_static_module;
extern ngx_module_t  ngx_http_autoindex_module;
extern ngx_module_t  ngx_http_index_module;
extern ngx_module_t  ngx_http_mirror_module;
extern ngx_module_t  ngx_http_try_files_module;
extern ngx_module_t  ngx_http_auth_basic_module;
extern ngx_module_t  ngx_http_access_module;
extern ngx_module_t  ngx_http_limit_conn_module;
extern ngx_module_t  ngx_http_limit_req_module;
extern ngx_module_t  ngx_http_geo_module;
extern ngx_module_t  ngx_http_map_module;
```

### 编译

在`nginx-1.14.2`目录编译
```bash
make
```

编译好的二进制文件在`objs`文件中

### 安装

安装
```
make install
```

之后进入`prefix`指定的按照目录下会看到以下文件

```bash
root@iZ2zeeq1jai7e7ypku5kakZ:~/geek/nginx# ll
total 24
drwxr-xr-x 6 root root 4096 Sep 12 10:42 ./
drwxr-xr-x 4 root root 4096 Sep 12 10:34 ../
drwxr-xr-x 2 root root 4096 Sep 12 10:42 conf/ # 配置文件
drwxr-xr-x 2 root root 4096 Sep 12 10:42 html/ # 
drwxr-xr-x 2 root root 4096 Sep 12 10:42 logs/ # 日志
drwxr-xr-x 2 root root 4096 Sep 12 10:42 sbin/ # 二进制文件
```