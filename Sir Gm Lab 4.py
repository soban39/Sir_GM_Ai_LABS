#q1 implementation of stack
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isempty():
            return None
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isempty(self):
        return len(self.items) == 0

    def peek(self):
        if self.isempty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


st = Stack()
print("Is stack empty?", st.isempty()) 
st.push("name : soban")
st.push("age : 21")
st.push(5339)
st.push("IT Professional")
print("Is stack empty?", st.isempty()) 
print("Size of stack is:", st.size())
print("Peek of stack is:", st.peek())
print("Stack is:", st)
print("Popped : ",st.pop())
print("Popped : ",st.pop())

print("Peek of stack is:", st.peek())
print("Stack is:", st)

print("------------------------------------------------------------------------------------------------")

#q2 implementation of queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
print("Is queue empty?", q.is_empty()) 

q.enqueue("soban")
q.enqueue("age : 21")
q.enqueue(5339)
q.enqueue("IT Professional")

print("Is queue empty?", q.is_empty()) 
print("Size of queue is:", q.size())
print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("Dequeued : ",q.dequeue())
print("Dequeued : ",q.dequeue())

print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("---------------------------------------------------------------------------------------------")
#q3 binary search
#iterative method
def find(start, end, val, list):
    while start <= end:
        mid = (start + end) // 2
        if val == list[mid]:
            return mid
        elif val > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.")

#recursive method
""" def find(start, end, val, list):
    if start > end:
        return -1
    mid = (start + end) // 2
    if val == list[mid]:
        return mid
    elif val > list[mid]:
        return find(mid + 1, end, val, list)
    else:
        return find(start, mid - 1, val, list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.") """
