import matplotlib.pyplot as plt

x=[20,40,60,80,100]
yt, ya, yd, ydr , ey , epby= [], [], [], [] , [] , []
# read data from file
with open("node.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            yt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            ya.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            yd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ydr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ey.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            epby.append(float(columns[1]))
            
nt, na, nd, ndr,ney,nepby = [], [], [], [],[],[]
with open("newnode.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            nt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            na.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            nd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ndr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ney.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            nepby.append(float(columns[1]))

print(x)
print(yt)
print("Modified")
print(nt)
# plot graph
plt.Color='red'
plt.plot(x,yt, label="Number of Node vs Throughtput")
plt.Color='green'
plt.plot(x,nt)
plt.xlabel('Number of Node')
plt.ylabel('Throughput')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsThroughput.png')
plt.close()
# plt.show()
print(ya)
print("Modified")
print(na)
plt.Color='red'
plt.plot(x,ya, label="Number of Node vs Average Delay")
plt.Color='green'
plt.plot(x,na)
plt.xlabel('Number of Node')
plt.ylabel('Average Delay')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsAverageDelay.png')
# plt.show()
plt.close()
print(yd)
print("Modified")
print(nd)
plt.Color='red'
plt.plot(x,yd, label="Number of Node vs Delivery ratio")
plt.Color='green'
plt.plot(x,nd)
plt.xlabel('Number of Node')
plt.ylabel('Delivery ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsDeliveryRatio.png')
# plt.show()
plt.close()
print(ydr)
print("Modified")
print(ndr)
plt.Color='red'
plt.plot(x,ydr, label="Number of Node vs Drop ratio")
plt.Color='green'
plt.plot(x,ndr)
plt.xlabel('Number of Node')
plt.ylabel('Drop ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsDropRatio.png')
# plt.show()
plt.close()
print(ey)
print("Modified")
print(ney)
plt.Color='red'
plt.plot(x,ey, label="Number of Node vs Total Energy Consumption")
plt.Color='green'
plt.plot(x,ney)
plt.xlabel('Number of Node')
plt.ylabel('Total Energy Consumption')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsTotalEnergyConsumption.png')
# plt.show()
plt.close()
print(epby)
print("Modified")
print(nepby)
plt.Color='red'
plt.plot(x,epby, label="Number of Node vs Energy Consumption per Byte")
plt.Color='green'
plt.plot(x,nepby)
plt.xlabel('Number of Node')
plt.ylabel('Energy Consumption per Byte')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofNodevsEnergyConsumptionperByte.png')
# plt.show()
plt.close()

#flow
x=[10,20,30,40,50]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("flow.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            yt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            ya.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            yd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ydr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ey.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            epby.append(float(columns[1]))
 
nt, na, nd, ndr,ney,nepby = [], [], [], [],[],[]
with open("newflow.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            nt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            na.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            nd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ndr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ney.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            nepby.append(float(columns[1]))
            
print(x)
print(yt)
print("Modified")
print(nt)
# plot graph
plt.Color='red'
plt.plot(x,yt, label="Number of Flow vs Throughtput")
plt.Color='green'
plt.plot(x,nt)
plt.xlabel('Number of Flow')
plt.ylabel('Throughput')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsThroughput.png')
plt.close()
print(ya)
print("Modified")
print(na)
plt.Color='red'
plt.plot(x,ya, label="Number of flow vs Average Delay")
plt.Color='green'
plt.plot(x,na)
plt.xlabel('Number of flow')
plt.ylabel('Average Delay')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsAverageDelay.png')
plt.close()
print(yd)
print("Modified")
print(nd)
plt.Color='red'
plt.plot(x,yd, label="Number of flow vs Delivery ratio")
plt.Color='green'
plt.plot(x,nd)
plt.xlabel('Number of flow')
plt.ylabel('Delivery ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsDeliveryRatio.png')
plt.close()
print(ydr)
print("Modified")
print(ndr)
plt.Color='red'
plt.plot(x,ydr, label="Number of flow vs Drop ratio")
plt.Color='green'
plt.plot(x,ndr)
plt.xlabel('Number of flow')
plt.ylabel('Drop ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsDropRatio.png')
plt.close()
print(ey)
print("Modified")
print(ney)
plt.Color='red'
plt.plot(x,ey, label="Number of flow vs Total Energy Consumption")
plt.Color='green'
plt.plot(x,ney)
plt.xlabel('Number of flow')
plt.ylabel('Total Energy Consumption')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsTotalEnergyConsumption.png')
plt.close()
print(epby)
print("Modified")
print(nepby)
plt.Color='red'
plt.plot(x,epby, label="Number of flow vs Energy Consumption per Byte")
plt.Color='green'
plt.plot(x,nepby)
plt.xlabel('Number of flow')
plt.ylabel('Energy Consumption per Byte')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/NumberofflowvsEnergyConsumptionperByte.png')
plt.close()

# speed
x=[5,10,15,20,25]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("speed.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            yt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            ya.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            yd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ydr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ey.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            epby.append(float(columns[1]))


nt, na, nd, ndr,ney,nepby = [], [], [], [],[],[]
with open("newspeed.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            nt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            na.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            nd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ndr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ney.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            nepby.append(float(columns[1]))
            

#plot graph
print(x)
print(yt)
print("Modified")
print(nt)
plt.Color='red'
plt.plot(x,yt, label="Speed vs Throughtput")
plt.Color='green'
plt.plot(x,nt)
plt.xlabel('Speed')
plt.ylabel('Throughput')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsThroughput.png')
plt.close()
print(ya)
print("Modified")
print(na)
plt.Color='red'
plt.plot(x,ya, label="Speed vs Average Delay")
plt.Color='green'
plt.plot(x,na)
plt.xlabel('Speed')
plt.ylabel('Average Delay')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsAverageDelay.png')
plt.close()
print(yd)
print("Modified")
print(nd)
plt.Color='red'
plt.plot(x,yd, label="Speed vs Delivery ratio")
plt.Color='green'
plt.plot(x,nd)
plt.xlabel('Speed')
plt.ylabel('Delivery ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsDeliveryRatio.png')
plt.close()
print(ydr)
print("Modified")
print(ndr)
plt.Color='red'
plt.plot(x,ydr, label="Speed vs Drop ratio")  
plt.Color='green'
plt.plot(x,ndr)  
plt.xlabel('Speed')
plt.ylabel('Drop ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsDropRatio.png')
plt.close()
print(ey)
print("Modified")
print(ney)
plt.Color='red'
plt.plot(x,ey, label="Speed vs Total Energy Consumption")
plt.Color='green'
plt.plot(x,ney)
plt.xlabel('Speed')
plt.ylabel('Total Energy Consumption')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsTotalEnergyConsumption.png')
plt.close()
print(epby)
print("Modified")
print(nepby)
plt.Color='red'
plt.plot(x,epby, label="Speed vs Energy Consumption per Byte")
plt.Color='green'
plt.plot(x,nepby)
plt.xlabel('Speed')
plt.ylabel('Energy Consumption per Byte')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/SpeedvsEnergyConsumptionperByte.png')
plt.close()

# Packet per second
x=[100,200,300,400,500]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("packet.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            yt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            ya.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            yd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ydr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ey.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            epby.append(float(columns[1]))

nt, na, nd, ndr,ney,nepby = [], [], [], [],[],[]
with open("newpacket.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(columns[0]=="Throughput"):
            nt.append(float(columns[1]))
        elif(columns[0]=="Average Delay"):
            na.append(float(columns[1]))
        elif(columns[0]=="Delivery ratio"):
            nd.append(float(columns[1]))
        elif(columns[0]=="Drop ratio"):
            ndr.append(float(columns[1]))
        elif(columns[0]=="Total Energy Consumption"):
            ney.append(float(columns[1]))
        elif(columns[0]=="Energy Consumption per Byte"):
            nepby.append(float(columns[1]))
#plot graph
print(x)
print(yt)
print("Modified")
print(nt)
plt.Color='red'
plt.plot(x,yt, label="Packet per second vs Throughtput")
plt.Color='green'
plt.plot(x,nt)
plt.xlabel('Packet per second')
plt.ylabel('Throughput')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsThroughput.png')
plt.close()
print(ya)
print("Modified")
print(na)
plt.Color='red'
plt.plot(x,ya, label="Packet per second vs Average Delay")
plt.Color='green'
plt.plot(x,na)
plt.xlabel('Packet per second')
plt.ylabel('Average Delay')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsAverageDelay.png')
plt.close()
print(yd)
print("Modified")
print(nd)
plt.plot(x,yd, label="Packet per second vs Delivery ratio")
plt.Color='green'
plt.plot(x,nd)
plt.xlabel('Packet per second')
plt.ylabel('Delivery ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsDeliveryRatio.png')
plt.close()
print(ydr)
print("Modified")
print(ndr)
plt.Color='red'
plt.plot(x,ydr, label="Packet per second vs Drop ratio")
plt.Color='green'
plt.plot(x,ndr)
plt.xlabel('Packet per second')
plt.ylabel('Drop ratio')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsDropRatio.png')
plt.close()
print(ey)
print("Modified")
print(ney)
plt.Color='red'
plt.plot(x,ey, label="Packet per second vs Total Energy Consumption")
plt.Color='green'
plt.plot(x,ney)
plt.xlabel('Packet per second')
plt.ylabel('Total Energy Consumption')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsTotalEnergyConsumption.png')
plt.close()
print(epby)
print("Modified")
print(nepby)
plt.Color='red'
plt.plot(x,epby, label="Packet per second vs Energy Consumption per Byte")
plt.Color='green'
plt.plot(x,nepby)
plt.xlabel('Packet per second')
plt.ylabel('Energy Consumption per Byte')
plt.legend(['Without Modification','With Modification'], loc='upper right',shadow=False)
plt.savefig('Fig/PacketpersecondvsEnergyConsumptionperByte.png')
plt.close()
