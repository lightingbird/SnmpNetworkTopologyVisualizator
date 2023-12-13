# 定义MIB的OID(object indentifier)和部分常量
# TABLE ROW DEFINITIONS
sysName_named_oid = [('SNMPv2-MIB', 'sysName', 0)]

# 接口描述
interfaces_table_named_oid = [
    ('IF-MIB', 'ifDescr'),
    ('IF-MIB', 'ifType'),
    ('IF-MIB', 'ifMtu'),
    ('IF-MIB', 'ifSpeed'),
    ('IF-MIB', 'ifPhysAddress'),
    ('IF-MIB', 'ifAdminStatus'),
    ('IF-MIB', 'ifOperStatus'),
    ('IF-MIB', 'ifHCInOctets'),
    ('IF-MIB', 'ifHCOutOctets'),
    ('IF-MIB', 'ifHighSpeed')
]

# LLDP信息描述：设备名，设备描述，设备ID，端口描述
lldp_table_named_oid = [
    ('LLDP-MIB', 'lldpRemSysName'),
    ('LLDP-MIB', 'lldpRemSysDesc'),
    ('LLDP-MIB', 'lldpRemPortId'),
    ('LLDP-MIB', 'lldpRemPortDesc')
]

# 获取本地端口
lldp_local_port_name = [('LLDP-MIB', 'lldpLocPortId', 0)]

#######
#STATS  traffic counter readings to hold
#######
MAX_STATS_RECORDS = 2016

#########################################################
# REGULAR EXPLRESSIONS(正则表达式) FOR MATCHING PORT NAMES TO SPEEDS
# NOTE: This is used in visuzation later to color lines
# 匹配端口名称，并分配速率
#########################################################
LINK_SPEEDS = [("^TwentyGigE*", "20"),
               ("^FortyGig*", "40"),
               ("^Ten-GigabitEthernet*", "10"),
               ("^GigabitEthernet*", "1")]

#########################################################
# REGULAR EXPLRESSIONS FOR MATCHING DEVICES HIERARHY(层次结构视图)
# E.g. Access(接入) layer switches have "AC" in their name
# or aggregation(聚合) layer devices have "AG" in their names
# 用于匹配：五个字母开头的后面跟L2的名称，层级，图标
#########################################################
NODE_HIERARCHY = [
                  ('^[a-zA-Z]{5}L2.*', "4", "L2.png"),
                  ('^[a-zA-Z]{5}L3.*', "5", "L3.png"),
                  ('^[a-zA-Z]{5}DS.*', "3", "DS.png"),
                  ('^[a-zA-Z]{5}AC.*', "2", "AC.png")
                  ]

# 忽略的接口类型
IGNORED_IFTYPES = [ "l3ipvlan", "softwareLoopback", "other"]