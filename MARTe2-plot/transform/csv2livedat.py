#!/usr/bin/env python3
#
# Quick prototype of driving live updating gnuplot.
#
# Lots of hard coded assumptions until the requirements for a stable tool are assessed.
#
import os
import pdb
import subprocess
import sys
import time

class DemosSigtools:
	def __init__(self, data_dir="/var/tmp", live_tmp = "tmp.dat"):
		self.data_dir = data_dir
		self.live_tmp = os.path.join(self.data_dir, live_tmp)
	def tail(self, target_file="Visualisation-1-signals.csv", n_lines = 1000):
		'''Repeatedly extract the last n_lines to a temporary file'''
		self.target_file = os.path.join(self.data_dir, target_file)
		get_cmd = ["tail", "-%d" % n_lines, "%s" % self.target_file]
		proc = subprocess.Popen(get_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderr = proc.communicate()
		print("Command %s returned " % ' '.join(get_cmd))
		if not stdout:
			return 0
		else:
			tmp_file = os.path.join(self.data_dir, "tmp.prep")
			with open(tmp_file, 'w') as fh:
				fh.writelines(stdout.decode('utf=8'))
			os.rename(tmp_file, self.live_tmp)
			print("File renamed")

def main(n_lines, n_iterations, delay_seconds = 1):
	dst = DemosSigtools()
	if n_iterations == 0:
		dst.tail(n_lines = n_lines)
		return
	elif n_iterations > 0:
		while n_iterations > 0:
			print("another it %s" % n_iterations)
			dst.tail(n_lines = n_lines)		
			time.sleep(delay_seconds)
			n_iterations-=1
		return
	else:
		while True:
			print("ininfinite")
			time.sleep(delay_seconds)
			dst.tail(n_lines = n_lines)
	pass	
		
if __name__ == '__main__':
	n_lines = 1000
	n_iterations = 10
	delay_seconds = 1
	nargs = len(sys.argv) - 1
	if nargs >= 1 : n_lines = int(sys.argv[1])
	if nargs >= 2 : n_iterations = int(sys.argv[2])
	if nargs >= 3 : delay_seconds = float(sys.argv[3])
	main(n_lines, n_iterations, delay_seconds)
