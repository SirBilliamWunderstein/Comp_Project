import mysql.connector as DCP
import pickle as dex
import random as rd
import specSQLpac.constance as const

con = const.Constance()

class PypedPyper():
    global portbay
    global ship
    global infodat # = [username str,lak str,pas str,restoIK list,eventIK list,anonymousIK list]
    global lak

    def __init__(self,use,pas,lak):
        try:
            self.portbay = DCP.connect(user = use,host = "localhost",password = pas,database = con.lak,auth_plugin='mysql_native_password')
        except:
            return con.incorrect_userpass
        if portbay.is_connected():
            print("Eshtablished connection successfully")  #  REPLACE LATER WITH FUNCTIONALITY MAYBE 
        self.ship = portbay.cursor()
        ship.execute("select * from listak where user = '{}'".format(use,))
        Q = self.ship.fetchall()
        if Q == None:
            return con.lakmismatch # cant use return here, find alternatives
        elif Q[0] == use:
            binfil = open("./bindump/LAK.dat","w+b")
            self.ship.execute("select * from {}".format(lak,))
            while True:
                Q = self.ship.fetchone()
                if Q == None:
                    break
                binfil.write(Q[0].to_byte(1,"big"))
            binfil.seek(0,0)
            self.infodat = dex.load(binfil)
            binfil.close()
        self.lak = lak
    
    def IK_Get(self):
        Q = ""
        for i in range(16):
            Q += chr(rd.randint(ord("a"),ord("z")))
        return Q

    def Retrieve_request_s(self):
        Q = self.infodat[2] + self.infodat[3] + self.infodat[4]
        for i in Q:
            pass

    def rem_request(self,IK,user):
        q = IK + user
        self.ship.execute("use {}".format(con.reqb))
        self.ship.execute("drop table {}".format(q,))
        self.ship.execute("delete from MesReq where IK = '{}' and user = '{}'".format(IK,user))
        self.portbay.commit()

    def resto_create(self,Title,menu,loc,opclo,desc): 
        self.ship.execute("use {}".format(con.resto,))
        Q = self.IK_Get()

        self.ship.execute("select ik from rlist")
        S = self.ship.fetchall()
        for i in S:
            if i[0] == Q:
                Q = self.IK_Get()
                break
        self.ship.execute("insert into rlist values('{}','{}','{}','{}','{}')".format(Q,Title,loc.get(),opclo,desc)) 
        self.infodat[3].append(Q)

        self.ship.execute("create table {}(id int,food str,price int,category varchar(1))".format(Q,))
        self.portbay.commit()
        S = list(menu.keys())
        for i in range(len(S)):
            self.ship.execute("insert into {} values({},'{}',{},'{}')".format(Q,i+1,S[i],menu[S[i]][0],menu[S[i]][1]))
            self.portbay.commit()

        binfil = open("../bindump/LAK.dat","wb")
        dex.dump(self.infodat,binfil)
        binfil.close()

        return Q
    
    def Standard_column_updater(self,db,tab,col,iden,ccol,dat):
        self.ship.execute("use {}".format(db))
        try:
            iden += 1
            iden -= 1
        except:
            iden = "'" + iden + "'"
        
        try:
            dat += 1
            dat -= 1
        except:
            dat = "'" + dat + "'"
        
        self.ship.execute("update {} set {} = {} where {} = {}".format(tab,ccol,dat,col,iden))
        self.portbay.commit()

    def bin_file_updater(self,db,IK,filoc):
        self.ship.execute("use {}".format(db,))
        self.ship.execute("delete from {}".format(IK))
        self.portbay.commit()

        binfil = open(filoc,"rb")
        Q = binfil.read()
        for i in Q:
            self.ship.execute("insert into {} values({})".format(IK,i))
            self.portbay.commit()
        binfil.close()

        if db == con.anon:
            ss = rd.randint(-127,128)
            self.ship.execute("update Uplist set RGI = {} where IK = '{}'".format(ss,IK))

    def eve_Create(self,title,loc,picloc,date,desc):
        self.ship.execute("use {}".format(con.eve,))
        Q = self.IK_Get()

        self.ship.execute("select ik from Elist")
        S = self.ship.fetchall()
        for i in S:
            if i[0] == Q:
                Q = self.IK_Get()
                break
        self.ship.execute("insert into elist values('{}','{}','{}',{},'{}')",format(Q,title,loc.get(),date,desc)) # make loc.get
        self.portbay.commit()

        self.ship.execute("create table {}(bina int)".format(Q,))
        self.portbay.commit()
        picfil = open(picloc,"rb")
        Q = picfil.read()
        for i in Q:
            self.ship.execute("insert into {} values({})".format(Q,i))
            self.portbay.commit()

        self.infodat[4].append(Q)
        binfil = open("./bindump/LAK.dat","wb")
        dex.dump(self.infodat,binfil)
        binfil.close()

        return Q
    
    def Anonym_Create(self,Title,iconloc,loc,cont,desc):  # housing,local business,breweries,etc
        self.ship.execute("use {}".format(con.anon,))
        Q = self.IK_Get()

        self.ship.execute("select ik from Anonlist")
        S = self.ship.fetchall()
        for i in S:
            if i[0] == Q:
                Q = self.IK_Get()
                break
        self.ship.execute("insert into Anonlist values('{}','{}',{},'{}')".format(Q,Title,loc,cont,desc))
        self.portbay.commit()
        self.ship.execute("create table {} values(bina int)".format(Q,))
        self.portbay.commit()

        icofil = open(iconloc,"rb")
        S = icofil.read()
        for i in S:
            self.ship.execute("insert into {} values({})".format(Q,i))
            self.portbay.commit()
        icofil.close()
        
        self.infodat[5].append(Q)
        binfil = open("./bindump/LAK.dat","wb")
        dex.dump(self.infodat,binfil)
        binfil.close()
        
        return Q
    
    def shutdown_protocol(self):
        self.portbay.commit()
        binfil = open("../bindump/LAK.dat","rb")
        self.ship.execute("use {}".format(con.lak,))
        self.ship.execute("delete * from {}".format(self.lak,))
        self.portbay.commit()
        Q = binfil.read()
        for i in Q:
            self.ship.execute("insert into {} values({})".format(self.lak,i))
            self.portbay.commit()
        binfil.close()
        # 
        self.portbay.close()
