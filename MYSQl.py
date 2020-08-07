import   mysql.connector
def insert(ip,timee,argg,brr):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  try:
    argg=argg.replace('"','\\"')
    argg=argg.replace("'","\\'")
    a.execute('insert into {}(ip,time,message) values("{}","{}","{}");'.format(brr,ip,timee,argg))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def select(brr):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  a.execute('select *  from {};'.format(brr))
  b=a.fetchall()
  return b
def delete(brr):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  try:
    a.execute('delete from {}'.format(brr))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def D_already(abrr):
    mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
    a = mydb.cursor()
    try:
      a.execute('delete from {};'.format(abrr))
      mydb.commit()
      return "ok"
    except Exception as f:
      return f
def I_already(ip,timee,abrr):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  try:
    a.execute('insert into {}(ip,time) values("{}","{}");'.format(abrr,ip,timee))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def S_already(who,abrr):
  mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
  a = mydb.cursor()
  a.execute('select time  from {} where ip="{}";'.format(abrr,who))
  aa=a.fetchall()
  r=[]
  for i in range(len(aa)):
    r.append(aa[i][0])
  return r  #返回保存的聊天时间
def active(br):
  try:
      mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
      a = mydb.cursor()
      a.execute('select ip  from {};'.format(br))
      return "ok"
  except Exception as f:
      return "error"
def aactive(abrr):
  try:
      mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
      a = mydb.cursor()
      a.execute('select ip  from {};'.format(abrr))
      return "ok"
  except Exception as f:
      return "error"
def retu(who,brr):
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  a.execute('select *  from {} where ip="{}";'.format(brr,str(who)))
  b = a.fetchall()
  return b
def user():
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  a.execute("select name,password  from user ;")
  aa = a.fetchall()
  return aa
def creuser(name,password):
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  try:
    a.execute('insert into user(name,password) values("{}","{}");'.format(name,password))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def crebr(brr):
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  try:
    a.execute('create table {}(ip varchar(200),time varchar(200) ,message varchar(200)) DEFAULT CHARSET=utf8;'.format(brr))
    mydb.commit()
    print("Ok")
    return "ok"
  except Exception as f:
    print(f)
    return f
def  crear(abrr):
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  try:
    a.execute('create table {}(ip varchar(200) ,time varchar(200)) DEFAULT CHARSET=utf8;'.format(abrr))
    mydb.commit()
    print("crear"+abrr)
    return "ok"
  except Exception as f:
    return f
def activebr(br):
  try:
      mydb = mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
      a = mydb.cursor()
      a.execute('select *  from {};'.format(br))
      return "ok"
  except Exception as f:
      return "error"
def creut(user):
  mydb = mysql.connector.connect(host="192.168.116.200", user="root", passwd="Pwd@123456", database="python")
  a = mydb.cursor()
  try:
    a.execute('create table {}(user varchar(200) ,password varchar(200)) DEFAULT CHARSET=utf8;'.format(user))
    mydb.commit()
    return "ok"
  except Exception as f:
    return f
def ACTIVE():
  try:
      mysql.connector.connect(host="192.168.116.200",user="root",passwd="Pwd@123456",database="python")
      return "ok"
  except Exception as f:
      return "error"