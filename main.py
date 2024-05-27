from time import time

def typing_tester():
    # sample text
    sample_text = 'Today is sunny!'

    # Start timer 
    start_time = time()
    # get user text
    user_input = input("Type the following text: "+ sample_text + '\n')
    end_time = time()

    user_speed = len(sample_text) / (end_time - start_time)

    accuracy = 0
    
    # Debug Index error
    while len(user_input) < len(sample_text):
        user_input += ' '

    for i in range(len(sample_text)):
        if sample_text[i] == user_input[i]:
            accuracy += 1

    accuracy = accuracy / len(sample_text) * 100

    print(f'Typing speed {user_speed}  characters per seconds')
    print(f'Accuracy: {accuracy}')

typing_tester()