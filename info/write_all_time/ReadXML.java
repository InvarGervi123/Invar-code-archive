import org.w3c.dom.*;
import javax.xml.parsers.*;
import java.io.File;

public class ReadXML {
    public static void main(String[] args) {
        try {
            File xmlFile = new File("users.xml");
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(xmlFile);
            doc.getDocumentElement().normalize();

            NodeList userList = doc.getElementsByTagName("משתמש");
            for (int i = 0; i < userList.getLength(); i++) {
                Node userNode = userList.item(i);

                if (userNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element userElement = (Element) userNode;
                    String name = userElement.getElementsByTagName("שם").item(0).getTextContent();
                    String creditCard = userElement.getElementsByTagName("כרטיסאשראי").item(0).getTextContent();

                    System.out.println("שם המשתמש: " + name);
                    System.out.println("מספר כרטיס אשראי: " + creditCard);
                    System.out.println("-----------");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
