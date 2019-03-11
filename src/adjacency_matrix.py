# -*- coding: utf-8 -*-
from copy import deepcopy
from csv import DictWriter
from math import factorial
from typing import Dict, List

from numpy import append, empty, ndarray, savetxt, zeros


class AdjacencyMatrix():
    def __init__(self,
                 matrix: ndarray = empty(3),
                 lookup_table: Dict = {},
                 init_state: List = [0, 1, 2, 3],
                 flag: str = 'original'):
        self.init_state = deepcopy(init_state)
        self.num_of_permutations = factorial(len(self.init_state))
        self.matrix = deepcopy(matrix) if matrix.shape != (3,) else zeros(
            (self.num_of_permutations, self.num_of_permutations), dtype=int)
        self.lookup_table = deepcopy(lookup_table)
        self.flag = flag

        if len(self.lookup_table) == 0:
            self.lookup_table[0] = self.init_state

    def __key_by_val(self,
                     val: List):
        for num, state in self.lookup_table.items():
            if state == val:
                return num
        return None

    def add_edge(self,
                 prev_state: List,
                 cur_state: List,
                 func: int):
        old_state = deepcopy(prev_state)
        new_state = deepcopy(cur_state)
        num_of_func = deepcopy(func)
        num_of_old = self.__key_by_val(old_state)
        num_of_new = self.__key_by_val(new_state)

        if num_of_new is None:
            num_of_new = len(self.lookup_table)
            self.lookup_table[num_of_new] = new_state
            self.matrix[num_of_old][num_of_new] = num_of_func

        else:
            if ((self.matrix[num_of_old][num_of_new] == 0) or
                    (self.matrix[num_of_old][num_of_new] == num_of_func)):
                self.matrix[num_of_old][num_of_new] = num_of_func
            else:
                with open(self.flag + '_notes.txt', 'a') as file:
                    print(f'Please, change this in future', file=file)
                    print(f'old_state: {old_state}', file=file)
                    print(f'new_state: {new_state}', file=file)
                    print(f'old func: {self.matrix[num_of_old][num_of_new]}',
                          file=file)
                    print(f'new func: {num_of_func}', file=file)
                    print(f'', file=file)

                self.matrix[num_of_old][num_of_new] = num_of_func

    def edge_exist(self,
                   prev_state: List,
                   cur_state: List,
                   func: int):
        old_state = deepcopy(prev_state)
        new_state = deepcopy(cur_state)
        num_of_func = deepcopy(func)
        num_of_old = self.__key_by_val(old_state)
        num_of_new = self.__key_by_val(new_state)

        if (num_of_old is None) or (num_of_new is None):
            return False

        if self.matrix[num_of_old][num_of_new] == num_of_func:
            return True

        return False

    def save_matrix(self):
        savetxt(self.flag + '_matrix.csv',
                self.matrix[:len(self.lookup_table), :len(self.lookup_table)],
                fmt='%d',
                delimiter=',')

    def save_lookup_table(self):
        with open(self.flag + '_lookup_table.csv', 'w') as file:
            writer = DictWriter(file, self.lookup_table.keys())
            writer.writeheader()
            writer.writerow(self.lookup_table)
