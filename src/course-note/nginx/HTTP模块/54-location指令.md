# location指令

# 示例

```c
server {
    server_name localhost
    error_log  logs/error.log  debug
    # root html/;
    default_type text/plain
    merge_slashes off

    location ~ / Test1 /$ {
        return 200 'first regular expressions match!\n'
    }

    location ~* / Test1/(\w+)$ {
        return 200 'longest regular expressions match!\n'
    }

    location ^ ~ / Test1 / {
        return 200 'stop regular expressions match!\n'
    }

    location / Test1/Test2 {
        return 200 'longest prefix string match!\n'
    }

    location / Test1 {
        return 200 'prefix string match!\n'
    }


    location = /Test1 {
        return 200 'exact match!\n'
    }

}

```

精确匹配

```bash
~/geek/nginx » curl localhost/Test1
exact match!
```

最长匹配规则匹配到了禁止正则

```bash
~/geek/nginx » curl localhost/Test1/
stop regular expressions match!
```

最长匹配未禁止正则 按照顺序匹配到了正则表达式

```bash
~/geek/nginx » curl localhost/Test1/Test2
longest regular expressions match!
```

正则表达式都没有匹配 最长前缀匹配了

```bash
~/geek/nginx » curl localhost/Test1/Test2/                           
longest prefix string match!

```