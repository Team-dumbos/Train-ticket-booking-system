try:
	from helper_functions import *
except:
	from data.helper_functions import *


def get_page(request, root):
	if request == 'login_page':
		from data.login_page import get_login_page
		return get_login_page(root)

	if request == 'register_page':
		from data.register_page import get_register_page
		return get_register_page(root)