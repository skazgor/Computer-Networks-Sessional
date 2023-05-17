# #Vary the number of nodes
# ns wireless_mobile.tcl 20 20 5 100
# awk -v NN=20 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr > newnode.txt
# # echo "" >> newnode.txt
# ns wireless_mobile.tcl 40 20 5 100
# awk -v NN=40 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newnode.txt
# echo "" >> newnode.txt
# ns wireless_mobile.tcl 60 20 5 100
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newnode.txt
# echo "" >> newnode.txt
# ns wireless_mobile.tcl 80 20 5 100
# awk -v NN=80 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newnode.txt
# echo "" >> newnode.txt
# ns wireless_mobile.tcl 100 20 5 100
# awk -v NN=100 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newnode.txt

# #vary number of flows
# ns wireless_mobile.tcl 60 10 5 100
# awk -v NN=60 -v NF=10 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr > newflow.txt
# echo "" >> newflow.txt
# ns wireless_mobile.tcl 60 20 5 100
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newflow.txt
# echo "" >> newflow.txt
# ns wireless_mobile.tcl 60 30 5 100
# awk -v NN=60 -v NF=30 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newflow.txt
# echo "" >> newflow.txt
# ns wireless_mobile.tcl 60 40 5 100
# awk -v NN=60 -v NF=40 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newflow.txt
# echo "" >> newflow.txt
# ns wireless_mobile.tcl 60 50 5 100
# awk -v NN=60 -v NF=50 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newflow.txt

# #vary speed
# ns wireless_mobile.tcl 60 20 5 100
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr > newspeed.txt
# echo "" >> newspeed.txt
# ns wireless_mobile.tcl 60 20 10 100
# awk -v NN=60 -v NF=20 -v SPEED=10 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newspeed.txt
# echo "" >> newspeed.txt
# ns wireless_mobile.tcl 60 20 15 100
# awk -v NN=60 -v NF=20 -v SPEED=15 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newspeed.txt
# echo "" >> newspeed.txt
# ns wireless_mobile.tcl 60 20 20 100
# awk -v NN=60 -v NF=20 -v SPEED=20 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newspeed.txt
# echo "" >> newspeed.txt
# ns wireless_mobile.tcl 60 20 25 100
# awk -v NN=60 -v NF=20 -v SPEED=25 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr >> newspeed.txt

# #vary packet per second
# ns wireless_mobile.tcl 60 20 5 100
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=100 -f parse_mobile.awk trace.tr > newpacket.txt
# echo "" >> newpacket.txt
# ns wireless_mobile.tcl 60 20 5 200
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=200 -f parse_mobile.awk trace.tr >> newpacket.txt
# echo "" >> newpacket.txt
# ns wireless_mobile.tcl 60 20 5 300
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=300 -f parse_mobile.awk trace.tr >> newpacket.txt
# echo "" >> newpacket.txt
# ns wireless_mobile.tcl 60 20 5 400
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=400 -f parse_mobile.awk trace.tr >> newpacket.txt
# echo "" >> newpacket.txt
# ns wireless_mobile.tcl 60 20 5 500
# awk -v NN=60 -v NF=20 -v SPEED=5 -v PACKET_PER_SECOND=500 -f parse_mobile.awk trace.tr >> newpacket.txt

python3 graph.py > new_wireless_static_summary.txt

