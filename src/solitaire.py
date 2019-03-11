# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List


class Solitaire():
    def __init__(self,
                 key: List[int] = [0, 1, 2, 3],
                 a_pos: int = -2,
                 b_pos: int = -1,
                 сardinality: int = 4):
        self.key = deepcopy(key)
        self.a_pos = a_pos if a_pos != -2 else len(self.key) - 2
        self.b_pos = b_pos if b_pos != -1 else len(self.key) - 1
        self.cardinality = сardinality

    def __obj_to_pos(self,
                     state: List,
                     idx: int):
        if (idx >= len(state)) or (idx < -len(state)):
            print('Exception __obj_to_pos')
            return None

        if (idx == self.a_pos) or (idx == self.b_pos):
            return len(state) - 1

        return state[idx] + 1

    def __swap(self,
               state: List,
               idx_left: int,
               idx_right: int):
        if idx_right <= idx_left:
            print('Exception __swap')
            return None
        if idx_right >= len(state):
            print('Exception __swap')
            return None
        if idx_left < 0:
            print('Exception __swap')
            return None

        if self.a_pos == idx_left:
            self.a_pos += 1
        elif self.a_pos == idx_right:
            self.a_pos -= 1

        if self.b_pos == idx_left:
            self.b_pos += 1
        elif self.b_pos == idx_right:
            self.b_pos -= 1

        res = deepcopy(state)
        res[idx_left], res[idx_right] = res[idx_right], res[idx_left]

        return res

    def __tail_to_head(self,
                       state: List):
        new_state = []
        new_state.append(state[0])
        new_state.append(state[-1])
        new_state.extend(state[1:-1])

        if len(new_state) != len(state):
            print('Exception __tail_to_head')
            return None

        if self.a_pos == len(state) - 1:
            self.a_pos = 1
            if self.b_pos != 0:
                self.b_pos += 1

        elif self.b_pos == len(state) - 1:
            self.b_pos = 1
            if self.a_pos != 0:
                self.a_pos += 1

        else:
            if self.b_pos != 0:
                self.b_pos += 1
            if self.a_pos != 0:
                self.a_pos += 1

        return new_state

    def __tail_to_head_new(self,
                           state: List):
        new_state = []
        new_state.append(state[-1])
        new_state.extend(state[:-1])

        if len(new_state) != len(state):
            print('Exception __tail_to_head')
            return None

        if self.a_pos == len(state) - 1:
            self.a_pos = 0
            self.b_pos += 1

        elif self.b_pos == len(state) - 1:
            self.b_pos = 0
            self.a_pos += 1

        else:
            self.b_pos += 1
            self.a_pos += 1

        return new_state

    def func1(self,
              state: List):
        cur_state = deepcopy(state)

        if self.a_pos == len(cur_state) - 1:
            return self.__tail_to_head(cur_state)

        return self.__swap(cur_state,
                           self.a_pos,
                           self.a_pos + 1)

    def func1_new(self,
                  state: List):
        cur_state = deepcopy(state)

        if self.a_pos == len(cur_state) - 1:
            return self.__tail_to_head_new(cur_state)

        return self.__swap(cur_state,
                           self.a_pos,
                           self.a_pos + 1)

    def func2(self,
              state: List):
        cur_state = deepcopy(state)

        if self.b_pos == len(cur_state) - 1:
            tmp_state = self.__tail_to_head(cur_state)
            return self.__swap(tmp_state,
                               self.b_pos,
                               self.b_pos + 1)

        elif self.b_pos == len(cur_state) - 2:
            tmp_state = self.__swap(cur_state,
                                    self.b_pos,
                                    self.b_pos + 1)
            return self.__tail_to_head(tmp_state)

        else:
            tmp_state = self.__swap(cur_state,
                                    self.b_pos,
                                    self.b_pos + 1)
            return self.__swap(tmp_state,
                               self.b_pos,
                               self.b_pos + 1)

    def func2_new(self,
                  state: List):
        cur_state = deepcopy(state)

        if self.b_pos == len(cur_state) - 1:
            return self.__tail_to_head_new(cur_state)

        elif self.b_pos == len(cur_state) - 2:
            tmp_state = self.__swap(cur_state,
                                    self.b_pos,
                                    self.b_pos + 1)
            return self.__tail_to_head(tmp_state)

        else:
            tmp_state = self.__swap(cur_state,
                                    self.b_pos,
                                    self.b_pos + 1)
            return self.__swap(tmp_state,
                               self.b_pos,
                               self.b_pos + 1)

    def func3(self,
              state: List):
        cur_state = deepcopy(state)
        new_state = []

        if self.a_pos < self.b_pos:
            new_state.extend(cur_state[self.b_pos + 1:])
            a_pos = len(new_state)
            new_state.extend(cur_state[self.a_pos:self.b_pos])
            b_pos = len(new_state)
            new_state.append(cur_state[self.b_pos])
            new_state.extend(cur_state[:self.a_pos])
            self.a_pos = a_pos
            self.b_pos = b_pos

        elif self.b_pos < self.a_pos:
            new_state.extend(cur_state[self.a_pos + 1:])
            b_pos = len(new_state)
            new_state.extend(cur_state[self.b_pos:self.a_pos])
            a_pos = len(new_state)
            new_state.append(cur_state[self.a_pos])
            new_state.extend(cur_state[:self.b_pos])
            self.a_pos = a_pos
            self.b_pos = b_pos

        else:
            print('Exception func3')
            return None

        if len(new_state) != len(cur_state):
            print('Exception func3')
            return None

        return new_state

    def func4(self,
              state: List):
        cur_state = deepcopy(state)

        if ((self.a_pos == len(cur_state) - 1) or
                (self.b_pos == len(cur_state) - 1)):
            return cur_state

        new_state = []
        pos = self.__obj_to_pos(cur_state, -1)
        new_state.extend(cur_state[pos:-1])
        new_state.extend(cur_state[:pos])
        new_state.append(cur_state[-1])

        self.a_pos = abs(pos - self.a_pos)
        self.b_pos = abs(pos - self.b_pos)

        if len(new_state) != len(cur_state):
            print('Exception func4')
            return None

        return new_state

    def make_gamma(self,
                   state: List):
        cur_state = deepcopy(state)

        pos = self.__obj_to_pos(cur_state, 0)
        if (pos == self.a_pos) or (pos == self.b_pos):
            return 'joker'
        else:
            return self.__obj_to_pos(cur_state, pos) % self.cardinality
