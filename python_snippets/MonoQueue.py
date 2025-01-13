"""mono deque implementation
"""
from collections import deque

class MonoQueue:
    # default is min queue, the key is to use the first element (if not outdated)
    def __init__(self,key=lambda x:x):
        self.deque=deque()
        self.key=key

    def empty(self):
        return len(self.deque)==0

    def front(self):
        return self.deque[0]
    
    def end(self):
        return self.deque[-1]
    
    def pop_front(self,key=lambda x:False) -> None:
        """ Remove out-dated element in top based on key
        """
        while not self.empty() and key(self.front()):
            self.deque.popleft()
    
    def pop_end(self, key=lambda x:False) -> None:
        """ Helper function maintaining sorted order of queue
        """
        while not self.empty() and key(self.end()):
            self.deque.pop()

    def push(self,ele):
        self.pop_end(key=lambda x:self.key(x)>self.key(ele))
        self.deque.append(ele)

    def __str__(self):
        return self.deque.__str__()
            
  
# Example driver code
if __name__ == "__main__":
    mono=MonoQueue()
    ele=[1,2,3,4,2,6,7,2]
    for i in ele:
        mono.push(i)
        print(f'Mono deque after inserting {i}:{mono}')

    print('Max deque test')
    
    mono=MonoQueue(key=lambda x:-x)
    ele=[1,2,3,4,2,6,7,2]
    for i in ele:
        mono.push(i)
        print(f'Mono deque after inserting {i}:{mono}')
