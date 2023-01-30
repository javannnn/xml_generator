import xml.etree.ElementTree as ET

def generate_xml(invoice_data):
    root = ET.Element("Invoice")

    customer = ET.SubElement(root, "Customer")
    customer_name = ET.SubElement(customer, "CustomerName").text = invoice_data["customer_name"]
    customer_code = ET.SubElement(customer, "CustomerCode").text = invoice_data["customer_code"]

    items = ET.SubElement(root, "Items")
    for item in invoice_data["items"]:
        item_element = ET.SubElement(items, "Item")
        item_code = ET.SubElement(item_element, "ItemCode").text = item["item_code"]
        item_name = ET.SubElement(item_element, "ItemName").text = item["item_name"]
        item_quantity = ET.SubElement(item_element, "ItemQuantity").text = str(item["item_quantity"])
        item_price = ET.SubElement(item_element, "ItemPrice").text = str(item["item_price"])
        item_total = ET.SubElement(item_element, "ItemTotal").text = str(item["item_total"])

    total = ET.SubElement(root, "Total").text = str(invoice_data["total"])
    date = ET.SubElement(root, "Date").text = invoice_data["date"]

    return ET.tostring(root, encoding="unicode")

# Example usage
invoice_data = {
    "customer_name": "John Doe",
    "customer_code": "JD1234",
    "items": [
        {
            "item_code": "I0001",
            "item_name": "item1",
            "item_quantity": 10,
            "item_price": 100,
            "item_total": 1000
        },
        {
            "item_code": "I0002",
            "item_name": "item2",
            "item_quantity": 5,
            "item_price": 200,
            "item_total": 1000
        }
    ],
    "total": 2000,
    "date": "2023-01-27"
}

xml = generate_xml(invoice_data)
print(xml)
