

# wsl 安装

[scottsimpson/learning-bash-scripting: The repository for the course Learning Bash Scripting](https://github.com/scottsimpson/learning-bash-scripting)

安装WSL:`wsl --install`
用户名：wei  密码：Ztw@123456

>wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理。
>
>原因： Windows 代理是 `127.0.0.1:7897`，NAT 模式下 WSL 无法使用 localhost 代理



1. 在用户目录下面创建`wslconfig`文件

   ```
   [wsl2]
   networkingMode=mirrored
   dnsTunneling=true
   firewall=true
   autoProxy=true
   ```

   

2. 关闭wsl ：`wsl --shutdown`

3. 重新运行 `wsl`



# 1. 基本命令



在WSL中，Windows C 盘在 WSL 里统一挂载到 /mnt/c/。

**注意：**路径分割必须使用正斜杠 `/`,在Linux中反斜杠`\`往往表示转义符。

```bash
# 切换目录到c/Users/13125/Desktop/test路径
cd /mnt/c/Users/13125/Desktop/test
```

`bash --version` 查看版本

`echo $SHELL`：查看SHELL

## 文件操作

1. 写文件。当文件不存在的时候就会默认先创建文件：

   + `>`：覆盖

     echo hello > file.txt

     cat file1 file2 > fileAll

   + `>>`：追加到结尾
   
     echo hello > file.txt

2. `pwd`：当前工作路径

3. `ls [-a]`：当前目录文件列表

   a 表示全部文件，包含隐藏文件，在Linux中以`.`开头的文件视为隐藏文件，不显式展示

4. `touch test.txt` ：在当前目录创建test.txt文件

5. `cat fileName`：读取文件

   cat file1 file2 > fileAll   合并file1 file2 两个文件覆盖fileAll   

6. `grep 关键字 文件名`：检索根据关键字检索文件

   关键字支持正则表达式，如：^de、de$

7. `rm test.txt`： 删除文件test.txt
8. `mv test.txt text1.txt` ：移动文件
   + 当text1.txt文件不存在的时候，重命名test.txt
   + 当text1.txt文件存在的时候，覆盖text1.txt

9. `rm [-i] *.txt` :删除文件，支持正则表达式（删除当前目录中所有以.txt结尾的文件）

   i 表示针对每一个要被删除的文件都提醒用户是否删除

10. `clear`：清理信息





## 特色命令

`alias rm='rm -i'`：重新定义一个命令

`history`：所有执行过的历史命令



# 2. bash 编程



**管道于重定向**







