

def construct_char_word(data_new):
    start_set = set()
    all_set = set()
    start_state = 'start_state'
    end_state = 'end_state'
    for i in range(len(data_new)):
        data = data_new[i]
        for j in range(len(data)):

            if j==0:
                cur_state = start_state
                next_state = data[j]
                input = data[j]
                output = '*e*'
                prob = 1
                temp_str = '('+cur_state+' ('+next_state + ' '+input+' '+output+' '+ str(prob)+'))'

                start_set.add(temp_str)
                cur_state = next_state
            else:
                if j==len(data)-1:
                    next_state = data[:j+1]
                    input = data[j]
                    output = '*e*'
                    prob = 1
                    temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                    all_set.add(temp_str)
                    cur_state = next_state

                    ######For end state
                    next_state = end_state
                    input = '*e*'
                    output = data
                    prob = 1
                    temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                    all_set.add(temp_str)

                else:
                    next_state = data[:j+1]
                    input = data[j]
                    output = '*e*'
                    prob = 1
                    temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                    all_set.add(temp_str)
                    cur_state = next_state

    print(end_state)
    for temp in start_set:
        print(temp)
    for temp in all_set:
        print(temp)










def read_file(file_name):
    data =set()
    fp=open(file_name,'r')
    for line in fp.readlines():
        data.add(line.split(' ')[0])


    return data






if __name__ == '__main__':
    file_name  = 'eword-epron.data'
    data = read_file(file_name)
    data=list(data)
    construct_char_word(data)








