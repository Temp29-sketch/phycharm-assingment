




import math

def calculate_kinematic_equations():
    print("Kinematic Equations")
    print("1. Distance = Velocity x Time")
    print("2. Velocity = Distance / Time")
    print("3. Time = Distance / Velocity")

    choice = int(input("Enter formula (1/2/3): "))

    if choice == 1:
        velocity = float(input("Enter velocity (m/s): "))
        time = float(input("Enter time (s): "))
        distance = velocity * time
        print(f"Distance = {distance} meters")

    elif choice == 2:
        distance = float(input("Enter distance (m): "))
        time = float(input("Enter time (s): "))
        velocity = distance / time
        print(f"Velocity = {velocity} m/s")

    elif choice == 3:
        distance = float(input("Enter distance (m): "))
        velocity = float(input("Enter velocity (m/s): "))
        time = distance / velocity
        print(f"Time = {time} seconds")

def calculate_force():
    print("Force Calculator")
    print("1. F = m x a")
    print("2. F = (m x Δv) / Δt")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        force = mass * acceleration
        print(f"Force = {force} Newtons")

    elif choice == 2:
        mass = float(input("Enter mass (kg): "))
        delta_velocity = float(input("Enter change in velocity (m/s): "))
        delta_time = float(input("Enter change in time (s): "))
        force = (mass * delta_velocity) / delta_time
        print(f"Force = {force} Newtons")

def calculate_energy():
    print("Energy Calculator")
    print("1. Kinetic Energy = 0.5 x m x v^2")
    print("2. Potential Energy = m x g x h")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        kinetic_energy = 0.5 * mass * (velocity ** 2)
        print(f"Kinetic Energy = {kinetic_energy} Joules")

    elif choice == 2:
        mass = float(input("Enter mass (kg): "))
        height = float(input("Enter height (m): "))
        gravitational_acceleration = 9.81  # m/s^2
        potential_energy = mass * gravitational_acceleration * height
        print(f"Potential Energy = {potential_energy} Joules")

def main():
    while True:
        print("Physics Calculator")
        print("1. Kinematic Equations")
        print("2. Force Calculator")
        print("3. Energy Calculator")
        print("4. Quit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            calculate_kinematic_equations()
        elif choice == 2:
            calculate_force()
        elif choice == 3:
            calculate_energy()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

