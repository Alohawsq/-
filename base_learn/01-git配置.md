## git配置
### 1.安装git
下载git安装包，进行安装

### 2.配置公钥
运行命令，按回车输入yes继续按回车
```
ssh-keygen -t rsa -b 4096 -C ssh-keygen -t rsa -b 4096 -C {your_email}
```
生成的公钥在输出中可以看到路径,文件名称为id_rsa.pub,
复制文件内容。

### 3.公钥配置到github
点击头像-->settings-->SSH and GPG keys--> New ssh key-->粘贴复制的公钥文件内容

### 4.本地git配置
```
 git config --global user.email {your_email}
 git config --global user.name {your_name}
```
your_email、your_name为github上你的信息

### 5.拉取仓库
```
 git clone git@github.com:Alohawsq/program-learning.git
```
