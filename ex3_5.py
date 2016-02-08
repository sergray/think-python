def do_twice(f_function):
	f_function()
	f_function()

def do_four(func_obj):
	do_twice(func_obj)
	do_twice(func_obj)

def arti_eksi():
	print '+ - - - -',

def uzun_cizgi():
	print '|        ',

def print_arti_eksi():
	do_twice(arti_eksi)
	print '+'

def print_uzun_cizgi():
	do_twice(uzun_cizgi)
	print '|'

def print_bes_satir():
	print_arti_eksi()
	do_four(print_uzun_cizgi)

def hepsini_yazdir():
	do_twice(print_bes_satir)
	print_arti_eksi()

hepsini_yazdir()

