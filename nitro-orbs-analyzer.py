def calculate_nitro_days(orbs_amount):
    days_per_nitro = 3
    orbs_per_nitro = 1400

    num_nitro_purchases = orbs_amount // orbs_per_nitro

    total_nitro_days = num_nitro_purchases * days_per_nitro

    return total_nitro_days

if __name__ == "__main__":
    while True:
        while True:
            user_orbs_str = input("enter amount of orbs u have: ")
            if not user_orbs_str.isdigit():
                print("try again idk what happened lmao")
                continue
            user_orbs = int(user_orbs_str)
            
            if user_orbs < 0:
                print("why did u put a negative number")
            else:
                days = calculate_nitro_days(user_orbs)
                print(f"with {user_orbs} orbs, you will have approximately {days} days of nitro")
                break
