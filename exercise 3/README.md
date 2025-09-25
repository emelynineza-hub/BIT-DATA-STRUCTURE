**Explanation of How the Stack and Queue Questions Were Solved**

1. Stack Questions

**Practical (Irembo)**:
The stack started empty.
Actions pushed in order: "Fill Form", "Upload File", "Confirm".
After pushing these, popping once removes the last pushed item ("Confirm").
Result: The remaining stack contains ["Fill Form", "Upload File"].
This demonstrates the LIFO (Last In, First Out) nature of stacks, where the most recent item is removed first.

**Practical (UR)**:
Stack was pushed with ["Read Book", "Write Notes", "Practice"].
Undo twice means popping two items: "Practice" then "Write Notes".
Result: The only remaining item is ["Read Book"].
This again shows LIFO behavior — the last two actions are undone first.

**Challenge (Stack Trace)**:
The stack is initialized empty, and items pushed in order: ["X", "Y", "Z", "W"].
Two pop operations remove "W" first, then "Z".
Result: The stack after 2 pops is ["X", "Y"].
The algorithmic sequence was: initialize stack → push all items → pop twice → final stack trace.
This clearly follows the LIFO principle, illustrating how stack operations manage data.

**Reflection (Why Stack Supports Temporary Storage of Steps)**:
Stacks operate on LIFO, so the most recent step is accessed first.
This is ideal for undo operations, backtracking, and nested tasks, where recent actions need to be reversed.
Stacks keep data temporarily, focusing only on the latest step, simplifying the management of intermediate states.
This structure ensures controlled, step-by-step processing, essential for computing and logical workflows.

2. Queue Questions
**Practical (Nyabugogo Bus Queue):**
Initially, 7 buses queue in order: Bus 1 to Bus 7.
After 5 buses depart (dequeued), the next bus in front is Bus 6.
This shows the FIFO (First In, First Out) principle where the earliest arrivals leave first, and the queue moves forward.

**Practical (Airtel Client Queue):**
4 clients queue: Client 1 to Client 4.
After serving 1 client (dequeue), the front is Client 2.
Again, FIFO ensures fair service in the order of arrival.

**Challenge (Restaurant Food Orders Queue):**
Algorithmic sequence:
Initialize an empty queue.
When a new order arrives, enqueue it to the back.
When ready, dequeue the order from the front for serving.
Repeat as orders come and are served.
This approach maintains order fairness in serving food.
Issue with using stack: Using a stack would serve the most recent order first (LIFO), reversing order and causing unfairness as older orders would be delayed indefinitely.

**Reflection (Why FIFO Gives Fairness in Service Centers):**
FIFO serves customers in the exact order they arrive, preventing unfair priority jumps.
This system ensures equal opportunity, predictable waiting times, and transparency.
It models real-life queues (banks, call centers), where fairness and order matter.
Theoretically, FIFO eliminates bias and promotes just, systematic service management.
