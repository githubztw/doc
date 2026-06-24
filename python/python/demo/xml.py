import xml.etree.ElementTree as ET

# 写入XML
def write_xml():
    root = ET.Element('root')
    child1 = ET.SubElement(root, 'child1')
    child1.text = 'This is child1 text.'
    child1.set('attribute', 'value')

    child2 = ET.SubElement(root, 'child2')
    child2.text = 'This is child2 text.'

    tree = ET.ElementTree(root)
    tree.write('./data/output.xml', encoding='utf-8', xml_declaration=True)


def process_element(element):
    # 处理当前元素
    print(f"Element: {element.tag}, Attributes: {element.attrib}, Text: {element.text}")
    
    # 递归处理子元素
    for child in element:
        process_element(child)

# 读取XML
def read_xml():
    tree = ET.parse('./data/output.xml')
    root = tree.getroot()
    print("Root element:", root.tag)
    process_element(root)
        
read_xml()
