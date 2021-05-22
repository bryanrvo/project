import xml.etree.ElementTree as ET

tree = ET.parse("VoorPeter/BeeFinity_Articles_EPLAN (12).xml")
root = tree.getroot()

for part in root.findall('part'):
    #item_dis = part.get('P_ARTICLE_NOTE')
    item_dis = part.get('P_ARTICLE_DESCR1')
    index = item_dis.find('nl_NL@')
    NL = item_dis[index - 1:]
    for eigenschapen in part.findall('freeproperty'):
        eigenschap1 = eigenschapen.get('P_ARTICLE_FREE_DATA_VALUE')
        if int(eigenschapen.get('pos')) == 1:
            index = eigenschap1.find('nl_NL@')
            EN = eigenschap1[index + 6:-1]
            print(EN)
        if int(eigenschapen.get('pos')) == 2:
            index = eigenschap1.find('nl_NL@')
            DU = eigenschap1[index + 6:-1]
            print(DU)
    #part.set('P_ARTICLE_NOTE', "de_DE@" + DU + ";en_US@" + EN + NL)
    part.set('P_ARTICLE_DESCR1', "de_DE@" + DU + ";en_US@" + EN + NL)
    
tree.write('VoorPeter/OUTPUT.xml')
    