def show_messages(list):
    for message in list:
        print(message)

def send_messages(messages):
    sent_messages = []

    for message in messages:
        sent_messages.append(message)
    messages.clear()
    return sent_messages
    
messages = ["Hello There", "What's up", "See you later"]

show_messages(messages)
sent = send_messages(messages[:])
print(f'Sent messages: {sent}')
print(f'Original messages: {messages}')