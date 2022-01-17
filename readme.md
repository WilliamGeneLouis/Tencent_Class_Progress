<!--
 * @Author: William
 * @Date: 2022-01-15 19:07:50
 * @LastEditTime: 2022-01-17 21:49:22
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /课程学习进度/readme.md
-->

# 课程进度情况

## Git初学

版本控制系统（Version Control System, VCS）: 记录和跟踪项目中各个文件的内容变化。
版本控制工具：自动备份以及跟踪项目所有代码的修改。

### 版本库（Repository）

    版本库是版本控制系统用来存储历史数据的地方 ： commit reason / current time / user / 
    commit : 类似一个对账单，每一次 commit 相当于在本地添加一次修改记录并且保存在版本库中。
    push: 将当地的提交记录上传到项目主版本库。

### 工作目录树（Working Trees）

    工作目录树包括了开发项目所需要的全部文件。
    在 Git 中，版本不在服务器上，而是存储在本地的 “.git” 目录里面。
    工作目录树的创建：
     1. 使用Git初始化版本库。
     2. 克隆一个已经存在的版本库。

### 代码修改与文件同步（Manipulating Files And Staying Sync）

    每次进行提交（commit）操作时，都会使得版本库中添加一个新的版本，包括了改动的日志信息
    以及提交留言（commit messsage）方便进行查找为什么进行这个改动。
    
    Push可以当作是把数据进行共享推入到上游版本库（upstream repository）。
    
### 分支（Branch）

    首先，在版本库中创建分支的起点。自此，两路发展平行并进。每条分支记录这条分支上发生的变化，
    与Master隔离。

    可以进行数据的记录分支不进行合并，可以在进行完实验后直接删除。

### 合并（Merge）

    合并就是把两条以上的分支合并到一起，Git 会比较各个分支上的变化，确定变化发生的位置———
    ——那个文件的那个位置

## Git设置

    command ： git config
    git config --global uesr.name "William"
    git config --global uesr.email "zhijiema6@gmail.com"
    check : git config --global --list
    
    Use different colour to show codes : git config --global colour.iu "auto" / "false"


### 创建版本库（Creating a Repository）

    以HTML为例子：
        mkdir mysite  //创建文件
        cd mysite     //进入到mysite 文件夹
        git init        // 创建本地git

### 代码修改（Marking Changes）

    git add index.html //向本地git添加一个HTML文件
    git commit -m "add in hello world HTML" //设置一个提交记录
    git log // 查看提交的相关信息

###  理解并且使用分支（Understand and use the branch）

    用来支持一个特定功能的开发的分支（Topic Branch）
    git checkout branch/name   //可以切换分支
    git branch x master   //从master上创建一个叫x分支
    
### 克隆版本库（Clone）

    git clone git://github.com/tswicegood/mysite.git

##  添加文件到暂存区（Add file）

    暂存到变更(stage change) 暂存区（Stage area）:
        意味着目录树中你打算提交到版本库的变化。
    
    git add -i //启动交互命令提示符 可以暂存对已有文件的修改
   
### git add -i 

     guister.iu@William  ~  cd mysite                        ✔  549  22:28:21
     guister.iu@William  ~/mysite   master ●  git add -i   ✔  550  22:28:30

                    staged     unstaged path
        1:    unchanged        +1/-1 index.html

        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now> 2                          // 此时输入2，意味着将文件加入到暂存区
                        staged     unstaged path
        1:    unchanged        +1/-1 index.html
        Update>> 1              //此时输入1，出现*，表示该文件已经暂存
                staged     unstaged path
        * 1:    unchanged        +1/-1 index.html
        Update>>                //此时输入回车，退回交互方式的主菜单
        updated 1 path

        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now> 1             //此时输入1，查看工作目录树的情况
                staged     unstaged path
        1:        +1/-1      nothing index.html  //此时没有*，代表该文件已经暂存，没有未暂存的修改

        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now> 3       //revert 可以撤销已暂存的修改 用法与update 类似
                staged     unstaged path
        1:        +1/-1      nothing index.html
        Revert>> 1          // 调出已暂存的文件 并且撤销暂存
                staged     unstaged path
        * 1:        +1/-1      nothing index.html 
        Revert>>
        reverted 1 path

        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now> 1         //此时可以看到之前的修改已经变成了未暂存的状态
                staged     unstaged path
        1:    unchanged        +1/-1 index.html

        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now>5                       /* 此时输入4，意味着暂存还没有被git跟踪的文件。 */
                        staged     unstaged path
        1:    unchanged        +1/-1 index.html
        Patch update>> 1
                staged     unstaged path
        * 1:    unchanged        +1/-1 index.html
        Patch update>>   //此处输入了enter键
        diff --git a/index.html b/index.html
        index e812d0a..ca86894 100644
        --- a/index.html
        +++ b/index.html
        @@ -6,7 +6,7 @@
        <body>
            <h1>Hello World!</h1>
            <ul>
        -        <li><a href="bio.html">Biography</a></li>
        +        <li><a href="about.html">About</a></li>
            </ul>
        </body>
        </html>
        (1/1) Stage this hunk [y,n,q,a,d,e,?]?         //根据需求决定是否添加文本块
                                            // y代表接受修改，n代表忽略修改，a代表添加剩余修改，d代表删除剩余的修改，？会显示所有的信息。
        
        *** Commands ***
        1: status	  2: update	  3: revert	  4: add untracked
        5: patch	  6: diff	  7: quit	  8: help
        What now> 7
        Bye.
    
    输入 git add -p 可以直接进入补丁模式：
        guister.iu@William  ~/mysite   master ●  git add -p   ✔  553  18:04:46  //为乱码，不支持该字符显示
        diff --git a/index.html b/index.html
        index e812d0a..ca86894 100644
        --- a/index.html
        +++ b/index.html
        @@ -6,7 +6,7 @@
        <body>
            <h1>Hello World!</h1>
            <ul>
        -        <li><a href="bio.html">Biography</a></li>
        +        <li><a href="about.html">About</a></li>
            </ul>
        </body>
        </html>
        (1/1) Stage this hunk [y,n,q,a,d,e,?]? y        //输入y表示暂存状态

### 提交修改（Commit Changes）

    Commit意味着把修改上传到本地版本库。   // Git不支持自动更新版本库。
    可以把暂存区当作是一个缓冲区，用命令git add 向缓冲区中添加修改，知道执行git commit 提交缓冲区中的修改。
    
#### 提交方法一

    (先暂存在提交 // 提交暂存后的修改)
    首先对要提交的文件或者是修改调用命令 git add 来添加到暂存区 例如： git add -p
    git add some-file
    git commit -m "changes to some-file"

#### 提交方法二

    （直接提交 // 提交工作目录树中的所有修改）
    给命令git commit 传递 -a 参数， Git 会把工作目录树中当前的所有修改提交到版本库中 //书中未标注本地版本库还是其他版本库
    例如：
    git commit -m "changes to some-file" -a

#### 提交方法三

    （直接提交 // 提交工作目录树中指定的修改）
    指定要提交的文件或者是文件列表，把要提交的文件列在其他参数后面。
    它将提取工作目录树中最新的版本，例如：
    git commit -m "changes to some-file" some-file

### 查看修改内容

    command line:
        git status
        git diff

#### 查看当前状态

    使用git status 可以查看工作目录树中所有的变动，该命令的输出结果是暂存区内要提交的内容，
    工作目录树中未纳入暂缓区的改动，以及未纳入Git版本控制的新文件

#### 查看文件改动

    使用命令git diff, Git可以显示出工作目录树、暂存区以及版本之间的差异
    直接调用不带参数的git diff，将显示工作目录树中未被暂存的改动（也未提交）
    
    git diff --cached 可以比较暂存区和版本库中的区别
    git diff HEAD 可以比较工作目录树（包括暂存和为暂存的修改）与版本库中的差别
    HEAD 指的是当前所在分支末梢的最新提交。

###  文件重命名与移动

git mv <源文件名字> <新文件名字>
该命令告诉git使用源文件的内容创建新文件，新文件保留源文件的历史修改记录，并且删除旧文件。


## 理解和使用分支

### 什么是分支

    git branch -m master mymaster  // change master branch name to mymaster 
    git branch // show us branch name

    -m 参数告诉Git要执行分支移动命令操作。
    git branch 没有参数，由于当前只有master这一条分支，所以只显示这一条分支


#### 以下情况可以创建分支

1. 试验性更改：
比如想测试新算法，看看是否会更快；或者为某个特别的模式重构部分代码。这时就可以创建新分支来发展工作，与那些
需要立即提交和上传的变更区分看。

2. 增加新功能