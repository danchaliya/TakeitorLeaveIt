"""
my_work.py
Author:  Divesh Anchaliya     <-- Put your name and project description here. Also include function descriptions in your code above each function.

"""

# Function: find_unopen
def find_unopen(opened, player_case_num):
    unopened_case = []
    i = 0
    for i in range(len(opened)):
        if i != player_case_num:
            if opened[i] == False:
                unopened_case.append(i)
    if len(unopened_case) == 1:
        indexReturn = unopened_case[0]
        return indexReturn
    else:
        return -1






# Function: game_over
def game_over(opened, player_case_num):
    total_true = 0


    for i, is_open in enumerate(opened):
        if i != player_case_num and is_open:
            total_true +=1

    if  total_true == len(opened) - 1:
        return True
    else:
        return False


# Function: get_options
def get_options(opened, player_case_num):
    options = []
    for i in range(len(opened)):
        if not opened[i] and i !=player_case_num:
            options.append(i)
    return options


# Function: largest_unchosen
def largest_unchosen(cases, opened):
   largest = 0
   for i in range(len(cases)):
       if not opened[i] and cases [i] > largest:
           largest = cases[i]
   return largest


# Function: banker_offer
def banker_offer(cases, opened):
    num_unopened = len(cases) - sum(opened)
    offer_factor = max(0.1, 1 - (1 - min(1, num_unopened / len(cases))) * 0.4)
    unopened_sum = sum(case for case, is_open in zip(cases, opened) if not is_open)
    return unopened_sum / num_unopened * offer_factor


if __name__ == '__main__':
    import take_it_leave_it

