## 编译Nginx

### 下载Nginx源代码

先将Nginx的源代码下载下来
```bash
wget http://nginx.org/download/nginx-1.14.2.tar.gz
```

将Nginx的源代码解压缩
```bash
tar -xzf nginx-1.14.2.tar.gz
```

进入Nginx目录
```bash
cd nginx-1.14.2/
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

configure生成中间文件 这里的路径是nginx编译好之后的路径
```bash
./configure --prefix=/home/wzt/nginx
```

### 编译

在nginx-1.14.2目录编译
```bash
make
```

### 安装

安装
```
make install
```
