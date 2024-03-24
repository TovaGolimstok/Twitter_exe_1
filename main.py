# import option
# import user_choice
# from user_display import display_menu
#
#
# def main():
#     while True:
#         display_menu()
#         choice = user_choice.get_user_choice()
#
#         if choice == '1':
#             height, width = user_choice.get_parameters()
#             option.option_1_rectangle(float(height), float(width))
#         elif choice == '2':
#             height, width = user_choice.get_parameters()
#             option.option_2_triangular(float(height), float(width))
#         elif choice == '3':
#             print("Exiting the program...")
#             break
#         else:
#             print("Invalid choice. Please select 1, 2, or 3.")
#
#
# if __name__ == "__main__":
#     main()
import user_choice
from functions.rectangle import option_1_rectangle
from functions.triangular import option_2_triangular
from issues.menu import Menu
from issues.rectangle import Rectangle
from issues.triangular import Triangular
from issues.user import User


def main():
    while True:
        Menu.display()
        choice = User.get_user_choice()

        if choice == '1':
            height,width=User.get_parameters()
            # height = float(User.get_height_from_user())  # Convert to float
            # width = float(User.get_width_from_user())  # Convert to float
            rectangle = Rectangle(height, width)
            option_1_rectangle(rectangle)
        elif choice == '2':
            height,width=User.get_parameters()
            # height = float(user_choice.get_height_from_user())  # Convert to float
            # width = float(user_choice.get_width_from_user())  # Convert to float
            triangular = Triangular(height, width)
            option_2_triangular(triangular)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")



if __name__ == "__main__":
    main()