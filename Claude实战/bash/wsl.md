

# wsl 安装

[scottsimpson/learning-bash-scripting: The repository for the course Learning Bash Scripting](https://github.com/scottsimpson/learning-bash-scripting)

安装WSL:`wsl --install`

安装 `ubuntu

> 1. wsl --install -d ubuntu-24.04  #  **注意**：最新版本是Ubuntu-26.04 
> 2. 注册账户：输入用户名，密码

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

4. `mkdir test`：创建目录

5. `ls [-a]`：当前目录文件列表

   a 表示全部文件，包含隐藏文件，在Linux中以`.`开头的文件视为隐藏文件，不显式展示

6. `touch test.txt` ：在当前目录创建test.txt文件

7. `cat fileName`：读取文件

   cat file1 file2 > fileAll   合并file1 file2 两个文件覆盖fileAll   

8. `grep 关键字 文件名`：检索根据关键字检索文件

   关键字支持正则表达式，如：^de、de$

9. `rm test.txt`： 删除文件test.txt

10. `mv test.txt text1.txt` ：移动文件
   + 当text1.txt文件不存在的时候，重命名test.txt
   + 当text1.txt文件存在的时候，覆盖text1.txt

11. `rm [-i] *.txt` :删除文件，支持正则表达式（删除当前目录中所有以.txt结尾的文件）

   i 表示针对每一个要被删除的文件都提醒用户是否删除

11. `clear`：清理信息
11. `ls -a`:读取全部文件信息，-a表示读取全部文件





## 特色命令

`alias rm='rm -i'`：重新定义一个命令

`less`: 分页展示数据

> help test | less   # 表示将test相关文档，通过管道传递给less，分页展示数据
>
> 通过q键退出文件读取

`history`：所有执行过的历史命令

`$RANDOM`：表示随机数内置变量，注意，必须大写

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



### 2.1.4 $(()) 算数求值

> 注意：一般情况下bash只可以做整数运算
>
> 可以通过算数求值的方式给变量重新赋值  ，如 :$((a=10))

```bash
echo $((2+2)) # 4
echo $((5*4)) # 20

# 也可以用来做复杂运算
echo $(((3+6)-5*(5-2)))

# 可以使用变量进行算数扩展。
a=3
# 注意：此处变量a在使用的时候，无需：$a
echo $((a=10)) # 输出10
echo $a # 输出10

a=$a+2 # 注意这种写法是不规范的，没有用$(())进行修饰
echo $a  #输出10+2

declare -i b=10
b=b+4
echo $b # 输出14，因为定义了整数型类型变量b
```



## 2.2 变量

`declare -[rluiaA] variable="Test"`

+ -r 只读变量
+ -l 全部转换成小写变量 `test`
+ -u 全部转换成大写变量 `TEST`
+ -i 表示整数类型数据
+ -a 表示普通一维数组
+ -A 表示字典数组

> **注意：**declare 定义的变量，其标记会**永远作用到变量中**，直到资源释放

`declare -p`：显示当前会话中设置的所有变量信息

`$RANDOM`：表示随机数内置变量，注意，必须大写

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



## 2.3 比较数值`[]`

**注意：**所有运算符前后必须加空格

+ -a  表示and
+ -o  表示or
+ 

```bash		
str=cat
[ $str = "cat" ]; echo $?  # 输出0，表示true
[ $str = "dog" ]; echo $? # 输出1 ，表示false
[ 4 -lt 5 ]; echo $?  # 输出0，表示true
[ 4 -gt 5 ]; echo $?   # 输出0，表示true
[ 4 -eq 4 ]; echo $?   # 输出0，表示true
[ 4 -ne 4 ]; echo $?   # 输出1，表示false


# 取反
[ ! 4 -gt 3 ]; echo $? # 输出1，表示false
```

| 运算符 | 全称          | 作用       |
| ------ | ------------- | ---------- |
| `-eq`  | equal         | 等于       |
| `-ne`  | not equal     | **不等于** |
| `-gt`  | greater than  | 大于       |
| `-ge`  | greater equal | 大于等于   |
| `-lt`  | less than     | 小于       |
| `-le`  | less equal    | 小于等于   |

### [[]]比较

+ `[ ]` 只能用外部 `&&` `||`；`[[ ]]` 支持内部 `&&` `||`
+ `[[ ]]` 支持字符串正则匹配、通配符匹配
  +  =~ 表示正则匹配运算符



**注意：**面对复杂的正则表达式，最好不要使用bash

```bash
# 使用正则表达式
str="abc123"
[[ $str =~ [0-9]+ ]]  # 支持正则，[] 完全做不到

# 使用通配符
[[ "test.txt" == test* ]]
```



## 2.4 格式化与美化文本输出

`echo -e`：开启**反斜杠转义解析**，识别 `\n`、 `\t`、 `\r`、 `\\` 等类特殊符号

```bash
echo -e "Name\t\tNumber"  
# 显示效果：Name            Number
echo -e "Name\nNumber" 
# 显示效果
# Name
# Number
```

### 占位符`printf`

会直接识别 `\n`、 `\t`、 `\r`、 `\\` 等类特殊符号

`%d`：表示数值

`%s`：表示字符串



`%10s`：字符串总宽度固定 10 字符，**右对齐**，左边补空格

`%05d`：数字总宽度固定 5 字符，**右对齐**，左边空位用0填充，（默认是空格填充）

`%-10s`：字符串总宽度固定 10 字符，**左对齐**，右边补空格



```bash
printf "the result is: %d and %s\n" $((2+2)) "test" # 输出：the result is: 4 and test

printf "%10s: %5d\n" "A Label" 123 "B Label" 456 "C" 
 A Label:   123
 B Label:   456
       C:     0 # 默认补0
       

```



## 32.5 数组：

一维数组

```bash
# 注意，元素之间用空格隔开，而不是逗号
snacks=("apple" "banana" "orange")
# 或显式声明数组
declare -a snacks=("apple" "banana" "orange")

# 添加数据
snacks[3]="egg" # 等效 snacks+=("egg")

echo ${snacks[3]} # 输出：egg
```

键值对数组

```bash
declare -A office
office[city]="San Francisco"
office["building name"]="HQ West"
echo ${office["building name"]} is in ${office[city]}


declare -A arr3=([Honda]=Civic [BMW]=7Series [Mercedes]=CClass)
echo ${arr3["Honda"]} # 等价 ${arr3[Honda]}
```

