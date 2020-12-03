from datetime import datetime, date
current = str(datetime.now())
print(current)  # 2020-12-02 20:15:12.461202
user_year = ""
current_year = ""
for i in range(4):
    user_year += "2018-10-10"[i]
    current_year += current[i]
print(user_year)  # 2018
print(current_year)  # 2020
diff = int(current_year) - int(user_year)
print(diff)  # 2
