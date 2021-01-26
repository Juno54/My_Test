import datetime as dt

class User:
	def __init__(self,full_name,birthday):
		self.name=full_name
		self.birthday1=birthday
		split_name=full_name.split(' ')

		self.first_name=split_name[0]
		self.last_name=split_name[1]

	def age(self):
		today=dt.datetime.today()
		#python切片包头不包尾
		year1s=int(self.birthday1[0:4])
		month1s=int(self.birthday1[4:6])
		day1s=int(self.birthday1[6:8])

		birthday_in_day=dt.datetime(year1s,month1s,day1s)
		##这里调用的days是datetime方法的
		ages_days=(today-birthday_in_day).days
		return ages_days/365

user1=User('Alex Guo','19870122')
user2=User('Juno Xu','19901004')
print(dt.datetime.today())
#print(user1.name)
#print(user1.first_name)
#print(user1.last_name)
print("Alex Guo's age is",user1.age())
print("Juno Xu's age is",user2.age())