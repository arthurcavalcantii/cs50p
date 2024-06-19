#converter :) para 🙂 e :( para 🙁
def main():
    msg = input("")
    finalmsg = convert(msg)
    print (finalmsg)

def convert(msg):
    msg1 = msg.replace (":)", "🙂")
    msg2 = msg1.replace(":(", "🙁")
    return(msg2)
main()


    
