## This is Readme
用于[问卷调查网站](https://rucsb.au1.qualtrics.com/)
2017-09-19:之前的版本记录过于混乱,就让他们迷失在时间线中吧.
***
* id.js,practice.js,fixed10.js,random6.js均为september文件夹下最新版,所实现的基本功能均包括:1.屏蔽shift+字母产生的大写字母;2.屏蔽ctrl+字母的默认事件,并使ctrl+字母产生大写字母;3.记录上一个操作到ctrl/shift/capslock的时间.文件名称均对应相应block的时间
* 'a'project:id-a.js为id的block,主要检测按完数字到错误字母的时间以及按完数字到字母'a'的时间
* fixed-a.js为fixed的block,用于检测上一个按键到'a'的时间,并记录是首次输入正确还是修改正确