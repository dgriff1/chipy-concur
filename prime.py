from multiprocessing import Process, Queue


def is_prime( n ):
	if n == 0 or n == 1 or n == 2: 
		return True
	for i in range(2, int(n / 2) + 1 ):
		if n % i == 0:
			return False
	return True


def calc_primes( q, num_from, num_to):
	print "Calcing from ", num_from, " to ", num_to 
	for i in range(num_from, num_to):
		if is_prime(i):
			q.put(i)


assert is_prime(0) == True
assert is_prime(1) == True
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False


q = Queue()

num_from = 0 
step = 100
procs = []
for i in range(8):
	p = Process(target=calc_primes, args=(q, num_from, num_from+step))
	p.start()
	procs.append(p)
	num_from = num_from + step

for p in procs:
	print "Joining ", p.join()

while not q.empty():
	print "Q ", q.get()
