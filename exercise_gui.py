

# # 36. #####
# import tkinter as tk

# class CounterApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title(" Count_home")

#         self.counter_value = 0

#         self.label = tk.Label(self.root, text="Counter: 0", font=("Arial", 18))
#         self.label.pack(pady=10)

#         self.increment_button = tk.Button(self.root, text="Increment", command=self.increment_counter)
#         self.increment_button.pack()

#         self.decrement_button = tk.Button(self.root, text="Decrement", command=self.decrement_counter)
#         self.decrement_button.pack()

#     def increment_counter(self):
#         self.counter_value += 1
#         self.label.config(text=f"Counter: {self.counter_value}")

#     def decrement_counter(self):
#         self.counter_value -= 1
#         self.label.config(text=f"Counter: {self.counter_value}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CounterApp(root)
#     root.mainloop()




# 37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and 

# import tkinter as tk
# from tkinter import messagebox

# class ToDoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List App")

#         self.tasks = []  # لیست وظایف

#         # Label ورودی
#         self.label = tk.Label(self.root, text="Add Task:")
#         self.label.pack(pady=10)

#         # ورودی متنی
#         self.task_entry = tk.Entry(self.root, width=30)
#         self.task_entry.pack()

#         # دکمه افزودن
#         self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
#         self.add_button.pack(pady=10)

#         # دکمه حذف
#         self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
#         self.remove_button.pack()

#         # لیست باکس برای نمایش وظایف
#         self.task_listbox = tk.Listbox(self.root, width=50)
#         self.task_listbox.pack(pady=20)

#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.tasks.append(task)
#             self.task_listbox.insert(tk.END, task)
#             self.task_entry.delete(0, tk.END)  # پاک کردن ورودی
#         else:
#             messagebox.showwarning("Warning", "Please enter a task.")

#     def remove_task(self):
#         try:
#             index = self.task_listbox.curselection()[0]
#             task = self.task_listbox.get(index)
#             self.task_listbox.delete(index)
#             self.tasks.remove(task)
#         except IndexError:
#             messagebox.showwarning("Warning", "Please select a task to remove.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ToDoApp(root)
#     root.mainloop()

### 38


# from tkinter import *
# import tkinter as tk


# class Calculator(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Calculator')
#         self.geometry('480x480+200+300')
#         self.result = tk.Entry(self, font=('Arial', 26))
#         self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=30, ipady=15, sticky=tk.W + tk.E)
#         self.result.config(justify=tk.RIGHT)

#         button_frame = tk.Frame(self)
#         button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

#         # Number buttons
#         self.create_button('1', button_frame, 0, 0, lambda: self.add_number(1))
#         self.create_button('2', button_frame, 0, 1, lambda: self.add_number(2))
#         self.create_button('3', button_frame, 0, 2, lambda: self.add_number(3))
#         self.create_button('4', button_frame, 1, 0, lambda: self.add_number(4))
#         self.create_button('5', button_frame, 1, 1, lambda: self.add_number(5))
#         self.create_button('6', button_frame, 1, 2, lambda: self.add_number(6))
#         self.create_button('7', button_frame, 2, 0, lambda: self.add_number(7))
#         self.create_button('8', button_frame, 2, 1, lambda: self.add_number(8))
#         self.create_button('9', button_frame, 2, 2, lambda: self.add_number(9))
#         self.create_button('0', button_frame, 3, 1, lambda: self.add_number(0))

#         # Operation buttons
#         self.create_button('+', button_frame, 0, 3, lambda: self.add_operation('+'))
#         self.create_button('-', button_frame, 1, 3, lambda: self.add_operation('-'))
#         self.create_button('*', button_frame, 2, 3, lambda: self.add_operation('*'))
#         self.create_button('/', button_frame, 3, 3, lambda: self.add_operation('/'))

#         # Function buttons
#         self.create_button('=', button_frame, 3, 2, lambda: self.calculate(), "green")
#         self.create_button('C', button_frame, 3, 0, lambda: self.clear(), "red")

#     def create_button(self, text, frame, row, column, command, bg="white"):
#         button = tk.Button(frame, text=text, command=command, font=('Arial', 16), width=4, height=2)
#         button.config(bg=bg)
#         button.grid(row=row, column=column, padx=10, pady=10)

#     def add_number(self, number):
#         current = self.result.get()
#         current += str(number)
#         self.result.delete(0, tk.END)
#         self.result.insert(0, current)

#     def add_operation(self, operation):
#         current = self.result.get()
#         current += operation
#         self.result.delete(0, tk.END)
#         self.result.insert(0, current)

#     def calculate(self):
#         try:
#             current = self.result.get()
#             result = eval(current)  # eval can be dangerous in real applications
#             self.result.delete(0, tk.END)
#             self.result.insert(0, result)
#         except Exception as e:
#             self.result.delete(0, tk.END)
#             self.result.insert(0, "Error")

#     def clear(self):
#         self.result.delete(0, tk.END)


# if __name__ == "__main__":
#     app = Calculator()
#     app.mainloop()

#

# 39. Create a class LoginApp that uses tkinter to create a login form GUI. 

# import tkinter as tk
# from tkinter import messagebox

# class LoginApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login App")

#         # Frame برای گروه‌بندی ورودی‌ها و دکمه
#         self.frame = tk.Frame(self.root, padx=20, pady=20)
#         self.frame.pack()

#         # برچسب ورودی نام کاربری
#         self.label_username = tk.Label(self.frame, text="Username:")
#         self.label_username.grid(row=0, column=0, sticky="w")

#         # ورودی متنی نام کاربری
#         self.entry_username = tk.Entry(self.frame, width=30)
#         self.entry_username.grid(row=0, column=1)

#         # برچسب ورودی رمز عبور
#         self.label_password = tk.Label(self.frame, text="Password:")
#         self.label_password.grid(row=1, column=0, sticky="w")

#         # ورودی متنی رمز عبور
#         self.entry_password = tk.Entry(self.frame, show="*", width=30)
#         self.entry_password.grid(row=1, column=1)

#         # دکمه ورود
#         self.login_button = tk.Button(self.root, text="Login", command=self.login)
#         self.login_button.pack(pady=10)

#     def login(self):
#         username = self.entry_username.get()
#         password = self.entry_password.get()

#         # اینجا می‌توانید اعتبارسنجی ورود را انجام دهید
#         # به عنوان مثال، اینجا یک اعتبارسنجی ساده انجام شده است
#         if username == "admin" and password == "1234":
#             messagebox.showinfo("Login Successful", "Welcome, Admin!")
#         else:
#             messagebox.showerror("Login Error", "Invalid username or password.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoginApp(root)
#     root.mainloop()




## 40. Create a class WeatherApp that uses tkinter to create a weather information GUI. 

# import tkinter as tk
# from tkinter import messagebox
# import requests

# class WeatherApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather App")

#         # Create widgets
#         self.city_entry = tk.Entry(root, width=50)
#         self.city_entry.pack()

#         self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
#         self.get_weather_button.pack()

#         self.weather_label = tk.Label(root, text="")
#         self.weather_label.pack()




#     def get_weather(self):
#         city = self.city_entry.get()
#         if city:
#             api_key = "your_api_key"  # Replace with your actual API key
#             url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#             try:
#                 response = requests.get(url)
#                 data = response.json()
#                 if data["cod"] == 200:
#                     weather = data["weather"][0]["description"]
#                     temp = data["main"]["temp"]
#                     self.weather_label.config(text=f"Weather: {weather}, Temperature: {temp}°C")
#                 else:
#                     self.weather_label.config(text="City not found.")
#             except Exception as e:
#                 messagebox.showerror("Error", "Could not retrieve weather data.")
#         else:
#             messagebox.showwarning("Warning", "You must enter a city.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WeatherApp(root)
#     root.mainloop()        