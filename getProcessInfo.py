import psutil
import json

def getProcessList(batch, timestamp):
    listOfProcessNames = list();
    for process in psutil.process_iter():
        processInfoDictionary = process.as_dict(attrs=['pid', 'name', 'memory_percent'])
        processInfoDictionary['memory_percent'] = round(process.memory_percent(), 2)
        processInfoDictionary['batch'] = batch
        processInfoDictionary['timestamp'] = timestamp
        listOfProcessNames.append(processInfoDictionary)
    return json.dumps(listOfProcessNames);
