from src.library import Library
from src.item_builder import ItemBuilder
from src.user_builder import UserBuilder
from datetime import datetime, timedelta


def scenario_jonny_codewarrior(library):
    # 0 = Jonny
    # One outstanding book, not overdue
    library.checkout_item(1, "Angels and Demons", date=datetime.now() - timedelta(days=1))
    # Check out book, "Document, Your Job depends on it"
    if library.can_checkout(1):
        library.checkout_item(1, "Document, Your job depends on it")
    else:
        print("Unable to check out item... :(")
    print('HUZZAH!!!')

def scenario_judy_hacker(library):
    """
    Judy Hacker, has fines of £2 outstanding,
    would like a DVD “Debugging to music”,
    does have a book out (not overdue) and is bringing back an overdue journal.
    """
    library.checkout_item(2, "New Moon", date=datetime.now() - timedelta(days=32))
    library.return_item(2, "New Moon")
    library.checkout_item(2, "Twilight")
    library.checkout_item(2, "Debugging to music")
    #### Adam: How does the library know she has this journal if it hasn't been previously checked out?? ####
    #### She must have stolen it. Should we have a library.call_police() method? ####
    # library.return_item(2, "Pirates of the Caribbean: The Journal")


def scenario_miss_marple(library):
    # 2 = Miss
    library.checkout_item(1, "Sleuthing in C#", date=datetime.now() - timedelta(days=8271))  # C# first appeared in 2000
    # Miss marple tries to check out journal 'Sleuthing in C#'
    if library.can_checkout(2):
        library.checkout_item(3, "Sleuthing in C#")
    else:
        print("Unable to check out item... :(")


def scenario_eric_halfbee(library):
    """
    Eric Halfbee comes in with a pile of overdue items,
    but doesn’t know if he has enough money to pay off his debts.
    If he has, he’d like a borrow a DVD.
    """
    library.checkout_item(4, "Life of Pi", date=datetime.now() - timedelta(days=40))
    library.checkout_item(4, "Labyrinth", date=datetime.now() - timedelta(days=40))
    library.checkout_item(4, "The Tales of Beedle the Bard", date=datetime.now() - timedelta(days=40))
    library.return_item(4, "Life of Pi")
    library.return_item(4, "Labyrinth")
    #### Adam: Fixed extra whitespace on this title in the txt file ####
    library.return_item(4, "The Tales of Beedle the Bard")
    fine = library.get_total_fine(4)
    print(f"Outstanding fine: £{fine:.2f}")
    library.pay_fine(4, 10)
    library.checkout_item(4, "Pirates of the Caribbean")


def build_library(library):
    item_builder = ItemBuilder()

    item_builder.set_library(library)

    ##### Adam: Needed to change the path to this slightly on my machine ####
    # item_builder.load_books_in_file("top100t.txt")
    item_builder.load_books_in_file("src/top100t.txt")
    #### Adam: Added debugging to music to the library ####
    item_builder.create_dvd("Debugging to music")
    item_builder.create_dvd("Pirates of the Caribbean")
    item_builder.create_journal("Pirates of the Caribbean: The Journal")
    item_builder.create_journal("Sleuthing in C#")

    item_builder.populate_library()


def build_users(library):
    user_builder = UserBuilder()
    user_builder.set_library(library)

    # TODO: Generate users from Enums instead of for loop
    for i in range(0, 4):
        user_builder.create_user()


if __name__ == '__main__':
    print("Welcome to Alexandria")

    lib_controller = Library(max_loans=5, max_fines=50)

    build_library(lib_controller)

    build_users(lib_controller)

    # Run scenario's
    scenario_jonny_codewarrior(lib_controller)
    scenario_judy_hacker(lib_controller)
    scenario_miss_marple(lib_controller)
    scenario_eric_halfbee(lib_controller)
