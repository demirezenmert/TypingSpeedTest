from time import time



def typing_tester(user_input, sample_text, start_time):
    # sample text
    
    end_time = time()
    
    sample_text = sample_text

    
    
    # get user text
    user_input = user_input

    user_speed = len(sample_text) / (end_time - start_time)

    accuracy = 0
    
    # Debug Index error
    while len(user_input) < len(sample_text):
        user_input += ' '

    if len(user_input) > len(sample_text):
        user_input = user_input[:len(sample_text)]

    for i in range(len(sample_text)):
        if sample_text[i] == user_input[i]:
            accuracy += 1

    accuracy = accuracy / len(sample_text) * 100

    print(f'Typing speed {user_speed}  characters per seconds')
    print(f'Accuracy: {accuracy}')

