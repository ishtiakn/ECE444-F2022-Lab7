# This is the Test Client.
# It sends text to the ML API and evaluates the output and latency.

import requests
import json
from time import perf_counter

ML_API_url = 'http://ece444f2022lab7-env.eba-gfthzbea.us-east-1.elasticbeanstalk.com/ML_API'

###### Test Cases ######
# [str: test_case, int: expected response]
test_cases = [["Pigs can fly", 1], 
              ["The Earth is flat", 1],
              ["Grass is real", 0],
              ["Circles are round", 0]]

###### Run Tests ######
print("\nTESTING {} ...\n".format(ML_API_url))
for test_case in test_cases:
    print("TEST CASE: ", test_case[0])
    print("EXPECTED RESPONSE: ", test_case[1])
    response = requests.post(ML_API_url, json={'exp':test_case[0],}).json()
    print("ACTUAL RESPONSE: ", response)
    
    # Measure average latency over a number of calls
    sum_latency = 0
    num_calls = 100

    for i in range(num_calls):
        start_time = perf_counter()
        #The code we are timing:
        requests.post(ML_API_url, json={'exp':test_case[0],})
        end_time = perf_counter()
        latency = end_time - start_time
        sum_latency += latency
    #Compute average latency & convert s to ms    
    avg_latency = 1000*sum_latency/num_calls
    
    print(
        "AVERAGE LATENCY OVER {num_calls} CALLS: {avg_latency:.6f}ms\n".format(
            num_calls=num_calls, avg_latency=avg_latency
        )
    )
    