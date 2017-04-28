



def read_data(file_name):
    fp = open(file_name,'r')
    data = []
    for line in fp.readlines():
        data+=[line[:-1]]
    return data




def generate_wfst(data):
    start_set = set()
    all_set = set()
    state_count = 0
    start_state = 's'
    end_state = 's'
    for line in data:
        input = line.split(':')[0].strip()
        temp_output = line.split(':')[1].split('#')[0].strip()
        output_list = temp_output.split(' ')

        if len(output_list)==1:
            prob = line.split(':')[1].split('#')[1].strip()
            cur_state = start_state
            next_state = end_state
            output = output_list[0]
            temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
            start_set.add(temp_str)
        else:

            for i in range(len(output_list)):
                if i==0:
                    output = output_list[i]
                    cur_state = start_state
                    next_state = 's'+str(state_count)
                    prob = line.split(':')[1].split('#')[1].strip()
                    temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                    start_set.add(temp_str)
                    state_count+=1
                    cur_state = next_state
                    continue
                if i==len(output_list)-1:
                    next_state = 's'
                    output = output_list[i]
                    input = '*e*'
                    prob = 1
                    temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                    all_set.add(temp_str)
                    cur_state = next_state
                    continue

                output = output_list[i]
                next_state='s'+str(state_count)
                input = '*e*'
                prob = 1
                temp_str = '(' + cur_state + ' (' + next_state + ' ' + input + ' ' + output + ' ' + str(prob) + '))'
                state_count+=1
                cur_state=next_state
                all_set.add(temp_str)

    print(end_state)
    for temp in start_set:
        print(temp)
    for temp in all_set:
        print(temp)



















if __name__ == '__main__':
    file_name = 'epron-jpron.probs'
    d = read_data(file_name)
    generate_wfst(d)
