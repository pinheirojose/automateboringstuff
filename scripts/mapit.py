import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', args separated by whitespace']

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address) 
