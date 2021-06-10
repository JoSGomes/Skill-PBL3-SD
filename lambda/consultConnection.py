import mysql.connector
import sys
import os
from datetime import datetime, timedelta, timezone

def consult_connection():
    ENDPOINT="pbl.cxqwhnwtx9nu.us-east-1.rds.amazonaws.com"
    PORT="3306"
    USR="admin"
    REGION="us-east-1"
    DBNAME="pbl"
    
    delta = timedelta(hours=-3)
    fuso = timezone(delta)
    
    data_e_hora_atuais = datetime.now()
    atual = data_e_hora_atuais.astimezone(fuso)
    
    horalocal = atual.strftime('%H:%M:%S')
    diaAtual = int(atual.strftime('%d'))
    
    conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd="password", port=PORT, database=DBNAME)
    cur = conn.cursor()
    
    cur.execute("SELECT `hour` FROM pbl.connections where id=1")
    lastPostingHour = str(cur.fetchall()).replace("(", "").replace(")", "").replace(",","").replace("'","").replace("[","").replace("]","")
    
    cur.execute("SELECT `day` FROM pbl.connections where id=1")
    lastPostingDay = int(str(cur.fetchall()).replace("(", "").replace(")", "").replace(",","").replace("'","").replace("[","").replace("]",""))
    
    cur.execute("SELECT `interval` FROM pbl.connections where id=1")
    interval = str(cur.fetchall()).replace("(", "").replace(")", "").replace(",","").replace("'","").replace("[","").replace("]","")
    interval = int(interval)
    
    lastPostingHourSplited = lastPostingHour.split(":", 3)
    lastPostingHourSum = int(lastPostingHourSplited[0])*3600 + int(lastPostingHourSplited[1])*60 + int(lastPostingHourSplited[2])*1
    
    horalocalSplited = horalocal.split(":", 3)
    
    actualHourSum = int(horalocalSplited[0])*3600 + int(horalocalSplited[1])*60 + int(horalocalSplited[2])*1
    if(lastPostingDay >= diaAtual):
        if(lastPostingHourSum+interval >= actualHourSum):
            return("CONECTADA")
        else:
            cur.execute("UPDATE pbl.connections SET value = 'Desconectada' WHERE id ='1'")
            conn.commit()
            return("DESCONECTADA")
    else:
        cur.execute("UPDATE pbl.connections SET value = 'Desconectada' WHERE id ='1'")
        conn.commit()
        return("DESCONECTADA")