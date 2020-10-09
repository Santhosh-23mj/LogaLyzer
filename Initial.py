#!/usr/bin/env python3

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
    def __init__(self, filename):
        self.filename = filename
    
    def readFile(self):
        with open(self.filename) as f:
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

def main():
    log = LogLyzer("varysample")
    log.readFile()
    for obj in log.objArray:
        print(obj.ip)
        print(obj.req)
        print(obj.res)
        print(obj.UA)
        print(obj.file)
        print(obj.tms)
        print("\n")

main()