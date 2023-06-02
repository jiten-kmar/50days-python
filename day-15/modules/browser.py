import webbrowser

user_input=input("Enter the search string: ").replace(" ","+")
webbrowser.open("https://www.google.com/search?q="+ user_input)

