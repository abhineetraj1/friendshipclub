import os
import shutil as sl
w = os.listdir()
w.remove("task.py")
n = 0
while(n < len(w)):
	if (len(os.listdir(w[n])) == 3):
		os.remove((w[n]+"/1").replace("x0",""))
	else:
		sl.rmtree(w[n])
	n=n+1
