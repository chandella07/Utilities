
b="""  (security login show)
vserver  user-or-group-name application authmethod role  acctlocked comment
-------- ------------------ ----------- ---------- ----- ---------- -------
cluster1 admin              console     password   admin no         -
cluster1 admin              http        password   admin no         -
cluster1 admin              ontapi      password   admin no         -
cluster1 admin              service-processor password admin no     -
cluster1 admin              ssh         password   admin no         -
5 entries were displayed.

"""

c='''vserver lif               role    data-protocol home-node   home-port curr-node   curr-port status-oper status-extended numeric-id is-home address         netmask     netmask-length auto-configuration auto subnet-name status-admin failover-policy firewall-policy auto-revert sticky dns-zone listen-for-dns-query allow-lb-migrate lb-weight failover-group wwpn address-family comment ipspace is-dns-update-enabled
------- ----------------- ------- ------------- ----------- --------- ----------- --------- ----------- --------------- ---------- ------- --------------- ----------- -------------- ------------------ ---- ----------- ------------ --------------- --------------- ----------- ------ -------- -------------------- ---------------- --------- -------------- ---- -------------- ------- ------- ---------------------
Cluster cluster1-01_clus1 cluster -             cluster1-01 e0a       cluster1-01 e0a       up          -               1024       true    169.254.151.224 255.255.0.0 16             -                  -    -           up           local-only                      true        false  none     false                false            load      Cluster        -    ipv4           -       Cluster -                    
Cluster cluster1-01_clus2 cluster -             cluster1-01 e0b       cluster1-01 e0b       up          -               1023       true    169.254.182.223 255.255.0.0 16             -                  -    -           up           local-only                      true        false  none     false                false            load      Cluster        -    ipv4           -       Cluster -                    
Cluster cluster1-02_clus1 cluster -             cluster1-02 e0a       cluster1-02 e0a       up          -               1013       true    169.254.150.235 255.255.0.0 16             -                  -    -           up           local-only                      true        false  none     false                false            load      Cluster        -    ipv4           -       Cluster -                    
Cluster cluster1-02_clus2 cluster -             cluster1-02 e0b       cluster1-02 e0b       up          -               1014       true    169.254.24.36   255.255.0.0 16             -                  -    -           up           local-only                      true        false  none     false                false            load      Cluster        -    ipv4           -       Cluster -                    
cluster1 cluster1-01_mgmt1 node-mgmt -          cluster1-01 e0c       cluster1-01 e0c       up          -               1026       true    10.237.140.82   255.255.255.0 24           -                  -    -           up           local-only      mgmt            true        false  none     false                false            load      Default        -    ipv4           -       Default -                    
cluster1 cluster1-02_mgmt1 node-mgmt -          cluster1-02 e0c       cluster1-02 e0c       up          -               1027       true    10.237.140.83   255.255.255.0 24           -                  -    -           up           local-only      mgmt            true        false  none     false                false            load      Default        -    ipv4           -       Default -                    
cluster1 cluster_mgmt     cluster-mgmt -        cluster1-01 e0c       cluster1-01 e0c       up          -               1025       true    10.237.140.81   255.255.255.0 24           -                  -    -           up           broadcast-domain-wide mgmt      false       false  none     false                false            load      Default        -    ipv4           -       Default -                    
7 entries were displayed.

'''

k='''node            utcdateandtime
--------------- ------------------------
initenasggnna1a Wed Jan 03 06:29:03 2018

'''


def get_dict_column_wise(output,col_num,start_line=0,end_line=-1):
     list1= []
     list2= []
     lines = output.splitlines()
     for line in lines[start_line:end_line]:
          column = line.split()
          if not column[col_num].startswith('--'):
               list1.append(column[col_num])
     list2.append(list1)
     dict1 = {i[0]:i[1:] for i in list2}
     print dict1
	
get_dict_column_wise(k,1,start_line=0,end_line=-1)
	




