import time

class HashTable:
    def __init__(self, cashe):
        #if we use cash as the number of buckets we want,
        #then we can simply create a method that puts the same
        #value into the same bucket every time, then we only have
        #to search that bucket for the value, Massively speeding up
        #the time to search. The larger the cashe the faster the search
        # but the larger the foot print is;
        self.buckets = [[] for i in range(cashe)]; #make a 2d array where 1d is the bucket, and 2 is the value

    def get_bucket(self, string):
        #we get some string and now we need to find a bucket to put it in
        h = 0; #we will use a very rutimentry hash but this should work fine
        for i in string:
            h += ord(i); #add up all the unichar values
        return h % len(self.buckets);
        #% gives us the remainder of a division call. meaning we will get
        # a number between 0 and length -1 which will be perfect for this
        # and since the same set of letters will always produce the same bucket
        # we can garrentee that we will always find our value if it exist in
        # the list
    def append(self, item):
        #so we need some string and we just add it to the bucket that fits
        ind = self.get_bucket(item); #find a bucket that fits
        self.buckets[ind].append(item); #just drop it in the bucket

    def contains(self, item):
        #so first lets find a bucket again
        ind = self.get_bucket(item);
        for i in self.buckets[ind]:
            if(i == item):
                return True;
        return False;



start_time = time.time()
hashtable = HashTable(200);
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
for n in names_1:
    hashtable.append(n);
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for n in names_2:
    if(hashtable.contains(n)):
        duplicates.append(n);
##for name_1 in names_1:
##    for name_2 in names_2:
##        if name_1 == name_2:
##            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

