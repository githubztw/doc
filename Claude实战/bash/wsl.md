

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

2. `-`：表示上次操作目录地址

   `cd -`上次操作的路径地址

3. `pwd`：当前工作路径

4. `ls [-a]`：当前目录文件列表

   a 表示全部文件，包含隐藏文件，在Linux中以`.`开头的文件视为隐藏文件，不显式展示

5. `touch test.txt` ：在当前目录创建test.txt文件

6. `cat fileName`：读取文件

   cat file1 file2 > fileAll   合并file1 file2 两个文件覆盖fileAll   

7. `grep 关键字 文件名`：检索根据关键字检索文件

   关键字支持正则表达式，如：^de、de$

8. `rm test.txt`： 删除文件test.txt

9. `mv test.txt text1.txt` ：移动文件
   + 当text1.txt文件不存在的时候，重命名test.txt
   + 当text1.txt文件存在的时候，覆盖text1.txt

10. `rm [-i] *.txt` :删除文件，支持正则表达式（删除当前目录中所有以.txt结尾的文件）

   i 表示针对每一个要被删除的文件都提醒用户是否删除

11. `clear`：清理信息





## 特色命令

`alias rm='rm -i'`：重新定义一个命令

`history`：所有执行过的历史命令

单引号：`''` 表示原样输出

双引号：`""`表示会根据内容直接解析命令

无引号：正常展示，但是遇见歧义信息容易出现异常

```bash
# 单引号，原样输出 the (kernel) is $(uname -r)
echo 'the (kernel) is $(uname -r)'

echo "the (kernel) is $(uname -r)" # 正常输出 the (kernel) is 6.6.114.1-microsoft-standard-WSL2

# 无引号，无歧义字符，正常输出 the kernel is 6.6.114.1-microsoft-standard-WSL2
echo the kernel is $(uname -r)

# 无引号，有歧义字符(),出现异常，-bash: syntax error near unexpected token `('
echo the (kernel） is $(uname -r)
```



`echo` : 默认会在结尾添加一个换行符号。`echo -n` 关闭换行

```bash
# 输出：Part of a statement
# 注意：中间必须用分号 ; 分割
echo -n "Part of" ; echo "a statement"

# 输出：Part of  echo a statement
# 没有分号;,不会换行
echo -n "Part of " echo "a statement"

```



# 2. bash 编程



**管道于重定向**

+ 管道：

  通过`|`实现数据管道（链式）传递

+ 重定向：

  通过`>`、`>>`重定向写入数据。

  通过`<`实现输出

  `<<` 实现段落输出

**展开于替换**

`~`：home环境变量值（用户目录路径）， `whoami`：当前用户名称



## 2.1 展开

### 2.1.1  {..}

常常用于数据替换。可以用于笛卡尔数据生成

`{star..end..[间隔n]}` ：从 star开始，间隔n个数据，读取到end

`{star..end..[间隔n]}` _`{star..end..[间隔n]}`：可以实现笛卡尔积式内容生成

```bash
touch file_{01..05}{a..d}  #创建笛卡尔积文件夹目录，5*4=20个目录

echo {01..10..2}  #  01，03，05，07，09
echo {a,b,c} # 简单枚举
# 一次性读取 dir1、dir2、dir3 三个文件夹里的 lorem.txt 文件，分别打印每个文件开头的第一行(head -n1)内容。
echo head -n1 {dir1,dir2,dir3}/lorem.txt
```

### 2.1.2 `${}`：参数扩展

```bash
# 定义变量。注意，= 两边不可以有空格
greeting="hello there!"

# 使用变量的时候，必须通过 $ 符号 

echo $greeting  #hello there!

# 参数截取
echo ${greeting:6} #  there!
echo ${greeting:6:3} # the 

#替换参数
echo ${greeting/e/_} # h_llo there! 将第一个e替换成_
echo ${greeting//e/_} # h_llo th_r_! 将所有的e替换成_

# 注意当对字符串操作的时候，必须使用 ${},否则bash不能识别
echo $greeting:4:3 #hello there!:4:3
```


### 2.1.3 $(...) 命令替换

```bash
# 将命令嵌入到字符串中，运行的时候，可以直接将结果做位置替换。它可以式一个简单命令，也可以式一个复杂处理命令，如管道、重定向语句等
echo "the files $(ls)"
```



### 2.1.4 $(()) 算数扩展

```bash
echo $((2+2)) # 4
echo $((5*4)) # 20
```



## 2.2 变量

`declare -[rlu] variable="Test"`

+ -r 只读变量
+ -l 全部转换成小写变量 `test`
+ -u 全部转换成大写变量 `TEST`

> **注意：**declare 定义的变量，其标记会永远作用到变量中，直到资源释放

`declare -p`：显示当前会话中设置的所有变量

```bash
myvar="Hello!" # 常规定义变量
echo "The value of the myvar variable is: $myvar"

myvar="Bonjour!" # 变量重新赋值
echo "The value of the myvar variable is: $myvar"

declare -r myname="Scott" # 定义只读变量
echo "The value of the myname variable is: $myname"

myname="Michael" # 会出现异常，但不影响后续运行
echo "The value of the myname variable is: $myname"

declare -l lowerstring="This is some TEXT!" # 将文本转换成小写
echo "The value of the lowerstring variable is: $lowerstring"
lowerstring="Let's CHANGE the VALUE!"
echo "The value of the lowerstring variable is: $lowerstring"  # 结果依旧全是小写

declare -u upperstring="This is some TEXT!"
echo "The value of the upperstring variable is: $upperstring"  # 将文本转换成大写
upperstring="Let's CHANGE the VALUE!"
echo "The value of the upperstring variable is: $upperstring"  # 结果依旧全是大写
```

