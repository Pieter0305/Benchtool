import numpy as np
import time
import json
import psycopg2
import os



from numpy.lib.function_base import append


dbconn = psycopg2.connect(dbname='postgres', user='postgres', password='admin')
dbc = dbconn.cursor()
name=[]
stream1 = os.popen('wmic cpu get name')
name = stream1.readlines()
cores=[]
stream2 = os.popen('wmic cpu get NumberOfCores')
cores = stream2.readlines()
stream3 = os.popen('echo %PROCESSOR_ARCHITECTURE%')
arc = stream3.read()
width=[]
stream4 = os.popen('wmic cpu get datawidth')
width = stream4.readlines()

print('Processor Name: ', name[2].strip())
print('Number of cores:', cores[2].strip())
print('Processor width:', width[2].strip()) 
print('Processor architecture:', arc)
username = input("Please Enter Username:")
devicename = input("Please Enter Device name:")

numpyconfig = np.__config__.show()


print('Waiting 20 seconds')
time.sleep(20)

Initial = 1
Step = 5
Size = 500
count = 0

label = []
fdic = []
i64dic = []
i32dic = []
i16dic = []

print('Running test for Float64')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.float64)
    m2 = np.random.rand(i,i).astype(np.float64)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    fdic.append(timedif)
    label.append(i)

print('Running test for Int64')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.int64)
    m2 = np.random.rand(i,i).astype(np.int64)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    i64dic.append(timedif)

print('Running test for Int32')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.int32)
    m2 = np.random.rand(i,i).astype(np.int32)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    i32dic.append(timedif)

print('Running test for Int16')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.int16)
    m2 = np.random.rand(i,i).astype(np.int16)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    i16dic.append(timedif)

jsonf64 = json.dumps(fdic)
jsoni64 = json.dumps(i64dic)
jsoni32 = json.dumps(i32dic)
jsoni16 = json.dumps(i16dic)
jsonlabel = json.dumps(label)

print('Uploading test results to database')

dbc.execute('INSERT INTO "Benchmark_Tool_userdata" (username, device, float64, int16, int32, int64, label) VALUES (%s,%s,%s,%s,%s,%s,%s)', 
    (username, devicename, jsonf64, jsoni16, jsoni32, jsoni64, jsonlabel))
dbconn.commit()
dbc.close()
dbconn.close()

"""Print debugs
print(fdic[1]*1000)
print(i64dic[1]*1000)
print(i32dic[1]*1000)
print(i16dic[1]*1000)

print(json_float64)
print(label)

with open("float64.json", "w") as outfile:
    json.dump(fdic, outfile)

with open("int64.json", "w") as outfile:
    json.dump(i64dic, outfile)

with open("int32.json", "w") as outfile:
    json.dump(i32dic, outfile)

with open("int16.json", "w") as outfile:
    json.dump(i16dic, outfile)
"""

