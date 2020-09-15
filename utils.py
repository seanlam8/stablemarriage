import sys
import os 

def manipulate(file):
    with open(file, 'r') as f:
        data = f.readlines()
    preferences = [line.replace("Â", " ").strip().split() for line in data]
    people = preferences.pop(0)
    dic = {}
    for i in range(len(people)):
        dic[people[i]] = i
    for i in range(len(preferences)):
        for j in range(len(preferences[i])):
            preferences[i][j] = dic.get(preferences[i][j])
    return preferences, people
