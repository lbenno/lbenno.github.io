"""
Returns a message to User when they enter certain input
"""
# From an input (command)
# return a message
# python3 github_page1.py

welcome_message = str("""Welcome to Lauren's first attempts at coding""")
command = input("Enter input here: ")


if command == 'welcome':
    print(welcome_message)
else:
    print('say what?')
