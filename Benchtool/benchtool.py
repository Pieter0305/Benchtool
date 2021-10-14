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

pname = name[2].strip()
core = cores[2].strip()
bits = width[2].strip()


print('Processor Name: ', pname)
print('Number of cores:', core)
print('Processor width:', bits) 
print('Processor architecture:', arc)
user = input("Please Enter Username:")
devicename = input("Please Enter Device name:")
print(type(user))
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
    fdic.append(timedif*1000)
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
    i64dic.append(timedif*1000)

print('Running test for Int32')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.int32)
    m2 = np.random.rand(i,i).astype(np.int32)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    i32dic.append(timedif*1000)

print('Running test for Int16')

for i in range(Initial,Size,Step):
    m1 = np.random.rand(i,i).astype(np.int16)
    m2 = np.random.rand(i,i).astype(np.int16)
    d= time.perf_counter()
    tNumpy = np.dot(m1, m2) 
    e = time.perf_counter()
    count = count + 1 
    timedif = e-d
    i16dic.append(timedif*1000)

jsonf64 = json.dumps(fdic)
jsoni64 = json.dumps(i64dic)
jsoni32 = json.dumps(i32dic)
jsoni16 = json.dumps(i16dic)
jsonlabel = json.dumps(label)

print('Uploading test results to database')

query = 'INSERT INTO "Benchmark_Tool_userdata" (username, device, pname, cores, width, arc, label, float64, int64, int32, int16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'


dbc.execute(query, (user, devicename, pname, core, bits, arc, jsonlabel, jsonf64, jsoni64, jsoni32, jsoni16))
dbconn.commit()
dbc.close()
dbconn.close()

