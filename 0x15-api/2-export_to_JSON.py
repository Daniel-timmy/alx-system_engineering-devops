#!/usr/bin/python3
"""REST API for employees todos"""
import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + employeeId

    response = requests.get(url=url)
    response_t = requests.get(url=url_todo)

    t_response = response_t.json()
    b_response = response.json()

    dictionary = {employeeId: []}
    for item in t_response:
        dictionary[employeeId].append({"task": item["title"], "completed": item["completed"], "username": b_response["username"]})
    with open('{}.json'.format(employeeId), 'w') as file:
        json.dump(dictionary, file)
