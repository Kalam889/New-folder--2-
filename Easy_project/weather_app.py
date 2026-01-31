# import requests
# weather_key = "518ef81dee5df3e0e5f153758573a8e8"
# while True:
#     try:
#         print("1. Enter city: ")
#         print("2. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
            
#             city = input("Enter your city: ").lower()
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
#             response = requests.get(url)
#             response.raise_for_status()

#             data = response.json()
#             print(f"\nWeather in {city.title()}:")
#             print(f"Temperature: {data['main']['temp']} C")
#             print(f"Feels Like: {data['main']['feels_like']} C")
#             print(f"Humidity: {data['main']['humidity']}%")
#             print(f"Condition: {data['weather'][0]['description'].title()}")
#             print(f"Wind Speed: {data['wind']['speed']} m/s")
#         elif choice == "2":
#             print("Exiting the program")
#             break
#         else:
#             print("Invalid input.Pleas choose given optio")
#     except requests.exceptions.ConnectionError:
#         print("⚠️ No internet connection. Please check your network and try again.")

#     except requests.exceptions.HTTPError as e:
#         if response.status_code == 404:
#             print("❌ City not found. Please check the name and try again.")
#         elif response.status_code == 401:
#             print("🔒 Invalid API key. Please verify your API key.")
#         else:
#             print(f"⚠️ HTTP Error: {e}")

# # General error (any unexpected problem)
#     except Exception as e:
#         print(f"⚠️ An unexpected error occurred: {e}")


import requests
from tkinter import *
from tkinter import messagebox
weather_key = "518ef81dee5df3e0e5f153758573a8e8"

def show_weather():
    city = entry_city.get().strip().lower()
    if city == "":
        messagebox.showwarning("Input Error", "Pleas enter a city name")
        return
    try:    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description'].title()
        wind_speed = data['wind']['speed']
        result_label.config(text=(f"City: {city.title()}\n"
                              f"Temperature: {temp}°C\n"
                              f"Feels Like: {feels_like}°C\n"
                              f"Humidity: {humidity}%\n"
                              f"Condition: {condition}\n"
                              f"Wind Speed: {wind_speed} m/s"))
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            messagebox.showerror("Error","❌ City not found. Please check the name and try again.")
        elif response.status_code == 401:
            messagebox.showerror("🔒 Invalid API key. Please verify your API key.")
        else:
            messagebox.showerror(f"⚠️ HTTP Error: {e}")

# General error (any unexpected problem)
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")    

def exit_app():
    window.destroy() 
window = Tk()
window.title("Weather App")
window.geometry("300x400")
title_label = Label(window, text="Weather App")
title_label.pack(pady=10)
city_label = Label(window, text="Enter City")
city_label.pack()
entry_city = Entry(window)
entry_city.pack(pady=10)
frame = Frame(window,bg="#cce7ff")
frame.pack(pady=10)
search_btn = Button(frame, text="Search", command=show_weather, background="lightblue")
search_btn.grid(row=0, column=0, padx=10)

exit_btn = Button(frame, text="Exit", command=exit_app, background="lightcoral")
exit_btn.grid(row=0, column=1, padx=10)


result_label = Label(window, text="")
result_label.pack(pady=50)

window.mainloop()



