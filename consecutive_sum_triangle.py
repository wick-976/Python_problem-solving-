def get_cons_sum(int_list):
    end_index=len(int_list) -1
    con_sum_list=[]
    for index in range(end_index):
        con_sum=int_list[index] + int_list[index + 1]
        con_sum_list.append(con_sum)
    
    return con_sum_list

def print_cons_sum_triangle(int_list):
    while len(int_list) >1:
        new_list=get_cons_sum(int_list)
        print(new_list)
        int_list=new_list
        

def convert_str_to_int(str_num_list):
    num_list=[]
    for item in str_num_list:
        num=int(item)
        num_list.append(num)
    return num_list

str_num_list=input().split(',')
int_list=convert_str_to_int(str_num_list)
print(int_list)
print_cons_sum_triangle(int_list)