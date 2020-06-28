# root和alias

Nginx核心知识100讲课程笔记:books:
课程链接 [:mortar_board:](https://time.geekbang.org/course/detail/100020301-72403)

### 基本信息

+ 功能均为将url映射为文件路径，返回静态文件内容

+ 格式

```bash
alias path

root path
```

### 区别

+ root会映射完整url，会将location匹配的部分，追加到path后面

+ alias出现在location块中 root可以出现在http,server,location, if in location

+ alias无默认值 root默认值为root html

### 示例

配置文件
```c
server {
	server_name static.taohui.tech;
	error_log  logs/myerror.log  info;
	
	location /root {
		root html;
	}

	location /alias {
    		alias html;
	}

	location ~ /root/(\w+\.txt) {
		root html/first/$1;
	}

	location ~ /alias/(\w+\.txt) {
		alias html/first/$1;
	}

	location  /RealPath/ {
		alias html/realpath/;
                return 200 '$request_filename:$document_root:$realpath_root\n';
	}

}
# 此配置文件来自 https://github.com/russelltao/geektime-nginx/blob/master/examples/static.conf
```

文件目录

```bash
/html/first/1.txt
```

测试1

```bash
curl localhost/root/
```

实际访问的地址

```bash
/home/sky/geek/nginx/html/root/index.html
# 分析
# 与第一个匹配 location /root
# 因为是root指令，所以html后面又加上了location中的root.因为后面有反斜杠,所以加上了index.html
```

测试2

```bash
curl localhost/root/1.txt
```

实际访问的地址

```bash
/home/sky/geek/nginx/html/first/1.txt/root/1.txt
# 分析
# 与location ~ /root/(\w+\.txt) 匹配
# 因为是root指令,会在html/first/1.txt,后面加上匹配到的root/1.txt
```

测试3

```bash
curl localhost/alias/
```

实际访问地址和结果

```bash
访问到了html/index.html 得到了默认的首页
```

测试4

```bash
curl hocalhost/alias/1.txt
```

实际访问地址和结果

```bash
~ » curl localhost/alias/1.txt                       
test1
# 分析 
# 匹配到了 location ~ /alias/(\w+\.txt)这个匹配项
# 因为alias并不会添加任何东西 所以访问到了/html/first/1.txt
```