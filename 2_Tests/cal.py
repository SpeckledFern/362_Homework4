#Sierra Freihoefer
#Description: Python file with various calculation functions to prefrom testing on.
#2-5-2021

def cube_volume(a, b, c):
	a_check = isinstance(a, int)
	if a_check == 0:
		return 0
	b_check = isinstance(b, int)
	if b_check == 0:
		return 0
	c_check = isinstance(c, int)
	if c_check == 0:
		return 0
	if a < 0 or b < 0 or c < 0:
		return 0
	c = a*b*c
	return c

def aver_list(a_list):
	total = 0
	for x in a_list:
		total += x
	if len(a_list) == 0:
		return 0

	c = total/len(a_list)
	return c

def make_name(first, last):
	f_check = isinstance(first, str)
	if f_check == 0:
		return 0
	l_check = isinstance(last, str)
	if l_check == 0:
		return 0
	if first == "":
		return 0
	if last == "":
		return 0
	
	full = first + " " + last
	return full
