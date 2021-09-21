
a="" 
import asyncio
import websockets
import ssl
import random
import moderateur
async def hello(websocket, path):
    a,group=str(await websocket.recv()).split("[group]")
    a=a.lower()
    print("____connection:"+a)
    try:
        with open("Answer_l.txt","r")as fic:
            
            Answer_l=fic.read().split(";")
        with open("Question_l.txt","r")as fic:
            
            Question_l=fic.read().split(";")
        with open("bad.txt","r")as fic:
            bad=fic.read()
        with open("good.txt","r")as fic:
            good=fic.read()
    except Exception as e:
        print(e)    
        Question_l=[]
        Answer_l=[] 
    print(Question_l)
    finder=False
    
    I=0
    re_data=[]
    if(moderateur.main(a.replace("<message>",""),good,bad)=="good"):
        if(a.find("<message>") !=-1 and a.find("<new>")==-1):
            for el in Question_l:
                i_word=0
                
                for word in a.replace("<message>","").split(" "):
                    
                    if(el.find(word) !=-1):
                        i_word+=1
                     
                
                if(el.find("["+group+"]")==-1):
                    print(el)
                    i_word=0
                if(i_word/len(a.replace("<message>","").split(" "))>0.65):
                    
                    if(str(Question_l).find(Answer_l[I])!=-1):
                        re_data.append(Answer_l[I])
                    else:
                        
                        re_data.append("<new>"+Answer_l[I])
                    finder=True
                    print(I) 
                I+=1
            if(finder==False):
                await websocket.send("<new>"+a)
               

        if(len(re_data) !=0):
            if(len(re_data)==1):
                await websocket.send(re_data[0])
            else:
                await websocket.send(random.choice(re_data))
                
        if(a.find("<new>") !=-1):
             
            finder=False
            if(len(a.split(" "))<2):
                 await websocket.send("<new>"+a.split("<new>")[1].split("[/]")[1])
                 print(a) 
                 b=a.split("<new>")[1].split("[/]")[1]
                 print(b)
                 with open("Question_l.txt","a")as fic:
                     fic.write(a.split("<new>")[1].split("[/]")[0]+";")
                 with open("Answer_l.txt","a")as fic:
                     fic.write(b+";") 
                 
                 Answer_l.append(b)
                 Question_l.append(a.split("<new>")[1].split("[/]")[0])
                 I=0
                 for el in Question_l:
                    if(el.find(b)!=-1):
                         
                        await websocket.send(Answer_l[I])
                        print("61")
                        finder=True
                        print(I) 
                    I+=1
              
                 """
                 with open("Question_l.txt","w")as fic:
                     fic.write(a+";")
                 with open("Answer_l.txt","w")as fic:
                     fic.write(b+";")
                 """
            else:
                 if(moderateur.main(a.split("<new>")[1].split("[/]")[1],good,bad)=="good"):
                     await websocket.send("<new>"+a.split("<new>")[1].split("[/]")[1])
                     print(a) 
                     b=a.split("<new>")[1].split("[/]")[1]
                     print(b)
                     with open("Question_l.txt","a")as fic:
                         fic.write(a.split("<new>")[1].split("[/]")[0]+"["+group+"]"+";")
                     with open("Answer_l.txt","a")as fic:
                         fic.write(b+";") 
                     
                     Answer_l.append(b)
                     Question_l.append(a.split("<new>")[1].split("[/]")[0])
                     I=0
                     for el in Question_l:
                        if(el.find(b)!=-1):
                             
                            await websocket.send(Answer_l[I])
                            print("61")
                            finder=True
                            print(I) 
                        I+=1
            
               
    else:
        await websocket.send("désolé je veux pas parler de ce sujet")   
ssl_root="/etc/letsencrypt/live/youlink.ddns.net"
ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(ssl_root+"/fullchain.pem",
                    ssl_root + "/privkey.pem")
start_server = websockets.serve(hello, '', 8765,ssl=ssl_ctx)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
    
    
   
