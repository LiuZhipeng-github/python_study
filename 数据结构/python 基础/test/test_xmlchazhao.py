# -*- coding:utf-8 -*-
from xml.etree import ElementTree as ET
# import xml.etree.ElementTree as ET
# tree = ET.parse('parser_test.xml')
# root = tree.getroot()
pom = 'http://people.example.com'
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}


def _tag(name):
    return '{%s}%s' %(pom,name)


# for actor in root.findall('real_person:city', ns):
#     print(actor)
#     print('$'*29)
#     print('real_person:actor', '99999',ns)
#     name = actor.find('real_person:name', ns)
#     print(name.text)
#     for char in actor.findall('role:character', ns):
#         print(' |-->', char.text)

# names = tree.findall(_tag('city'))  # 这里要寻找的是根目录下的子标签
# print(_tag('city'),'ppp')
# for name in names:  # 这层是actors标签下的子标签
#     print(name.tag)
#     for i in name:  # 这层是city下的子标签
#         print(i.text)
#         print(i.attrib)
#         for n in i:  # 这是area下的标签
#             print(n.text)
tag = 'modules'


def main():
    with open('parser_test.xml',encoding='utf-8') as f:
        tree = ET.parse(f)
    if tag == 'modules':
        modules = tree.find(_tag('city'))
        if not modules:
            return []
        for i in modules:
            print(i.tag,'p')
            print(i.tag.replace('{%s}'%pom,''))
        return [module.text for module in modules]


if __name__ == '__main__':
    print(main())