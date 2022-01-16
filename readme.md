<!--
 * @Author: William
 * @Date: 2022-01-15 19:07:50
 * @LastEditTime: 2022-01-16 13:04:02
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
    每次进行提交（commit）操作时，都会使得版本库中添加一个新的版本，包括了改动的日志信息以及提交留言（commit messsage）方便进行查找为什么进行这个改动。
    Push可以当作是把数据进行共享推入到上游版本库（upstream repository）。
    
