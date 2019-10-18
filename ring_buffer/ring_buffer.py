import datetime

class RingBuffer:
  #i could do this as a touple but this is not a
  #scaleable solution to other platforms and has more overhead
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0;
    self.time = [0]*capacity; 
    self.storage = [None]*capacity;

  def append(self, item):
    if(self.current < self.capacity):
      self.time[self.current] = datetime.datetime.now();
      self.storage[self.current] = item;
      self.current += 1;
      return;
    ltime = self.time[0];
    ind = 0;
    for i in range(1,len(self.storage)):
      if ltime > self.time[i]:
        ltime = self.time[i];
        ind = i;
    self.time[ind] = datetime.datetime.now();
    self.storage[ind] = item;
    
  def get(self):
    return [ self.storage[i] for i in range(len(self.storage)) if not self.storage[i] == None]
