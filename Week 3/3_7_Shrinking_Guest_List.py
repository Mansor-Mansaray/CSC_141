invites = ['Fatima', 'Josalyn', 'Bryan', 'Nicki', 'Rhea']

message0 = f"You're just in time for dinner {invites[0]}, Welcome."
message1 = f"You're just in time for dinner {invites[1]}, Welcome."
message2 = f"You're just in time for dinner {invites[2]}, Welcome."
message3 = f"You're just in time for dinner {invites[3]}, Welcome."
message4 = f"You're just in time for dinner {invites[4]}, Welcome."

print(message0)
print(message1)
print(message2)
print(message3)
print(message4)

message11 = f"Sorry but I won't be able to make it to dinner tonight. \n{invites[1]}"
print(message11)

NewInvites = ['Fatima', 'Jackie', 'Nicki', 'Rhea']

message5 = f"You're just in time for dinner {NewInvites[0]}, Welcome."
message6 = f"You're just in time for dinner {NewInvites[1]}, Welcome."
message7 = f"You're just in time for dinner {NewInvites[2]}, Welcome."
message8 = f"You're just in time for dinner {NewInvites[3]}, Welcome."


print(message5)
print(message6)
print(message7)
print(message8)


message000 = "I found a new venue with a bigger table"
print(message000)

NewInvites.append('Kobe')
NewInvites.insert(0,'Keanu')
NewInvites.insert(4, 'Edgar')

print(NewInvites)

message007 = "Sorry everyone the new table won't be availabe for dinner.\nOnly 2 people can come."
print(message007)

Uninvited = NewInvites.pop(0)
FirstUninvited = NewInvites.pop(1)
SeccondUninvited = NewInvites.pop(2)
ThirdUninvited = NewInvites.pop(3)
ForthUninvited = NewInvites.pop(2)

print(Uninvited)
print(FirstUninvited)
print(SeccondUninvited)
print(ThirdUninvited)
print(ForthUninvited)

print(f"Sorry {Uninvited.title()} you were uninvited.")
print(f"Sorry {FirstUninvited.title()} you were uninvited.")
print(f"Sorry {SeccondUninvited.title()} you were uninvited.")
print(f"Sorry {ThirdUninvited.title()} you were uninvited.")
print(f"Sorry {ForthUninvited.title()} you were uninvited.")

message777 = "Hey Fatima and Nicki, You guys are still invited to dinner."
print(message777)
NewInvites.remove('Nicki')
print(NewInvites)
NewInvites.remove('Fatima')
print(NewInvites)