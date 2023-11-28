import threading
import requests
import time


def getData(urls):
    st = time.time()  # start time in sec
    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())
    et = time.time()  # end time in sec
    elapsedTime = et - st  # difference in sec
    print("Execution time: ", elapsedTime, " seconds")
    return jsonArray


urls = ["https://postman-echo.com/delay/3"] * 5
getData(urls)
