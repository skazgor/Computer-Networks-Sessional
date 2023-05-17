import matplotlib.pyplot as plt

x=[250,500,750,1000,1250]
yt, ya, yd, ydr = [], [], [], []
# read data from file
with open("area.txt", "r") as file:
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

print(x)
print(yt)
# plot graph
plt.plot(x,yt, label="Area size(m) vs Throughtput")
plt.xlabel('Area size(m)')
plt.ylabel('Throughput')
plt.savefig('areaVsThroughput.png')
plt.close()
# plt.show()
plt.plot(x,ya, label="Area size(m) vs Average Delay")
plt.xlabel('Area size(m)')
plt.ylabel('Average Delay')
plt.savefig('areaVsAverageDelay.png')
# plt.show()
plt.close()
plt.plot(x,yd, label="Area size(m) vs Delivery ratio")
plt.xlabel('Area size(m)')
plt.ylabel('Delivery ratio')
plt.savefig('areaVsDeliveryRatio.png')
# plt.show()
plt.close()
plt.plot(x,ydr, label="Area size(m) vs Drop ratio")
plt.xlabel('Area size(m)')
plt.ylabel('Drop ratio')
plt.savefig('areaVsDropRatio.png')
# plt.show()
plt.close()


# flow
x=[10,20,30,40,50]
yt, ya, yd, ydr = [], [], [], []
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

#plot graph
 
plt.plot(x,yt, label="Number of flow vs Throughtput")    
plt.xlabel('Number of flow')
plt.ylabel('Throughput')
plt.savefig('flowVsThroughput.png')
plt.close()
plt.plot(x,ya, label="Number of flow vs Average Delay")
plt.xlabel('Number of flow')
plt.ylabel('Average Delay')
plt.savefig('flowVsAverageDelay.png')
plt.close()
plt.plot(x,yd, label="Number of flow vs Delivery ratio")
plt.xlabel('Number of flow')
plt.ylabel('Delivery ratio')
plt.savefig('flowVsDeliveryRatio.png')
plt.close()
plt.plot(x,ydr, label="Number of flow vs Drop ratio")
plt.xlabel('Number of flow')
plt.ylabel('Drop ratio')
plt.savefig('flowVsDropRatio.png')
plt.close()

# node
x=[20,40,60,80,100]
yt, ya, yd, ydr = [], [], [], []
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

plt.plot(x,yt, label="Number of node vs Throughtput")
plt.xlabel('Number of node')
plt.ylabel('Throughput')
plt.savefig('nodeVsThroughput.png')
plt.close()
plt.plot(x,ya, label="Number of node vs Average Delay")
plt.xlabel('Number of node')
plt.ylabel('Average Delay')
plt.savefig('nodeVsAverageDelay.png')
plt.close()
plt.plot(x,yd, label="Number of node vs Delivery ratio")
plt.xlabel('Number of node')
plt.ylabel('Delivery ratio')
plt.savefig('nodeVsDeliveryRatio.png')
plt.close()
plt.plot(x,ydr, label="Number of node vs Drop ratio")
plt.xlabel('Number of node')
plt.ylabel('Drop ratio')
plt.savefig('nodeVsDropRatio.png')
plt.close()     
