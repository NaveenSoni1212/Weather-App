from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    api_key = "bc03fe63fe5b9d1c31712896d7e4d9cd"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        
        weather_climate_2.config(text=data["weather"][0]["main"])
        weather_Discreption_2.config(text=data["weather"][0]["description"])
        weather_Temperature_2.config(text=int(data["main"]["temp"] - 273.15)) 
        weather_pressure_2.config(text=data["main"]["pressure"])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        weather_climate_2.config(text="Error")
        weather_Discreption_2.config(text="")
        weather_Temperature_2.config(text="")
        weather_pressure_2.config(text="")
    
    except KeyError:
        print("Error: City not found or unexpected response format.")
        weather_climate_2.config(text="City not found")
        weather_Discreption_2.config(text="")
        weather_Temperature_2.config(text="")
        weather_pressure_2.config(text="")








win = Tk()

win.title("Weather App")

win.config(bg="blue")

win.geometry("500x550")

name_label = Label(win,text="Weather App" ,font=("Time New Roman",25 , "bold"))

name_label.place(x=25,y=50,height=50 , width=450)


city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather App" ,font=("Time New Roman",15),values=list_name , textvariable=city_name)

com.place(x=25,y=120,height=50 , width=450)






weather_climate = Label(win,text="Weather Climate" ,font=("Time New Roman",10))

weather_climate.place(x=25,y=260,height=50,width=200)


weather_climate_2 = Label(win,text="" ,font=("Time New Roman",10))

weather_climate_2.place(x=250,y=260,height=50,width=200)



weather_Discreption = Label(win,text="Weather Discreption" ,font=("Time New Roman",10))

weather_Discreption.place(x=25,y=330,height=50,width=200)


weather_Discreption_2 = Label(win,text="" ,font=("Time New Roman",10))

weather_Discreption_2.place(x=250,y=330,height=50,width=200)


weather_Temperature = Label(win,text="Temperature" ,font=("Time New Roman",10))

weather_Temperature.place(x=25,y=400,height=50,width=200)


weather_Temperature_2 = Label(win,text="" ,font=("Time New Roman",10))

weather_Temperature_2.place(x=250,y=400,height=50,width=200)




weather_pressure = Label(win,text="Pressure" ,font=("Time New Roman",10))

weather_pressure.place(x=25,y=470,height=50,width=200)



weather_pressure_2 = Label(win,text="" ,font=("Time New Roman",10))

weather_pressure_2.place(x=250,y=470,height=50,width=200)



done_button = Button(win,text="Done",font=("Time New Roman",10 , "bold"),command=data_get)

done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()