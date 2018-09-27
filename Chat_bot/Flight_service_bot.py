
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from pandas.io.json import json_normalize
import json
import pandas as pd
from tkinter import *


# In[22]:


def flight_status(fid):
    
    fid=str(fid).strip()
    
       
    api_id='Provide api id'
        
    api_key='provide api key'
        
        
    url = "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/"
        
    fs_url= url+str(fid)+"?appId="+str(api_id)+"&appKey="+str(api_key)
    
    
        
    try:    

        url=urlopen(fs_url)
        js=json.load(url)
        
        fs=js['flightStatus']
        l=[]
        #status=['flightId','carrierFsCode','flightNumber','departureAirportFsCode','arrivalAirportFsCode','departureDate','arrivalDate','status']
        
        
        status=['status']
        
        for k,v in fs.items():
            if k in status:
                #print(k,v)
                l.append([k, v])
        return l


    except:  
        return "Please check the flightId"
      
        

    
    
    


# In[21]:


def airport_track(airport):
    
    date='2018/09/27'
    dep='dep'
    airport=str(airport).upper().strip()
    l=[]
    for hr in range(0,24):

        url= "https://api.flightstats.com/flex/flightstatus/rest/v2/json/airport/status/"
        
        ar=str(airport)+"/dep/"+str(date)+"/"+str(hr)
        
        app="?appId= (api id and app key need to be given )&utc=false&numHours=1&maxFlights=5"
        
        
        url_at=url+ar+app
        
        
        
        
        
        try:
        
            js=json.load(urlopen(url_at))
        
            m=json_normalize(js,'flightStatuses')
            
            l.append(m['flightId'])
                
            
            
        except:
            
            pass
        
    if len(l)==0:
        return "Kindly check the Airport Code"
        
    else:
        return l
        


# In[24]:


window=Tk()

window.title("Chat service")
window.geometry("500x530")
window.resizable(0,0)

ChatLog = Text(window, bd=0, bg="white", height="10", width="700", font="Arial")
ChatLog.insert(END, "Kindly Enter flightId or Airport code to avail the service..\n\n\n")
ChatLog.config(state=DISABLED)

EntryBox = Text(window, bd=0, bg="yellow",fg="Black",width="29", height="10", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)

ChatLog.place(x=6,y=6, height=386, width=370)

EntryBox.place(bordermode=OUTSIDE,x=10, y=400, height=90, width=365)



SendButton = Button(window, font=30, text="Send", width="12", height=5,
                    bd=50, bg="green", activebackground="red",
                    activeforeground="pink", highlightcolor = "blue",
                    command=ClickAction)

SendButton.place(x=385, y=405, height=80)

window.mainloop()


# In[15]:


def ClickAction():
    #Write message to chat window

    
    EntryText=message(EntryBox.get("0.0",END))
    
    
    you(ChatLog, EntryText)
    
    EntryText=EntryText.strip()

    
    
    
    
    etxt=status(EntryText)
    
    etxt=message(etxt)
    
    
    ChatLog.yview(END)
    EntryBox.delete("0.0",END)
    

    Bot(ChatLog, etxt)

    
    
    




# In[16]:


def status(data):
    
    if data.isdigit():
        
        result= flight_status(data)
        
    else:
        result=airport_track(data)
    
    return result
    


# In[17]:


def you(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


# In[18]:


def Bot(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            try:
                LineNumber = float(ChatLog.index('end'))-1.0
            except:
                pass
          
            ChatLog.insert(END, "Bot: " + EntryText)
            ChatLog.tag_add("Bot:", LineNumber, LineNumber+1.6)
 
            ChatLog.tag_config("Bot:", foreground="#04B404", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


# In[19]:


def PressAction(event):
 
    EntryBox.config(state=NORMAL)
    ClickAction()
     
def DisableEntry(event):
    EntryBox.config(state=DISABLED)


# In[20]:


def message(EntryText):

    
    EntryText=str(EntryText).strip()

    for i in range(0,len(EntryText), 1):
        return EntryText[i:]+'\n'

    return ''

