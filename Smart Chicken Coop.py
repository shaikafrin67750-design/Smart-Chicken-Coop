# Smart Chicken Coop using Python

def smart_chicken_coop(temperature, humidity, light_level):
print("\n===== SMART CHICKEN COOP =====")
print(f"Temperature : {temperature:.1f} °C")
print(f"Humidity    : {humidity:.1f} %")
print(f"Light Level : {light_level:.1f} %")

```
# Fan control
if temperature > 30:
    print("Fan: ON")
else:
    print("Fan: OFF")

# Heater control
if temperature < 18:
    print("Heater: ON")
else:
    print("Heater: OFF")

# Ventilation
if humidity > 70:
    print("Ventilation: ON")
else:
    print("Ventilation: OFF")

# Coop light
if light_level < 30:
    print("Coop Light: ON")
else:
    print("Coop Light: OFF")

print("System monitoring completed.")
```

while True:
print("\n1. Check Coop Conditions")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        light_level = float(input("Enter light level (0-100%): "))

        if (
            0 <= humidity <= 100
            and 0 <= light_level <= 100
        ):
            smart_chicken_coop(
                temperature,
                humidity,
                light_level
            )
        else:
            print("Enter valid humidity and light values.")

    except ValueError:
        print("Invalid input! Enter numbers only.")

elif choice == "2":
    print("Smart Chicken Coop System Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
