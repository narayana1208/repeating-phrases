import sys
from pprint import pprint

def suffix_array(text):
	suffix = [0]*len(text)
	for i in xrange(len(text)):
		suffix[i]  = text[i:]
	suffix.sort()
	return suffix


def longest_common_prefix(suffix):
	lcp = [0]*len(suffix)
	previous = ""
	for i in xrange(len(text)):
		count = 0
		current = suffix[i]
		max_count = min(len(current), len(previous))
		count = 0
		for j in xrange(max_count):
			if current[j] != previous[j]:
				break
			count +=1
	
		lcp[i] = count
		previous = current		
	return lcp


def leftmost(A, W):
	length = len(W)
	if W <= A[0][0:length]:
		return 0
	elif W > A[-1]:
		return len(A)-1
	else: 
		L = 0
		R = len(A)-1
		
		# print "(  L,   M,   R)"
		# print "(%3d, %3d, %3d)" % (L, (L + R)//2, R)		
		while R-L > 1:
			M = (L + R)//2
			if W <= A[M][0:length]: 
				R = M
			else: 
				L = M
			# print "(%3d, %3d, %3d)" % (L, M, R)
		return R


def rightmost(A, W):
	length = len(W)
	if W >= A[-1][0:length]:
		return len(A)-1
	elif W < A[0]:
		return 0
	else: 
		L = 0
		R = len(A)-1
		# print "(  L,   M,   R)"
		# print "(%3d, %3d, %3d)" % (L, (L + R)//2, R)		
		while R-L > 1:
			M = (L + R)//2
			if W >= A[M][0:length]: 
				L = M
			else: 
				R = M
			# print "(%3d, %3d, %3d)" % (L, M, R)
		return L


def max_value_and_index(L):
	# todo: have the return a list in case of ties
	max_value = L[0]
	max_index = 0
	i = 0
	for x in L:
		if x > max_value:
			max_value = x
			max_index = i
		i += 1
	return (max_value, max_index)


def suffix_count_of_word(suffix, W):
	if (not W):
		return 0
	return (rightmost(suffix, W) - leftmost(suffix, W)) + 1

	
def suffix_counts(suffix):
	count = [0]*len(suffix)
	for i in xrange(len(suffix)):
		count[i] = suffix_count_of_word(suffix, suffix[i][0:lcp[i]])
		# print "%10d %10d '%s'" % (count[i], lcp[i], suffix[i][0:lcp[i]])
	return count


def left_maximal(text, suffix, W1):
	c1 = suffix_count_of_word(suffix, W1)
	W2 = text[:-len(W)]
	c2 = suffix_count_of_word(suffix, W2)
	print " c2 = (%d, '%s') and c1 = (%d, '%s')  " %  (c2, W2, c1, W1)
	return c2 < c1 


def get_text():
	input_filename = 'state of the union 2011 lowercased ascii.txt'
	with open(input_filename, 'r') as f:
		text = f.read().strip()
	f.closed
	# text = "we do big things. blah blah we do big things."
	# text = "abcd xxxx abcd yyyy abcd"
	# text = "abcd abcd"	
	return text


text = get_text()

print "  text[]  (size = %10d bytes)" % sys.getsizeof(text)
# pprint(text)

import time

t0 = time.clock()
suffix = suffix_array(text)
t = (time.clock() - t0) * 10

print "suffix[]  (size = %10d bytes, exec_time = %5f)" % (sys.getsizeof(suffix), t)
# pprint(suffix)

t0 = time.clock()
lcp = longest_common_prefix(suffix)
t = (time.clock() - t0) * 10
print "   lcp[]  (size = %10d bytes, exec_time = %5f)" % (sys.getsizeof(lcp), t)
# pprint(lcp)

t0 = time.clock()
count = suffix_counts(suffix)
t = (time.clock() - t0) * 10
print " count[]  (size = %10d bytes, exec_time = %5f)" % (sys.getsizeof(count), t)
# pprint(count)
	

max_lcp, i = max_value_and_index(lcp)
phrase = suffix[i][:lcp[i]]
print "longest repeated phrase = %d X '%s' " % (count[i], phrase)


max_count, i = max_value_and_index(count)
phrase = suffix[i][:lcp[i]]
print "   most repeated phrase = %d X '%s' " % (max_count, phrase)

# print "  # lpc suffix"
# for i in xrange(len(text)):
# 	print "%3d %3d '%s'" % (count[i], lcp[i], suffix[i][:lcp[i]])

def q(s):
	return "'" + s + "'"


def wcount(text):
	"returns the number of words"
	import re
	text = re.sub('[^\w&^\d]', ' ', text)
	return len(text.split())

def print_maximal_phrases(suffix, lcp, count):
	prev = ""
	print '%s\t%s\t%s' % ("count", "numberwords", "phrase")
	for i in xrange(len(suffix)):
		w = suffix[i][:lcp[i]]
		if w.strip() == prev.strip():
			continue
		if w[:1].isalnum() or w[-1:].isalnum(): 
			continue
		
		s = suffix[i]
		left_suffix = text[-(len(s)+1):]
		j = leftmost(suffix, left_suffix)
		left_suffix = left_suffix[:lcp[j]]
		if count[j] != 0 and lcp[j] <= lcp[i]:
			print '%d\t%d\t%s' % (count[i], wcount(w), q(w))
			prev = w
		

print_maximal_phrases(suffix, lcp, count)

