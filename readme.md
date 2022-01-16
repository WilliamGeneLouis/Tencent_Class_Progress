<!--
 * @Author: William
 * @Date: 2022-01-15 19:07:50
 * @LastEditTime: 2022-01-16 22:29:06
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /课程学习进度/readme.md
-->

# 课程进度情况

## 1.16 (Part one)
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
    
### 克隆版本库
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
        What now>
   