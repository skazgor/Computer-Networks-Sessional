# # vary number of nodes
# ns wireless_static.tcl 20 20 300 100
# awk -v NN=20 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr > node.txt
# echo "" >> node.txt
# ns wireless_static.tcl 40 20 300 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> node.txt
# echo "" >> node.txt
# ns wireless_static.tcl 60 20 300 100
# awk -v NN=60 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> node.txt
# echo "" >> node.txt
# ns wireless_static.tcl 80 20 300 100
# awk -v NN=80 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> node.txt
# echo "" >> node.txt
# ns wireless_static.tcl 100 20 300 100
# awk -v NN=100 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> node.txt 

# # vary flow
# ns wireless_static.tcl 40 10 300 100
# awk -v NN=40 -v NF=10 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr > flow.txt
#  echo "" >> flow.txt
# ns wireless_static.tcl 40 20 300 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> flow.txt
#     echo "" >> flow.txt
# ns wireless_static.tcl 40 30 300 100
# awk -v NN=40 -v NF=30 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> flow.txt
#     echo "" >> flow.txt
# ns wireless_static.tcl 40 40 300 100
# awk -v NN=40 -v NF=40 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> flow.txt
#     echo "" >> flow.txt
# ns wireless_static.tcl 40 50 300 100
# awk -v NN=40 -v NF=50 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> flow.txt

# # vary range
# ns wireless_static.tcl 40 20 100 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=100 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr > range.txt
#   echo "" >> range.txt
# ns wireless_static.tcl 40 20 200 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=200 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> range.txt
#     echo "" >> range.txt
# ns wireless_static.tcl 40 20 300 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> range.txt
#     echo "" >> range.txt
# ns wireless_static.tcl 40 20 400 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=400 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> range.txt
#     echo "" >> range.txt
# ns wireless_static.tcl 40 20 500 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=500 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr >> range.txt

# # vary packet per second
# ns wireless_static.tcl 40 20 300 100
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=100 -f parse_static.awk trace.tr > packet.txt
#     echo "" >> packet.txt
# ns wireless_static.tcl 40 20 300 200
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=200 -f parse_static.awk trace.tr >> packet.txt
#     echo "" >> packet.txt
# ns wireless_static.tcl 40 20 300 300
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=300 -f parse_static.awk trace.tr >> packet.txt
#     echo "" >> packet.txt
# ns wireless_static.tcl 40 20 300 400
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=400 -f parse_static.awk trace.tr >> packet.txt
#     echo "" >> packet.txt
# ns wireless_static.tcl 40 20 300 500
# awk -v NN=40 -v NF=20 -v TX_RANGE=300 -v PACKET_PER_SECOND=500 -f parse_static.awk trace.tr >> packet.txt

# # plot
python3 graph.py > mac_static_summary.txt