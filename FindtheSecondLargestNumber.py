"""
Title     : Find the Runner-Up Score!
Subdomain : Data Types
Domain    : Python
Author    : Shubham Jirge
Created   : 14/12/23
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])
