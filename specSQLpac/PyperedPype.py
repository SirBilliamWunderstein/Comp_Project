import mysql.connector as dcp
import pickle as dex
import specSQLpac.constance as Constance
import specTKpac as LPS

con = Constance.Constance()


class PyperedPype():
    global portbay
    global ship
    global infodat
    global restoIK
    global eventIK
    global anonIK

    def __init__(self,Retriever,pas,):
        try:
            self.portbay = dcp.connect(user = Retriever,host = "localhost",password = pas,auth_plugin='mysql_native_password')
        except:
            pass
        
        self.infodat = [Retriever,pas]
        binfil = open("./bindump/ret.dat","wb")
        dex.dump(self.infodat,binfil)
        binfil.close()

        try:
            binfil = open("./Icon/Smakefile.dat","rb")
            self.IconUpdate(binfil)
            binfil.close()
        except:
            self.First_Icon_Run()
        
        try:
            binfil = open("./bindump/mapdat/Smakefile.dat","rb")
            self.MapUpdate(binfil)
            binfil.close()
        except:
            self.First_Map_Run()
        
        self.fetch_IK()

    def fetch_Resto_men(self,IK):
        self.ship.execute("use {}".format(con.resto,))
        self.ship.execute("select * from {}".format(IK,))
        Q = self.ship.fetchall()
        S = []
        for i in Q:
            S.append(list(i))
        
        return S

    def db_Get(self,IK):
        lee = ""
        self.ship.execute("use {}".format(con.anon))
        self.ship.execute("select IK from Anonlist")
        wee = self.ship.fetchall()
        for i in wee:
            if i[0] == IK:
                lee = con.anon
        
        self.ship.execute("use {}".format(con.resto))
        self.ship.execute("select IK from rlist")
        wee = self.ship.fetchall()
        for i in wee:
            if i[0] == IK:
                lee = con.resto
                
        self.ship.execute("use {}".format(con.anon))
        self.ship.execute("select IK from Elist")
        wee = self.ship.fetchall()
        for i in wee:
            if i[0] == IK:
                lee = con.eve
        return lee

    def IK_get(self,name,db):
        self.ship.execute("use {}".format(db,))
        q = ""
        if db == con.resto:
            q = "RList"
        elif db == con.eve:
            q = "EList"
        else:
            q = "AnonList"
        self.ship.execute("select IK from {} where Title = \"{}\"".format(q,name))
        
    def Nam_get(self,IK,db,le = "Title"):
        self.ship.execute("use {}".format(db,))
        q = ""
        if db == con.resto:
            q = "RList"
        elif db == con.eve:
            q = "EList"
        else:
            q = "AnonList"
        self.ship.execute("select {} from {} where IK = \"{}\"".format(le,q,IK))

    def send_Request(self,recev,standardizedmes,address):
        self.ship.execute("use {}".format(con.reqb,))
        nam = recev + ":" + self.infodat[0]
        self.ship.execute("create table {}(desc varchar(250),loc varchar(100))".format(nam,))
        self.portbay.commit()
        self.ship.execute("insert into {} values(\"{}\",\"{}\")".format(nam,standardizedmes,address))
        self.portbay.commit()
        self.ship.execute("insert into MesRel values(\"{}\",\"{}\")".format(recev,self.infodat[0]))
        self.portbay.commit()

        fil = open("./bindump/LOGDATA.txt","a")
        fil.write(recev+":"+standardizedmes + "\n")
        fil.close()

    def Restriever(self,IK):
        self.ship.execute("use {}".format(con.resto,))
        self.ship.execute("select * from {}".format(IK,))
        Q = []
        q = self.ship.fetchall()
        for i in q:
            Q.append(list(i))
        return Q

    def Postriever(self,IK):
        self.ship.execute("use {}".format(con.eve,))
        self.ship.execute("select * from {}".format(IK))
        binfil = open("./Pic/"+IK+".png","wb")
        try:
            while True:
                q = self.ship.fetchone()
                if q == None:
                    break
                else:
                    binfil.write(q[0].to_byte(1,"big"))
            binfil.close()
            return con.success
        except:
            binfil.close()
            return con.failed

    def First_Icon_Run(self):
        self.ship.execute("use {}".format(con.anon))
        self.ship.execute("select IK from Anonlist")

        Q = self.ship.fetchall()
        for i in Q:
            binfil = open("./Icon/"+i[0]+".png","wb") # check for .. or .
            self.ship.execute("select * from {}".format(i[0],))
            while True:
                S = self.ship.fetchone()
                if S == None:
                    break
                binfil.write(S[0].to_byte(1,"big"))
            binfil.close()
        
        binfil = open("./Icon/Smakefile.dat")
        self.ship.execute("select * from Uplist")
        Q = self.ship.fetchall()
        S = {}
        for i in Q:
            S[i[0]] = i[1]
        dex.dump(S,binfil)
        binfil.close()

    def fetch_IK(self):
        Q = []
        self.ship.execute("use {}".format(con.resto,))
        self.ship.execute("select * from Rlist")
        q = self.ship.fetchall()
        for i in q:
            i = list(i)
            q = i[2].split(":")
            i[2] = LPS.location(q[0],q[1],q[2])
            Q.append(i)
        self.restoIK = Q

        Q = []
        self.ship.execute("use {}".format(con.eve,))
        self.ship.execute("select * from Elist")
        q = self.ship.fetchall()
        for i in q:
            i = list(i)
            q = i[2].split(":")
            i[2] = LPS.location(q[0],q[1],q[2])
            Q.append(i)
        self.eventIK = Q

        Q = []
        self.ship.execute("use {}".format(con.anon,))
        self.ship.execute("select * from Anonlist")
        q = self.ship.fetchall()
        for i in q:
            i = list(i)
            q = i[2].split(":")
            i[2] = LPS.location(q[0],q[1],q[2])
            Q.append(i)
        self.anonIK = Q
    
    def Rest_IK_get(self,name):
        self.ship.execute("use {}".format(con.resto,))
        self.ship.execute("select IK from RList where Title = {}".format(name,))
        q = self.ship.fetchone()
        return q[0]
    
    def IconUpdate(self,bin):
        self.ship.execute("use {}".format(con.anon,))
        self.ship.execute("select * from Uplist")
        Q = self.ship.fetchall()
        q = dex.load(bin)
        for i in Q:
            if i[1] != q[i[0]]:
                binfil = open("./Icon/"+i[0]+".png","wb")
                self.ship.execute("select * from {}".format(i[0],))
                while True:
                    S = self.ship.fetchone()
                    if S == None:
                        break
                    binfil.write(S[0].to_byte(1,"big"))
                binfil.close()
                print("Icon Updated")
            elif i[1] not in q.keys():
                binfil = open("./Icon/"+i[0]+".png","wb")
                self.ship.execute("select * from {}".format(i[0],))
                while True:
                    S = self.ship.fetchone()
                    if S == None:
                        break
                    binfil.write(S[0].to_byte(1,"big"))
                binfil.close()
                print("Icon Updated")
            else:
                print("Icon To Date")
        S = {}
        for i in Q:
            S[i[0]] = i[1]
        dex.dump(S,binfil)
        binfil.close()
    
    def First_Map_Run(self):
        self.ship.execute("use {}".format(con.mapdat))
        self.ship.execute("select IK from MapList")

        Q = self.ship.fetchall()
        for i in Q:
            binfil = open("./bindump/mapdat/"+i[0]+".png","wb") # check for .. or .
            self.ship.execute("select * from {}".format(i[0],))
            while True:
                S = self.ship.fetchone()
                if S == None:
                    break
                binfil.write(S[0].to_byte(1,"big"))
            binfil.close()
        
        binfil = open("./bindump/mapdat/Smakefile.dat")
        self.ship.execute("select * from Maplist")
        Q = self.ship.fetchall()
        S = {}
        for i in Q:
            S[i[0]] = i[1]
        dex.dump(S,binfil)
        binfil.close()
    
    def MapUpdate(self,bin):
        self.ship.execute("use {}".format(con.mapdat,))
        self.ship.execute("select * from MapList")
        Q = self.ship.fetchall()
        q = dex.load(bin)
        for i in Q:
            if i[1] != q[i[0]]:
                binfil = open("./bindump/mapdat/"+i[0]+".dat","wb")
                self.ship.execute("select * from {}".format(i[0],))
                while True:
                    S = self.ship.fetchone()
                    if S == None:
                        break
                    binfil.write(S[0].to_byte(1,"big"))
                binfil.close()
            elif i[1] not in q.keys():
                binfil = open("./bindump/mapdat/"+i[0]+".png","wb")
                self.ship.execute("select * from {}".format(i[0],))
                while True:
                    S = self.ship.fetchone()
                    if S == None:
                        break
                    binfil.write(S[0].to_byte(1,"big"))
                binfil.close()
            else:
                pass
        S = {}
        for i in Q:
            S[i[0]] = i[1]
        dex.dump(S,binfil)
        binfil.close()
