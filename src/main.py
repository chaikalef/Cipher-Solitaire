# -*- coding: utf-8 -*-
from adjacency_matrix import AdjacencyMatrix
from solitaire import Solitaire

init_state = [0, 1, 2, 3]
seq_of_application_of_func = [3, 2, 4, 1]
cipher = Solitaire()

lookup_table = {
    1: cipher.func1,
    2: cipher.func2,
    3: cipher.func3,
    4: cipher.func4,
    5: cipher.make_gamma
}
lookup_table_modified = {
    1: cipher.func1_new,
    2: cipher.func2_new,
    3: cipher.func3,
    4: cipher.func4,
    5: cipher.make_gamma
}

print('Start original method')
adjacency_matrix = AdjacencyMatrix(init_state=init_state)
exec_flag = True
cur_state = init_state
while exec_flag:
    for cnt in range(len(seq_of_application_of_func)):
        cur_func = seq_of_application_of_func[cnt]
        new_state = lookup_table[cur_func](cur_state)

        if adjacency_matrix.edge_exist(cur_state,
                                       new_state,
                                       cur_func):
            exec_flag = False
            continue
        adjacency_matrix.add_edge(cur_state,
                                  new_state,
                                  cur_func)
        cur_state = new_state

print('save_matrix')
adjacency_matrix.save_matrix()
print('save_lookup_table')
adjacency_matrix.save_lookup_table()

print('Start modified method')
adjacency_matrix = AdjacencyMatrix(init_state=init_state,
                                   flag='modified')
exec_flag = True
cur_state = init_state
while exec_flag:
    for cnt in range(len(seq_of_application_of_func)):
        cur_func = seq_of_application_of_func[cnt]
        new_state = lookup_table_modified[cur_func](cur_state)

        if adjacency_matrix.edge_exist(cur_state,
                                       new_state,
                                       cur_func):
            exec_flag = False
            continue
        adjacency_matrix.add_edge(cur_state,
                                  new_state,
                                  cur_func)
        cur_state = new_state

print('save_matrix modified')
adjacency_matrix.save_matrix()
print('save_lookup_table modified')
adjacency_matrix.save_lookup_table()
print('Finish')
