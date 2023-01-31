import requests
import threading
import time

# GET FROMTIME
print("Enter fromTime (Format: dd/mm/yyyy): ")
time_string = input()
fromTime = time.mktime(time.strptime(time_string, "%d/%m/%Y"))

# GET TOTIME
print("Enter toTime (Format: dd/mm/yyyy): ")
time_string = input()
toTime = time.mktime(time.strptime(time_string, "%d/%m/%Y"))

# GET THE NUMBER OF REQUEST
print("Enter number of requests:")
a = int(input())

def thread_func():
    # MAKING A POST REQUEST
    for i in range(10):
      r = requests.post('http://103.1.238.175:2000/api/social/dataSensor', data = {"stationID":"1012991250","fromTime":fromTime,"toTime":toTime})
      print(r)
      print(r.elapsed.total_seconds())

# CREATE SOME THREAD AND START THEM 
threads = []
for i in range(a):
  threads.append(threading.Thread(target=thread_func))
  threads[-1].start()

#WAIT FOR ALL THREAD TO COMPLETE
for thread in threads:
  thread.join()