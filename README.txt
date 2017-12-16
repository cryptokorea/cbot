cbot : Crypto Bot


How to run
	1. login to coinone site as your account
	2. get ACCESS_TOKEN and SECRET_KEY from cointone site
		https://coinone.co.kr/account/login/?next=/developer/app/
		Generate new key ( withdraw is not needed )
	3. Add ACCESS_TOKEN and SECRET_KEY to API/my_key_info.py
		class my_info:
		    ACCESS_TOKEN = 'YOURS'
		    SECRET_KEY = 'YOURS'
	4. excute run.py 



Ref : http://doc.coinone.co.kr/
* Please check API directory from run.py
	sys.path.append("C:/Users/user/PycharmProjects/coinone/API")