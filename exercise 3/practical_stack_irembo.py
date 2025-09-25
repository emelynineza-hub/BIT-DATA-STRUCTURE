#STACK PRACTICES
irembo_stack = []
irembo_stack.append("Fill Form")
irembo_stack.append("Upload File")
irembo_stack.append("Confirm")
irembo_stack.pop()
print("This remains when pop once in IREMBO: ",irembo_stack)

UR_stack = []
UR_stack.append("Fill Form")
UR_stack.append("Upload File")
UR_stack.append("Confirm")
UR_stack.pop()
UR_stack.pop()
print("This remains when pop twice in UR: ",UR_stack)

#QUEUE PRACTICE
Nyabugogo_queue=[]
Nyabugogo_queue.append("Bus 1")
Nyabugogo_queue.append("Bus 2")
Nyabugogo_queue.append("Bus 3")
Nyabugogo_queue.append("Bus 4")
Nyabugogo_queue.append("Bus 5")
Nyabugogo_queue.append("Bus 6")
Nyabugogo_queue.append("Bus 7")
Nyabugogo_queue.pop(0)
Nyabugogo_queue.pop(0)
Nyabugogo_queue.pop(0)
Nyabugogo_queue.pop(0)
Nyabugogo_queue.pop(0)
print("After 5 buses depart,in the front remain:",Nyabugogo_queue[0])

Airtel_queue=[]
Airtel_queue.append("Client 1")
Airtel_queue.append("Client 2")
Airtel_queue.append("Client 3")
Airtel_queue.append("Client 4")
Airtel_queue.pop(0)
print("After 1 client served,in the front remain:",Airtel_queue[0])


