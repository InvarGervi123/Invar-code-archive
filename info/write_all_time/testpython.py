import xml.etree.ElementTree as ET

def read_user_names_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()  
    
    for user in root.findall('user'):
        name = user.find('name').text
        credit_card = user.find('cardnumber').text
        
        print("user name", name)
        print("card user", credit_card)
        print("-----------")

if __name__ == "__main__":
    read_user_names_from_xml("test.xml")
