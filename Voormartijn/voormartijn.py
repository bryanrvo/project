import xml.etree.ElementTree as ET

tree = ET.parse("Voormartijn/parts.xml")
root = tree.getroot()

#EB-0824-100-0

for part in root.findall('part'):
    ## PARTNR
    item_dis = part.get('P_ARTICLE_PARTNR')
    index = item_dis.find(':')
    if index != -1 and index < 6:
        voor = item_dis[:index]
        achter = item_dis[index + 1:]
        part.set('P_ARTICLE_PARTNR', voor + "." + achter)
    ## P_ARTICLE_REF_TERMINAL_NAME
    item_dis = part.get('P_ARTICLE_REF_TERMINAL_NAME')
    if item_dis != None:
        index = item_dis.find(':')
        if index != -1 and index < 6:
            voor = item_dis[:index]
            achter = item_dis[index + 1:]
            part.set('P_ARTICLE_REF_TERMINAL_NAME', voor + "." + achter)
    ## P_ARTICLE_REF_CONSTRUCTION_NAME
    item_dis = part.get('P_ARTICLE_REF_CONSTRUCTION_NAME')
    if item_dis != None:
        index = item_dis.find(':')
        if index != -1 and index < 6:
            voor = item_dis[:index]
            achter = item_dis[index + 1:]
            part.set('P_ARTICLE_REF_CONSTRUCTION_NAME', voor + "." + achter)
    ## accessoryposition
    for accessoryposition in part.findall('accessoryposition'):
        item_dis = accessoryposition.get('partnr')
        if item_dis != None:
            index = item_dis.find(':')
            if index != -1 and index < 6:
                voor = item_dis[:index]
                achter = item_dis[index + 1:]
                accessoryposition.set('partnr', voor + "." + achter)

#terminal
for terminal in root.findall('terminal'):
    item_dis = terminal.get('P_PART_TERMINAL_NAME')
    if item_dis != None:
        index = item_dis.find(':')
        if index != -1 and index < 6:
            voor = item_dis[:index]
            achter = item_dis[index + 1:]
            terminal.set('P_PART_TERMINAL_NAME', voor + "." + achter)

#accessorylist
for accessorylist in root.findall('accessorylist'):
    item_dis = accessorylist.get('P_PART_ACCESSORYLIST_NAME')
    if item_dis != None:
        index = item_dis.find(':')
        if index != -1 and index < 6:
            voor = item_dis[:index]
            achter = item_dis[index + 1:]
            accessorylist.set('P_PART_ACCESSORYLIST_NAME', voor + "." + achter)

#construction
for construction in root.findall('construction'):
    ## PARTNR
    item_dis = accessorylist.get('P_PART_CONSTRUCTION_NAME')
    if item_dis != None:
        index = item_dis.find(':')
        if index != -1 and index < 6:
            voor = item_dis[:index]
            achter = item_dis[index + 1:]
            accessorylist.set('P_PART_CONSTRUCTION_NAME', voor + "." + achter)

    
tree.write('Voormartijn/OUTPUT.xml')
    

#part P_ARTICLE_REF_TERMINAL_NAME
#terminal P_PART_TERMINAL_NAME="SE_HARMONY_FIXING UNIT_TOWER LIGHT 100"

#Part accessoryposition partnr ER AL IN
#accessorylist P_PART_ACCESSORYLIST_NAME="A-B.100-C_FS0_ACC"

#construction P_PART_CONSTRUCTION_NAME
#part P_ARTICLE_REF_CONSTRUCTION_NAME