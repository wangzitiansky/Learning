# ls命令解析

### 命令格式

```shll
ls -l
```

### 字段分析

```shell
root@iZ2zeeq1jai7e7ypku5kakZ:~# ll
total 96
drwx------ 10 root root  4096 Jul 22 13:32 ./
drwxr-xr-x 23 root root  4096 Jun 18 20:09 ../
-rw-------  1 root root 16638 Jul 22 15:44 .bash_history
-rw-r--r--  1 root root  3106 Apr  9  2018 .bashrc
drwx------  3 root root  4096 Apr 26 16:29 .cache/
drwxr-xr-x 14 root root  4096 Jul 22 14:10 chipsec/
drwx------  3 root root  4096 Apr 26 16:24 .gnupg/
-rw-------  1 root root  7359 Jul 20 16:40 .mysql_history
drwxr-xr-x  3 root root  4096 Jun 18 14:55 nginx-tar/
drwxr-xr-x  2 root root  4096 Apr 26 16:29 .pip/
-rw-r--r--  1 root root   148 Aug 17  2015 .profile
-rw-r--r--  1 root root   206 Jun  8 10:44 .pydistutils.cfg
drwx------  2 root root  4096 Apr 26 08:30 .ssh/
drwxr-xr-x  6 root root  4096 Jun 25 18:36 .vim/
-rw-------  1 root root 16120 Jun 26 11:47 .viminfo
drwxr-xr-x  2 root root  4096 Jul 22 13:31 zd/
```

文件类型 + 权限（所有者，所属组，其他人）+ 硬链接数目 + 所属用户 + 所属组 + 修改时间 + 用户名