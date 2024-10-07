def reverse_dic(dic):
	r_dic={}

	for key, value in dic.items():
		r_dic[value]=key
	return r_dic

A={'a':1, 'b':2, 'c':3, 'd':5, 'e':5, 'f':6, 'g':7}

B=reverse_dic(A)
print(B)

