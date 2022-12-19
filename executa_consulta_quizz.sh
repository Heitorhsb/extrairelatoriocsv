#!/bin/bash
mongosh < /scriptspython/excluiecriacollection.js
sleep 10s
/scriptspython/coleta.py
sleep 10s
/scriptspython/corrigejson.py
sleep 10s
/scriptspython/reprocessajson.py
sleep 10s
/scriptspython/enviarelatorio.py
exit

