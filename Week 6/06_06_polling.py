taken_poll= {'jen' : 'python', 'sarah' : 'c', 'jake' : 'rust', 'liam' : 'python'}

taking_poll = { 'liam' : 'python',  'markus' : 'c++', 'edward' : 'rust', 'jarred' : 'java'}

for name in taking_poll:
    if taken_poll.get(name):
        print(f'Sorry {name.title()}, you have already responded to this poll.')
    else:
        print(f'Hello {name.title()}! Please take this poll.')