#!/usr/bin/env python3

""" 
Analysis Module 
"""
from tkinter import filedialog

class Data:
    def __init__(self, ip):
        self.ip   = ip
        self.req  = {}
        self.res  = {}
        self.UA   = []
        self.file = {}
        self.tms  = {}
    
    def __repr__(self):
        return self.ip

class LogLyzer:
    
    objArray = []
    ipList   = []
    f        = None
    ipReq    = {}
    cumIpReq = {}
    cumReq   = {}
    cumRes   = {}
    cumUA    = {}
    cumFile  = {}

    
    def open_file(self):
        self.f = filedialog.askopenfile(mode='r')
        self.readFile(self.f)
        self.getCumulative()
        
    def freeMem(self):
        self.objArray.clear()
        self.ipList.clear()
        self.f = None
        self.ipReq.clear()
        self.cumIpReq.clear()
        self.cumReq.clear()
        self.cumRes.clear()
        self.cumUA.clear()
        self.cumFile.clear()

    def returnSortDic(self, dic):
        dic = sorted(dic.items(), key = lambda kv:(kv[1],kv[0]))
        dic.reverse()
        return dic
    
    
    def getCumulative(self):
        for obj in self.objArray:
            self.cumIpReq[obj.ip] = sum(list(obj.req.values()))
            for k,v in obj.req.items():
                self.cumReq[k] = self.cumReq.get(k,0) + v
            for k,v in obj.res.items():
                self.cumRes[k] = self.cumRes.get(k,0) + v
            for ua in obj.UA:
                self.cumUA[ua] = self.cumUA.get(ua,0) + 1
            for k,v in obj.file.items():
                self.cumFile[k] = self.cumFile.get(k,0) + v
        self.ipReq = self.cumIpReq
        self.cumIpReq = dict(self.returnSortDic(self.cumIpReq))
        self.cumReq   = dict(self.returnSortDic(self.cumReq))
        self.cumRes   = dict(self.returnSortDic(self.cumRes))
        self.cumUA    = dict(self.returnSortDic(self.cumUA))
        self.cumFile  = dict(self.returnSortDic(self.cumFile))


    def readFile(self, f):
        while True:
            line = f.readline().replace("\"","").strip()
            if(not line):
                break
            else:
                temp = line.split()
                if( temp[0] not in self.ipList ):
                    self.ipList.append(temp[0])
                    obj = Data(temp[0])
                    obj.req[temp[5]] = obj.req.get(temp[5],0) + 1
                    obj.res[temp[8]] = obj.res.get(temp[8],0) + 1
                    obj.file[temp[6]] = obj.file.get(temp[6],0) + 1
                    obj.UA.append(' '.join(temp[11:]))
                    obj.tms[temp[3].replace("[","")] = obj.tms.get(temp[3].replace("[",""),0) + 1
                    self.objArray.append(obj)
                else:
                    index = self.ipList.index(temp[0])
                    self.objArray[index].req[temp[5]] = self.objArray[index].req.get(temp[5], 0) + 1
                    self.objArray[index].res[temp[8]] = self.objArray[index].res.get(temp[8], 0) + 1
                    self.objArray[index].file[temp[6]] = self.objArray[index].file.get(temp[6], 0) + 1
                    if( ' '.join(temp[11:]) not in self.objArray[index].UA ):
                        self.objArray[index].UA.append(' '.join(temp[11:]))
                    self.objArray[index].tms[temp[3].replace("[","")] = self.objArray[index].tms.get(temp[3].replace("[",""), 0) + 1
