import requests
from xml.dom.minidom import parseString
import csv

# Array to store tag names to retrieve
retrieveTags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction']

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

try:
    page = requests.get(url)
    page.raise_for_status()
    doc = parseString(page.content)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit(1)

# Uncomment the following line to check it works, then comment it out once you know it works
#print(doc.toprettyxml()) # Output to console

# Store the XML in a file
with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

# Step 2: Print Train Codes
print("Train Codes:")
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    if traincodenode and traincodenode.firstChild:
        traincode = traincodenode.firstChild.nodeValue.strip()
        print(traincode)

# Step 3: Print Latitudes
print("\nLatitudes:")
for objTrainPositionsNode in objTrainPositionsNodes:
    latitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    if latitudenode and latitudenode.firstChild:
        latitude = latitudenode.firstChild.nodeValue.strip()
        print(latitude)

# Step 4: Store Train Codes in CSV File
with open('trains.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        if traincodenode and traincodenode.firstChild:
            traincode = traincodenode.firstChild.nodeValue.strip()
            dataList = [traincode]
            train_writer.writerow(dataList)

# Step 5: Store All Properties in CSV
with open('trains_all_properties.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            if datanode and datanode.firstChild:
                dataList.append(datanode.firstChild.nodeValue.strip())
            else:
                dataList.append("N/A")  # Add a placeholder for missing data
        train_writer.writerow(dataList)

# Step 6: Filter Trains with Code Starting with 'D' and Store in CSV
with open('trains_filtered.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        if traincodenode and traincodenode.firstChild:
            traincode = traincodenode.firstChild.nodeValue.strip()
            if traincode.startswith('D'):
                dataList = [traincode]
                train_writer.writerow(dataList)
