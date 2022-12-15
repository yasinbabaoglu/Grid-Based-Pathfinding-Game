# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:48:14 2022

@author: Yasin
"""

import math 

def g(cost):
    return cost + 1

def h(goal_i, goal_j, current_i, current_j):
    cost_i = current_i - goal_i
    cost_j = current_j - goal_j
    return math.sqrt((cost_i) ** 2 + abs(cost_j) ** 2)
    
def calculate_estimate(current_index, matrix_cost):
    estimate_result = []
    current_i, current_j = current_index[0], current_index[1]
    if current_j + 1 < len(matrix_cost[0]):
        if matrix_cost[current_i][current_j + 1][1] == 0:
            estimate_result.append([current_i, current_j + 1])
    if current_j - 1 > -1:
        if matrix_cost[current_i][current_j - 1][1] == 0:
            estimate_result.append([current_i, current_j - 1])
    if current_i + 1 < len(matrix_cost):
        if matrix_cost[current_i + 1][current_j][1] == 0:
            estimate_result.append([current_i + 1, current_j])
    if current_i - 1 > -1:
        if matrix_cost[current_i - 1][current_j][1] == 0:
            estimate_result.append([current_i - 1, current_j])
    return estimate_result
    
def calculate_current(current_index, min_cost):
    min_index = 0
    for i in range(len(current_index)):
        if (current_index[i][2][0] + current_index[i][2][1]) <= min_cost:
            min_cost = current_index[i][2][0] + current_index[i][2][1]
            min_index = i
    
    return min_index
 
def calculate_move_util(all_path):
    path = []
    i = 0
    while i < len(all_path):
        if len(path) > 0:
            if all_path[i][0] == path[-1][0] and abs(all_path[i][1] - path[-1][1]) == 1:
                path.append(all_path[i])
                if len(path) > 4:
                    if path[-4][0] == path[-1][0] and abs(path[-4][1] - path[-1][1]) == 1:
                        path.pop(len(path)-3)
                        path.pop(len(path)-3)
                    elif path[-4][1] == path[-1][1] and abs(path[-4][0] - path[-1][0]) == 1:
                        path.pop(len(path)-3)
                        path.pop(len(path)-3)
            elif all_path[i][1] == path[-1][1] and abs(all_path[i][0] - path[-1][0]) == 1:
                path.append(all_path[i])
                if len(path) > 4:
                    if path[-4][0] == path[-1][0] and abs(path[-4][1] - path[-1][1]) == 1:
                        path.pop(len(path)-3)
                        path.pop(len(path)-3)
                    elif path[-4][1] == path[-1][1] and abs(path[-4][0] - path[-1][0]) == 1:
                        path.pop(len(path)-3)
                        path.pop(len(path)-3)
        else:
            path.append(all_path[i])
        i += 1
    i = 0
    while i < len(path):
        if path.count(path[i]) > 1:
            path.pop(i)
        i += 1
    
    return path

def calculate_move(matrix_cost, all_path):
    all_path.reverse()
    path = []
    i = 0
    while i < len(all_path):
        if len(path) > 0:
            if all_path[i][0] == path[-1][0] and abs(all_path[i][1] - path[-1][1]) == 1:
                path.append(all_path[i])
            elif all_path[i][1] == path[-1][1] and abs(all_path[i][0] - path[-1][0]) == 1:
                path.append(all_path[i])
        else:
            path.append(all_path[i])
        i += 1

    if len(path) > 1:
        return path[-2]
    return path[-1]

def a_star_b(harita, harita_B, start_i, start_j, goal_i, goal_j, who="B"):
    matrix_cost = []
    max_cost = len(harita) ** 3
    
    for i in range(len(harita)):
        temp = []
        for j in range(len(harita[0])):
            if who == "B":
                if math.sqrt((start_i - i)**2) < 3 and math.sqrt((start_j - j)**2) < 3:
                    if harita[i][j] == "C" or harita[i][j] == " ^" or harita[i][j] == "*^" or harita[i][j] == "O^" or harita[i][j] == "O" or harita[i][j] == "B":
                        if harita_B[i][j] == 0 or not harita[i][j] == "O" :
                            harita_B.append(harita[i][j])
                        temp.append([[max_cost, max_cost], 1])
                    else:
                        temp.append([[max_cost, max_cost], 0])
                else:
                        temp.append([[0, 0], 0])                    
            elif who == "O":
                if harita[i][j] == "C" or harita[i][j] == "* " or harita[i][j] == "*^" or harita[i][j] == "*B" or harita[i][j] == "O":
                    temp.append([[max_cost, max_cost], 1])
                else:
                    temp.append([[max_cost, max_cost], 0])
        matrix_cost.append(temp)
    estimate_indexs =  []
    current_indexs =  [[start_i, start_j, [0, max_cost]]]
    matrix_cost[start_i][start_j] = [[0, h(goal_i, goal_j, current_indexs[0][0], current_indexs[0][1])], 1]
    current_index = 0
    current_coordinats = [-1, -1, [0, max_cost]]
    all_path = []    
    
    while (len(current_indexs) > 0) and (not (current_coordinats[0] == goal_i and current_coordinats[1] == goal_j)):
        current_index = calculate_current(current_indexs, max_cost)
        all_path.append([current_indexs[current_index][0], current_indexs[current_index][1]])
        current_coordinats = current_indexs[current_index]
        current_indexs.pop(current_index)
        estimate_indexs = calculate_estimate(current_coordinats, matrix_cost)
        for estimate in estimate_indexs:
            cost_g = g(current_coordinats[2][0])
            cost_h = h(goal_i, goal_j, current_coordinats[0], current_coordinats[1])
            matrix_cost[estimate[0]][estimate[1]] = [[cost_g, cost_h], 1]
            current_indexs.append([estimate[0], estimate[1], [cost_g, cost_h]])
        
    if current_coordinats[0] == goal_i and current_coordinats[1] == goal_j:
        return calculate_move(matrix_cost, all_path), harita_B
    return [-1, -1], harita_B
    
def a_star(harita, start_i, start_j, goal_i, goal_j, who="B"):
    matrix_cost = []
    max_cost = len(harita) ** 3
    for i in range(len(harita)):
        temp = []
        for j in range(len(harita[0])):
            if who == "B":
                if harita[i][j] == "C" or harita[i][j] == " ^" or harita[i][j] == "*^" or harita[i][j] == "O^" or harita[i][j] == "O" or harita[i][j] == "B":
                    temp.append([[max_cost, max_cost], 1])
                else:
                    temp.append([[max_cost, max_cost], 0])
            elif who == "O":
                if harita[i][j] == "C" or harita[i][j] == "* " or harita[i][j] == "*^" or harita[i][j] == "*B" or harita[i][j] == "O":
                    temp.append([[max_cost, max_cost], 1])
                else:
                    temp.append([[max_cost, max_cost], 0])
        matrix_cost.append(temp)
    
    estimate_indexs =  []
    current_indexs =  [[start_i, start_j, [0, max_cost]]]
    matrix_cost[start_i][start_j] = [[0, h(goal_i, goal_j, current_indexs[0][0], current_indexs[0][1])], 1]
    current_index = 0
    current_coordinats = [-1, -1, [0, max_cost]]
    all_path = []    
    
    while (len(current_indexs) > 0) and (not (current_coordinats[0] == goal_i and current_coordinats[1] == goal_j)):
        current_index = calculate_current(current_indexs, max_cost)
        all_path.append([current_indexs[current_index][0], current_indexs[current_index][1]])
        current_coordinats = current_indexs[current_index]
        current_indexs.pop(current_index)
        estimate_indexs = calculate_estimate(current_coordinats, matrix_cost)
        for estimate in estimate_indexs:
            cost_g = g(current_coordinats[2][0])
            cost_h = h(goal_i, goal_j, current_coordinats[0], current_coordinats[1])
            matrix_cost[estimate[0]][estimate[1]] = [[cost_g, cost_h], 1]
            current_indexs.append([estimate[0], estimate[1], [cost_g, cost_h]])
        
    if current_coordinats[0] == goal_i and current_coordinats[1] == goal_j:
        return calculate_move(matrix_cost, all_path)
    return -1, -1


def display1(matrix):
    print("")
    print("")
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print("")

def display2(path):
    print("")
    for i in path:
        print(i)
        
        