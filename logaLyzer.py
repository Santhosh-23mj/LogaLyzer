#!/usr/bin/env python3

""" 
Analysis Module 
"""
from tkinter import filedialog

class Data:
    """
    Data class stores the data from the log file
    """
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
    """
    LogLyzer class reads the log file and saves all the data in easily
    consumable form
    """
    
    objArray = []
    ipList   = []
    f        = None
    ipReq    = {}
    cumIpReq = {}
    cumReq   = {}
    cumRes   = {}
    cumUA    = {}
    cumFile  = {}
    cumDate  = {}
    cumTms   = {}

    
    def open_file(self):
        """
        This function prompts the user to select the file that is to be analyzed
        in the GUI window.

        Returns
        -------
        Data stored in class variables

        """
        self.f = filedialog.askopenfile(mode='r')
        self.readFile(self.f)
        self.getCumulative()
        
    def freeMem(self):
        """
        This functions clears all variables makes the application ready for the
        next run.

        Returns
        -------
        None.

        """
        self.objArray.clear()
        self.ipList.clear()
        self.f = None
        self.ipReq.clear()
        self.cumIpReq.clear()
        self.cumReq.clear()
        self.cumRes.clear()
        self.cumUA.clear()
        self.cumFile.clear()
        self.cumDate.clear()
        self.cumTms.clear()

    def returnSortDic(self, dic):
        """
        This functions sorts a given dictionary in descending order based on values.

        Parameters
        ----------
        dic : Dictionary
            Unsorted dictionary

        Returns
        -------
        dic : Dictionary
            A dictionary sorted in descending order based on values.

        """
        dic = sorted(dic.items(), key = lambda kv:(kv[1],kv[0]))
        dic.reverse()
        return dict(dic)
    
    
    def getCumulative(self):
        """
        This function reads all the Data Objects and cumulates it, total requests
        responses, File access and User-Agents are calculated and stored in class
        variables in descending order of frequencies.

        Returns
        -------
        Data is stored in class variables

        """
        for obj in self.objArray:
            #print(obj.tms)
            self.cumIpReq[obj.ip] = sum(list(obj.req.values()))
            for k,v in obj.req.items():
                self.cumReq[k] = self.cumReq.get(k,0) + v
            for k,v in obj.res.items():
                self.cumRes[k] = self.cumRes.get(k,0) + v
            for ua in obj.UA:
                self.cumUA[ua] = self.cumUA.get(ua,0) + 1
            for k,v in obj.file.items():
                self.cumFile[k] = self.cumFile.get(k,0) + v
            for key in obj.tms:
                self.cumDate[key] = self.cumDate.get(key,0) + sum(list(obj.tms[key].values()))
            for key,values in obj.tms.items():
                #print(key,values)
                for k in values:
                    if(key in self.cumTms.keys()):
                        self.cumTms[key][k] = self.cumTms[key].get(k,0) + values[k]
                    else:
                        self.cumTms[key] = {}
                        self.cumTms[key][k] = values[k]            
        self.ipReq = self.cumIpReq
        self.cumIpReq = self.returnSortDic(self.cumIpReq)
        self.cumReq   = self.returnSortDic(self.cumReq)
        self.cumRes   = self.returnSortDic(self.cumRes)
        self.cumUA    = self.returnSortDic(self.cumUA)
        self.cumFile  = self.returnSortDic(self.cumFile)
        #print(self.cumTms)


    def readFile(self, f):
        """
        This function reads the file line by line and groups data based on IP address
        on different variables

        Parameters
        ----------
        f : file object
            The file object to read data for analysis

        Returns
        -------
        Data stored in Class variables.

        """
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
                    date = temp[3].replace("[","").split(":")[0]
                    hr   = temp[3].split(":")[1]
                    obj.tms[date] = {hr:1}
                    #obj.tms[temp[3].replace("[","").split("/")[0]] = obj.tms.get(temp[3].replace("[",""),0) + 1
                    self.objArray.append(obj)
                else:
                    index = self.ipList.index(temp[0])
                    self.objArray[index].req[temp[5]] = self.objArray[index].req.get(temp[5], 0) + 1
                    self.objArray[index].res[temp[8]] = self.objArray[index].res.get(temp[8], 0) + 1
                    self.objArray[index].file[temp[6]] = self.objArray[index].file.get(temp[6], 0) + 1
                    if( ' '.join(temp[11:]) not in self.objArray[index].UA ):
                        self.objArray[index].UA.append(' '.join(temp[11:]))
                    date = temp[3].replace("[","").split(":")[0]
                    hr   = temp[3].split(":")[1]
                    if(date in self.objArray[index].tms.keys()):
                        self.objArray[index].tms[date][hr] = self.objArray[index].tms[date].get(hr,0) + 1
                    else:
                        self.objArray[index].tms[date] = {}
                        self.objArray[index].tms[date][hr] = self.objArray[index].tms[date].get(hr,0) + 1
                    #self.objArray[index].tms[temp[3].replace("[","").split(":")[0]] = self.objArray[index].tms.get(temp[3].replace("[",""), 0) + 1
