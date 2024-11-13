import check_input
import small_plate
import large_plate
import turkey
import potatoes
import stuffing
import greenbeans
import pie

#unsure if these are the correct ones to import

def examine_plate(p):
    """
    display the plate's description and then based on the plate's area and
    weight capacity remaining, display a hint of how much more food the plate
    could hold and return False (suggested hints for weight: 1-6: bending,
    7-12: weak, 13+: strong. Suggested hints for area: 1-20: tiny bit, 21-40:
    some, 41+: plenty). If the plate failed, (area or weight capacity is less
    than or equal to 0), display a message for the type of failure, then return
    True.
    """
    print(p.description())

    weight = ''
    area = ''

    # check plate weight
    if 1 <= p.weight() <= 6:
        weight = "Bending"
    elif 7 <= p.weight() <= 12:
        weight = "Weak"
    else:
        weight = "Strong"

    # check plate area
    if 1 <=p.area() <= 20:
        area = "A tiny bit"
    elif 21 <= p.area() <= 40:
        area = "Some"
    else:
        area = "Plenty"

    if p.weight() <= 0 or p.area() <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge")
        return True
    else:
        print(f"Sturdiness: {weight}")
        print(f"Space available: {area}")
        return False


def main():
    """
    Present the user with a menu to choose the base plate type. Then repeatedly
    prompt the user to add a new food item to the plate, decorate the plate with
    that food item and then call examine_plate to display the hint. Aloow the
    user to add food until they decide to quit, or they spill their food on the
    floor. If they quit, diplay the contents of the final plate, number of items,
    and the space and weight remaining.
    """

    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")

    dish = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2)
    match dish:
        case 1:
            # construct small plate
            dish = small_plate.SmallPlate()
        case 2:
            dish = large_plate.LargePlate()

    while True:
        choice = check_input.get_int_range("1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n",1,6)
        match choice:
            case 1:
                # Turkey
                dish = turkey.Turkey(dish)
                if examine_plate(dish):
                    break
            case 2:
                # Stuffing
                dish = stuffing.Stuffing(dish)
                if examine_plate(dish):
                    break
            case 3:
                # Potatoes
                dish = potatoes.Potatoes(dish)
                if examine_plate(dish):
                    break
            case 4:
                # Green Beans
                dish = greenbeans.GreenBeans(dish)
                if examine_plate(dish):
                    break
            case 5:
                # Pie
                dish = pie.Pie(dish)
                if examine_plate(dish):
                    break
            case 6:
                # User Quits 
                print(dish.description())
                print(f"Good job! You made it to the table with {dish.count()} items")
                print(f"There was still {dish.area()} square inches left on your plate.")
                print(f"Your plate could have held {dish.weight()} more ounces of food.")
                print("Don't worry, you can always go back for more. Happy Thanksgiving!")
                break

main()