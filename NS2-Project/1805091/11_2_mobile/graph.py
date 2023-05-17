import matplotlib.pyplot as plt
i=0
x_individual=[[],[],[],[],[]]
x=[20,40,60,80,100]
yt, ya, yd, ydr , ey , epby= [], [], [], [] , [] , []
# read data from file
with open("node.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(len(columns)==1):
            i+=1
            continue
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
        elif(columns[0]=="Node"):
            node = int(columns[1])
            x_individual[i].append(float(columns[3]))

print(x)
print(yt)
# plot graph
plt.plot(x,yt, label="Number of Node vs Throughtput")
plt.xlabel('Number of Node')
plt.ylabel('Throughput')
plt.savefig('Fig/NumberofNodevsThroughput.png')
plt.close()
# plt.show()
print(ya)
plt.plot(x,ya, label="Number of Node vs Average Delay")
plt.xlabel('Number of Node')
plt.ylabel('Average Delay')
plt.savefig('Fig/NumberofNodevsAverageDelay.png')
# plt.show()
plt.close()
print(yd)
plt.plot(x,yd, label="Number of Node vs Delivery ratio")
plt.xlabel('Number of Node')
plt.ylabel('Delivery ratio')
plt.savefig('Fig/NumberofNodevsDeliveryRatio.png')
# plt.show()
plt.close()
print(ydr)
plt.plot(x,ydr, label="Number of Node vs Drop ratio")
plt.xlabel('Number of Node')
plt.ylabel('Drop ratio')
plt.savefig('Fig/NumberofNodevsDropRatio.png')
# plt.show()
plt.close()
print(ey)
plt.plot(x,ey, label="Number of Node vs Total Energy Consumption")
plt.xlabel('Number of Node')
plt.ylabel('Total Energy Consumption')
plt.savefig('Fig/NumberofNodevsTotalEnergyConsumption.png')
# plt.show()
plt.close()
print(epby)
plt.plot(x,epby, label="Number of Node vs Energy Consumption per Byte")
plt.xlabel('Number of Node')
plt.ylabel('Energy Consumption per Byte')
plt.savefig('Fig/NumberofNodevsEnergyConsumptionperByte.png')
# plt.show()
plt.close()
number_of_node=20
for arr in x_individual:
    print(arr)
    x_axis=range(1,arr.__len__()+1)
    plt.plot(x_axis,arr, label=f"Number of Node({number_of_node})vs per Node Throughput")
    plt.xlabel('Number of Node')
    plt.ylabel('per Node Throughput')
    plt.savefig(f'Fig/NumberofNode({number_of_node})vsperNodeThroughput.png')
    # plt.show()
    plt.close()
    number_of_node+=20

# flow
x_individual=[[],[],[],[],[]]
i=0
x=[10,20,30,40,50]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("flow.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(len(columns)==1):
            i+=1
            continue
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
        elif(columns[0]=="Node"):
            node = int(columns[1])
            x_individual[i].append(float(columns[3]))


#plot graph
print(x)
print(yt)
plt.plot(x,yt, label="Number of flow vs Throughtput")    
plt.xlabel('Number of flow')
plt.ylabel('Throughput')
plt.savefig('Fig/NumberofflowvsThroughput.png')
plt.close()
print(ya)
plt.plot(x,ya, label="Number of flow vs Average Delay")
plt.xlabel('Number of flow')
plt.ylabel('Average Delay')
plt.savefig('Fig/NumberofflowvsAverageDelay.png')
plt.close()
print(yd)
plt.plot(x,yd, label="Number of flow vs Delivery ratio")
plt.xlabel('Number of flow')
plt.ylabel('Delivery ratio')
plt.savefig('Fig/NumberofflowvsDeliveryRatio.png')
plt.close()
print(ydr)
plt.plot(x,ydr, label="Number of flow vs Drop ratio")
plt.xlabel('Number of flow')
plt.ylabel('Drop ratio')
plt.savefig('Fig/NumberofflowvsDropRatio.png')
plt.close()
print(ey)
plt.plot(x,ey, label="Number of flow vs Total Energy Consumption")
plt.xlabel('Number of flow')
plt.ylabel('Total Energy Consumption')
plt.savefig('Fig/NumberofflowvsTotalEnergyConsumption.png')
plt.close()
print(epby)
plt.plot(x,epby, label="Number of flow vs Energy Consumption per Byte")
plt.xlabel('Number of flow')
plt.ylabel('Energy Consumption per Byte')
plt.savefig('Fig/NumberofflowvsEnergyConsumptionperByte.png')
plt.close()
number_of_flow=10
for arr in x_individual:
    print(arr)
    x_axis=range(1,arr.__len__()+1)
    plt.plot(x_axis,arr, label=f"Number of flow({number_of_flow})vs per Node Throughput")
    plt.xlabel('Number of flow')
    plt.ylabel('per Node Throughput')
    plt.savefig(f'Fig/Numberofflow({number_of_flow})vsperNodeThroughput.png')
    plt.close()
    number_of_flow+=10

# speed
x_individual=[[],[],[],[],[]]
i=0
x=[5,10,15,20,25]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("speed.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(len(columns)==1):
            i+=1
            continue
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
        elif(columns[0]=="Node"):
            node = int(columns[1])
            x_individual[i].append(float(columns[3]))

#plot graph
print(x)
print(yt)
plt.plot(x,yt, label="Speed vs Throughtput")
plt.xlabel('Speed')
plt.ylabel('Throughput')
plt.savefig('Fig/SpeedvsThroughput.png')
plt.close()
print(ya)
plt.plot(x,ya, label="Speed vs Average Delay")
plt.xlabel('Speed')
plt.ylabel('Average Delay')
plt.savefig('Fig/SpeedvsAverageDelay.png')
plt.close()
print(yd)
plt.plot(x,yd, label="Speed vs Delivery ratio")
plt.xlabel('Speed')
plt.ylabel('Delivery ratio')
plt.savefig('Fig/SpeedvsDeliveryRatio.png')
plt.close()
print(ydr)
plt.plot(x,ydr, label="Speed vs Drop ratio")    
plt.xlabel('Speed')
plt.ylabel('Drop ratio')
plt.savefig('Fig/SpeedvsDropRatio.png')
plt.close()
print(ey)
plt.plot(x,ey, label="Speed vs Total Energy Consumption")
plt.xlabel('Speed')
plt.ylabel('Total Energy Consumption')
plt.savefig('Fig/SpeedvsTotalEnergyConsumption.png')
plt.close()
print(epby)
plt.plot(x,epby, label="Speed vs Energy Consumption per Byte")
plt.xlabel('Speed')
plt.ylabel('Energy Consumption per Byte')
plt.savefig('Fig/SpeedvsEnergyConsumptionperByte.png')
plt.close()
speed_=5
for arr in x_individual:
    print(arr)
    x_axis=range(1,arr.__len__()+1)
    plt.plot(x_axis,arr, label=f"Speed({speed_})vs per Node Throughput")
    plt.xlabel('Speed')
    plt.ylabel('per Node Throughput')
    plt.savefig(f'Fig/Speed({speed_})vsperNodeThroughput.png')
    plt.close()
    speed_+=5

# Packet per second
x_individual=[[],[],[],[],[]]
i=0
x=[100,200,300,400,500]
yt, ya, yd, ydr,ey,epby = [], [], [], [],[],[]
with open("packet.txt", "r") as file:
    for line in file:
        # split line into columns
        columns = line.split(": ")
        if(len(columns)==1):
            i+=1
            continue
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
        elif(columns[0]=="Node"):
            node = int(columns[1])
            x_individual[i].append(float(columns[3]))

#plot graph
print(x)
print(yt)
plt.plot(x,yt, label="Packet per second vs Throughtput")
plt.xlabel('Packet per second')
plt.ylabel('Throughput')
plt.savefig('Fig/PacketpersecondvsThroughput.png')
plt.close()
print(ya)
plt.plot(x,ya, label="Packet per second vs Average Delay")
plt.xlabel('Packet per second')
plt.ylabel('Average Delay')
plt.savefig('Fig/PacketpersecondvsAverageDelay.png')
plt.close()
print(yd)
plt.plot(x,yd, label="Packet per second vs Delivery ratio")
plt.xlabel('Packet per second')
plt.ylabel('Delivery ratio')
plt.savefig('Fig/PacketpersecondvsDeliveryRatio.png')
plt.close()
print(ydr)
plt.plot(x,ydr, label="Packet per second vs Drop ratio")
plt.xlabel('Packet per second')
plt.ylabel('Drop ratio')
plt.savefig('Fig/PacketpersecondvsDropRatio.png')
plt.close()
print(ey)
plt.plot(x,ey, label="Packet per second vs Total Energy Consumption")
plt.xlabel('Packet per second')
plt.ylabel('Total Energy Consumption')
plt.savefig('Fig/PacketpersecondvsTotalEnergyConsumption.png')
plt.close()
print(epby)
plt.plot(x,epby, label="Packet per second vs Energy Consumption per Byte")
plt.xlabel('Packet per second')
plt.ylabel('Energy Consumption per Byte')
plt.savefig('Fig/PacketpersecondvsEnergyConsumptionperByte.png')
plt.close()
number_of_packet=100
for arr in x_individual:
    print(arr)
    x_axis=range(1,arr.__len__()+1)
    plt.plot(x_axis,arr, label=f"Packet per second({number_of_packet})vs per Node Throughput")
    plt.xlabel('Packet per second')
    plt.ylabel('per Node Throughput')
    plt.savefig(f'Fig/Packetpersecond({number_of_packet})vsperNodeThroughput.png')
    plt.close()
    number_of_packet+=100



