import socket

s = socket.socket()
s.bind(("127.0.0.1", 4028))
s.listen()

MSGS = {
    "version": None,
    "summary": None,
    "config": None,
    "pools": None,
    "devs": None,
    "lcd": b'{"STATUS":[{"STATUS":"S","When":1512963848,"Code":7,"Msg":"3 Pool(s)","Description":"cgminer 4.8.0"}],"POOLS":[,{"LCD":"0","GHS5s":5179.07,"GHSavg":4810.16,"fan":"4200","temp":"62","pool":"stratum+tcp://us-east.stratum.slushpool.com:3333","user":"allen_santos.001"}],"id":1}',
    "stats": b'{"STATUS":[{"STATUS":"S","When":1512965718,"Code":70,"Msg":"CGMiner stats","Description":"cgminer 4.8.0"}],"STATS":[{"CGMiner":"4.8.0","Miner":"3.5.3.0","CompileTime":"Thu Dec  3 16:07:54 CST 2015","Type":"Antminer S7"}{"STATS":0,"ID":"BTM0","Elapsed":83764,"Calls":0,"Wait":0.000000,"Max":0.000000,"Min":99999999.000000,"GHS 5s":5130.11,"GHS av":4814.29,"baud":115200,"miner_count":3,"asic_count":8,"timeout":5,"frequency":"750","voltage":"0.706","hwv1":3,"hwv2":5,"hwv3":3,"hwv4":0,"fan_num":6,"fan1":4200,"fan2":0,"fan3":4080,"fan4":0,"fan5":0,"fan6":0,"fan7":0,"fan8":0,"fan9":0,"fan10":0,"fan11":0,"fan12":0,"fan13":0,"fan14":0,"fan15":0,"fan16":0,"temp_num":3,"temp1":54,"temp2":56,"temp3":62,"temp4":0,"temp5":0,"temp6":0,"temp7":0,"temp8":0,"temp9":0,"temp10":0,"temp11":0,"temp12":0,"temp13":0,"temp14":0,"temp15":0,"temp16":0,"temp_avg":57,"temp_max":65,"Device Hardware%":0.0231,"no_matching_work":21683,"chain_acn1":45,"chain_acn2":45,"chain_acn3":45,"chain_acn4":0,"chain_acn5":0,"chain_acn6":0,"chain_acn7":0,"chain_acn8":0,"chain_acn9":0,"chain_acn10":0,"chain_acn11":0,"chain_acn12":0,"chain_acn13":0,"chain_acn14":0,"chain_acn15":0,"chain_acn16":0,"chain_acs1":"oooooooo ooooo oooooooo oooooooo oooooooo oooooooo ","chain_acs2":"oooooooo ooooo oooooooo oooooooo oooooooo oooooooo ","chain_acs3":"oooooooo ooooo oooooooo oooooooo oooooooo oooooooo ","chain_acs4":"","chain_acs5":"","chain_acs6":"","chain_acs7":"","chain_acs8":"","chain_acs9":"","chain_acs10":"","chain_acs11":"","chain_acs12":"","chain_acs13":"","chain_acs14":"","chain_acs15":"","chain_acs16":"","USB Pipe":"0"}],"id":1}',
    "notify": b'{"STATUS":[{"STATUS":"S","When":1512966267,"Code":60,"Msg":"Notify","Description":"cgminer 4.8.0"}],"NOTIFY":[{"NOTIFY":0,"Name":"BTM","ID":0,"Last Well":1512966267,"Last Not Well":0,"Reason Not Well":"None","*Thread Fail Init":0,"*Thread Zero Hash":0,"*Thread Fail Queue":0,"*Dev Sick Idle 60s":0,"*Dev Dead Idle 600s":0,"*Dev Nostart":0,"*Dev Over Heat":0,"*Dev Thermal Cutoff":0,"*Dev Comms Error":0,"*Dev Throttle":0}],"id":1}',
}


while True:
    conn, addr = s.accept()

    key = conn.recv(1024)

    print("Server got: {}".format(key.decode()))

    conn.send(MSGS[key])
