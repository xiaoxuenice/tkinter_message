# -*- mode=python ending:utf-8 -*-
# pack：按添加顺序排列组件 bao
# grid：按行列形式排列组件 wangge          ,
#           row=0,column=0 行，列      rowspan占几行，columnspan占几列
#           sticky='w'   w左，e右
#           width=20 宽      height=2 高
# place：允许程序员指定组件的大小和位置 difang
from tkinter import *
import easygui, time, threading, MYSQl,test3,sys


class MY_GUI(threading.Thread):

    def __init__(self, xiaoxue,):
        self.xiaoxue = xiaoxue
    def XIAOXUE(self, IP,lt,brr,abrr):
        self.brr=brr
        self.abrr=abrr
        self.IP = IP
        self.lt = lt
        self.xiaoxue.title("welcome to use!!     {}    you now chat and   {}".format(self.IP.upper(),self.lt.upper()))
        screenWidth = self.xiaoxue.winfo_screenwidth()  # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()  # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("700x500+{}+{}".format(x, y))  # 宽高居中
        # self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg'] = '#ADD8E6'  # bg背景颜色 fg字体颜色
        self.xiaoxue.iconbitmap("a.ico")  # 图标
        self.xiaoxue.attributes("-alpha", 0.95)  # 虚化
        self.xiaoxue.bind("<Control-Key-d>", self.BTN3)

        self.entry33 = Entry(self.xiaoxue, width=63, )
        self.entry33.grid(row=2, column=0, columnspan=5, )
        self.entry33.bind("<Return>",self.SHELL)
        self.button1 = Button(self.xiaoxue, bg="pink", text="Start", activebackground='lime', command=lambda: self.thread_it(self.read),
                              width=10)  # activebackground按下去颜色
        self.button1.grid(row=0, column=0, sticky='w')  # 调度EXIT函数
        self.button2 = Button(self.xiaoxue, bg="pink", text="EXIT", activebackground='lime', command=self.TISHI,
                              width=10)
        self.button2.grid(row=1, column=0, sticky='w')  # 调度TISHI函数
        self.button3 = Button(self.xiaoxue, bg="pink", text="Status", activebackground='lime', command=self.BIND,
                              width=10)  # activebackground按下去颜色
        self.button3.grid(row=0, column=1, sticky='w')  # 调度BTN3函数
        self.button4 = Button(self.xiaoxue, bg="pink", text="History", activebackground='lime', command=self.BTN4,
                              width=10)
        self.button4.grid(row=1, column=1, sticky='w')  # 调度BTN4函数
        self.button7 = Button(self.xiaoxue, bg="pink", text="CLEAR", activebackground='lime', command=self.CLEAR,
                              width=10)
        self.button7.grid(row=2, column=0, sticky='w')  # 调度BTN6函数

        # 文本框
        self.scroll2 = Scrollbar()  # 滚动条
        self.text1 = Text(self.xiaoxue, width=97, height=17)
        ######################################################################
        # self.text1.tag_add("tag","1.0")
        self.text1.tag_config("tag", background='yellow', foreground='red')
        self.scroll2.config(command=self.text1.yview)
        self.text1.config(yscrollcommand=self.scroll2.set)
        self.text1.grid(row=3, column=0, columnspan=5)
        self.scroll2.grid(row=3, column=6, columnspan=1, sticky='nsw')
        self.text1.see(END)
        self.text1.update()
        # 输出框
        self.scroll1 = Scrollbar()  # 滚动条
        self.listbox = Listbox(self.xiaoxue, width=97, selectmode="extended")
        self.scroll1.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll1.set)
        self.listbox.grid(row=4, column=0, columnspan=5)  # nswe 上下左右
        self.scroll1.grid(row=4, column=6, columnspan=1, sticky="nsw")

# BTN2
    def TISHI(self):
        easygui.msgbox("走咯。。lalala~", '提示')
        sys.exit(0)

    # BTN3
    def BIND(self):
        easygui.msgbox(MYSQl.active(self.brr), "服务器连接状态")  # 看ssh连接是否正常

    # BTN4
    def BTN4(self):
        if MYSQl.active(self.brr) == "ok":
            self.listbox.delete(0, END)  # 从数据库输出到listbox历史执行命令
            for i in MYSQl.select(self.brr)[-1::-1]:
                xx = "{}  {}  {} ".format(i[0], self.TIME(i[1]), i[2])
                self.listbox.insert(END, xx)
        else:
            self.listbox.delete(0, END)
            self.listbox.insert("数据连接失败！")

    # >>>>>>>>>>>>>>>>>读取消息
    # >>>>>>>>>>>>>>>>>读取消息#>>>>>>>>>>>>>>>>>读取消息
    def read(self):
     while True:
        yjbcdtime = MYSQl.S_already(self.lt,self.abrr)
        print("   循环 中。。。。。。")
        ltjl = MYSQl.retu(self.lt,self.brr)
        for i in ltjl:
            if i[1] not in yjbcdtime:
                ddxx = "\n{} {}    \n{}\n".format(i[0], self.TIME(i[1]), i[2])
                self.text1.insert(END, ddxx, "tag")
                self.text1.see(END)
                MYSQl.I_already(i[0], i[1],self.abrr)
        time.sleep(1)
#开启线程操作
    @staticmethod
    def thread_it(func):
        t = threading.Thread(target=func)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()
    def SHELL(self,event):
        t = time.time()
        b = self.entry33.get()
        self.entry33.delete(0, END)
        bb = "\n{} {}      \n{}\n".format(self.IP, self.TIME(t), b)
        self.text1.insert(END, bb)
        self.text1.see(END)
        MYSQl.insert(self.IP, t, b,self.brr)  # 保存在数据库
    def  CLEAR(self):
        self.text1.delete(1.0, END)
        self.listbox.delete(0, END)
# 事件
    def BTN3(self, event):  # 事件触发删除历史命令
        if easygui.ccbox("你确定要删除本地和数据库的历史记录吗?"):
            print('hehe')
        else:
            cccccccc
        self.text1.delete(1.0,END)
        self.listbox.delete(0,END)
        MYSQl.delete(self.brr)
        MYSQl.D_already(self.abrr)

    # TIME
    def TIME(self, bbb):
        return (time.strftime("%m-%d %H:%M:%S", time.localtime(float(bbb))))

    ############################################################3
    def PLAY(self):
        self.xiaoxue = self.xiaoxue
        self.xiaoxue.title("登陆认证")
        screenWidth = self.xiaoxue.winfo_screenwidth()  # 宽
        screenHeight = self.xiaoxue.winfo_screenheight()  # 高
        x = int((screenWidth - 700) / 2)
        y = int((screenHeight - 500) / 2)
        self.xiaoxue.geometry("300x200+{}+{}".format(x, y))  # 宽高居中
        # self.xiaoxue.geometry("700x500+10+10")
        self.xiaoxue['bg'] = '#ADD8E6'  # bg背景颜色 fg字体颜色
        self.xiaoxue.iconbitmap("a.ico")  # 图标
        self.xiaoxue.attributes("-alpha", 0.95)
        self.label1 = Label(self.xiaoxue, text="", bg="lightblue", height=1)
        self.label1.grid(row=1, column=0, sticky=W)  #
        self.label1 = Label(self.xiaoxue, text="", bg="lightblue", height=1)
        self.label1.grid(row=5, column=0, sticky=W)
        self.label1 = Label(self.xiaoxue, text="", bg="lightblue", height=1)
        self.label1.grid(row=2, column=0, sticky=W)
        self.label1 = Label(self.xiaoxue, text="用户名:", bg="lightblue", height=1)
        self.label1.grid(row=3, column=0, sticky=W)  # 行 列 左粘
        self.label2 = Label(self.xiaoxue, text="密码 :", bg="lightblue", height=1)
        self.label2.grid(row=4, column=0, sticky=W)
        self.label11 = Label(self.xiaoxue, text="聊天人:", bg="lightblue", height=1)
        self.label11.grid(row=6, column=0, sticky=W)
        self.button1 = Button(self.xiaoxue, bg="pink", text="Login", activebackground='lime', command=self.zhangsan,
                              width=10)  # activebackground按下去颜色
        self.button1.grid(row=7, rowspan=1, column=1, )
        self.button1 = Label(self.xiaoxue, text="", bg="lightblue", width=10)  # activebackground按下去颜色
        self.button1.grid(row=7, column=0, )
        self.entry1 = Entry(self.xiaoxue, width=20)
        self.entry1.grid(row=3, column=1, sticky='w')
        self.entry2 = Entry(self.xiaoxue, width=20,show="~")  # 密码隐藏
        self.entry2.grid(row=4, column=1, sticky='w')
        self.entry8 = Entry(self.xiaoxue, width=20, )  # show="~")  # 密码隐藏
        self.entry8.grid(row=6, column=1, sticky='w')

    def zhangsan(self):
        b = self.entry1.get()
        b=b.lower().strip()
        c = self.entry2.get()
        c=c.lower().strip()
        e = self.entry8.get()
        e=e.lower().strip()
        if MYSQl.ACTIVE() == "ok":
            print("网络OK")
        else:
            easygui.msgbox("\n\n你连不到数据库哦~~~~     请排查网络。。。","网络提示！")
            sys.exit(0)
        if MYSQl.activebr("user") == "ok":
            d = MYSQl.user()
            yh=[]
            for i in d:
                yh.append(i[0])
            if b in yh:
             for i in d:
                if i[0] == b:
                    if  test3.pd(c,i[1]) == "ok":
                        br=[b,e]
                        brr=''.join(sorted(br))
                        abrr="a"+brr
                        if MYSQl.active(brr) == "ok" and MYSQl.aactive(brr) == "ok":
                            self.xiaoxue.destroy()
                            Start = Tk()
                            MY_GUI(Start).XIAOXUE(b,e,brr,abrr)
                            Start.mainloop()
                        else:
                            MYSQl.crebr(brr)
                            MYSQl.crear(abrr)
                            self.xiaoxue.destroy()
                            Start = Tk()
                            MY_GUI(Start).XIAOXUE(b, e, brr, abrr)
                            Start.mainloop()
            else:
                pd=test3.sc(c)
                MYSQl.creuser(b,pd)
        else:
            MYSQl.creut("user")
if __name__ == "__main__":
    Start = Tk()
    MY_GUI(Start).PLAY()
    Start.mainloop()
