import tkinter as tk
from functions import CardReader

class MainWindow:
    def __init__(self):
        self.card_reader = CardReader(self)
        self.questions = Questions(self.card_reader)

        self.my_w = tk.Tk()
        self.my_w.title("ST1 CAPSTONE PROJECT")
        self.my_w.configure(bg='pink')
        #self.my_w.geometry("widthxheight")

        self.my_font1 = ('times', 12, 'bold')

        self.lb1 = tk.Label(self.my_w, text='File name:\npricetest.csv', width=30, font=self.my_font1)
        self.lb1.grid(row=1, column=2)

        self.b1 = tk.Button(self.my_w, text='Expand Card Details', width=20, command=self.read_file, bg="#cc66ff",
            fg="white")
        self.b1.grid(row=2, column=2, pady=5)

        self.b2 = tk.Button(self.my_w, text='Open Questions Window', width=20, command=self.start_question_window, bg="#cc66ff",
            fg="white")
        self.b2.grid(row=3, column=2, pady=5)

        self.my_w.mainloop()

    def read_file(self): # reads file, then refreshes the treeview to reflect changes
        self.card_reader.read_file()
        self.card_reader.trv_refresh()

    def start_question_window(self):
        if self.card_reader.df is None:
            #print("making new df")
            self.card_reader.read_file()
        #else:
            #print("already got a df")
        QuestionWindow(self.questions)


class QuestionWindow:
    def __init__(self, questions):
        self.questions = questions


        self.question_window = tk.Tk()
        self.question_window.title("ST1 CAPSTONE PROJECT")
        self.question_window.configure(bg="pink")

        self.start_label1 = tk.Label(self.question_window, text="WELCOME", font="Arial", bg="pink")
        ""
        self.start_label1.grid(row=1, column=2)

        self.start_label2 = tk.Label(
            self.question_window,
            text="""
                Welcome to my program designed to analyze Magic: The Gathering cards from a comprehensive dataset.
                Magic: The Gathering (MTG) is a collectible card game that has captured the hearts and minds of millions of players worldwide since its debut in 1993.
                Developed by mathematics professor Richard Garfield and published by Wizards of the Coast,
                MTG offers a rich and immersive fantasy experience where players assume the roles of powerful wizards known as Planeswalkers,
                and engage in epic battles using spells, artifacts, and creatures represented by beautifully illustrated cards.
                My program aims to leverage this wealth of data to provide insights and facilitate a deeper understanding of MTG cards,
                analyzing key features such as mana cost, card type, rarity, and special abilities to unravel patterns, trends, and relationships within the dataset.
                \nPlease select a question below to explore the dataset\n
                """,
            font=("Arial", 10),
            bg="pink"
        )
        self.start_label2.grid(row=2, column=2)

        self.q1 = tk.Button(
            self.question_window,
            text='What is the total number of red creature cards in the dataset?',
            width=50,
            command=self.questions.question_1,
            bg="#cc66ff",
            fg="white"
        )
        self.q1.grid(row=3, column=2)

        self.q2 = tk.Button(
            self.question_window,
            text='How many instant cards in total?',
            width=50,
            command=self.questions.question_2,
            bg="#cc66ff",
            fg="white"
        )
        self.q2.grid(row=4, column=2)

        self.q3 = tk.Button(
            self.question_window,
            text='What is the highest priced card in the dataset and the lowest?',
            width=50,
            command=self.questions.question_3,
            bg="#cc66ff",
            fg="white"
        )
        self.q3.grid(row=5, column=2)

        self.q4 = tk.Button(
            self.question_window,
            text='Which creatures have the highest attack value?',
            width=50,
            command=self.questions.question_4,
            bg="#cc66ff",
            fg="white"
        )
        self.q4.grid(row=6, column=2)

        self.quit1 = tk.Button(
            self.question_window,
            text='Close',
            width=10,
            command=self.question_window.destroy,
            bg="#ff0066",
            fg="white"

        )
        self.quit1.grid(row=10, column=2)

        self.question_window.mainloop()


class Questions:
    def __init__(self, card_reader):
        self.card_reader = card_reader
# create the window to display the results
    def make_result_window(self, qnumber, text, listData=False):
        result_window = tk.Toplevel()
        result_window.title(f"ST1 CAPSTONE PROJECT Q.{qnumber}")
        result_window.configure(bg="pink")
        start_label1 = tk.Label(
            result_window,
            text=text,
            font=("Arial", 12),
            bg="pink"
        )
        start_label1.grid(row=1, column=0)

        if listData:
            listbox = tk.Listbox(
                result_window,
                font = ("Arial", 12),
                height=6,
                width=25
            )

            idx = 1
            for creature in listData:
                listbox.insert(idx, creature)
                idx += 1
            listbox.grid(row=2, column=0, columnspan=3)

        result_window.quit1 = tk.Button(
            result_window,
            text='Close',
            width=10,
            command=result_window.destroy,
            bg="#ff0066",
            fg="white"
        )
        result_window.quit1.grid(row=3, column=0)

# functions for each individual question, taking values from functions.py and sending to result_window
    def question_1(self):
        red_creature_cards = self.card_reader.calculate_red_creature_cards()
        text="Number of red creature cards: {}".format(red_creature_cards)
        self.make_result_window(1, text)


    def question_2(self):
        total_instant_cards = self.card_reader.calculate_total_instant_cards()
        text="Total number of instant cards: {}".format(total_instant_cards)
        self.make_result_window(2, text)


    def question_3(self):
        highest_priced_card, lowest_priced_card = self.card_reader.get_highest_and_lowest_priced_card()
        text="Highest priced card: {}\nLowest priced card: {}".format(highest_priced_card, lowest_priced_card)
        self.make_result_window(3,text)

    def question_4(self):
        highest_attack, creatures_with_highest_attack = self.card_reader.get_creatures_with_highest_attack()
        text = "Highest attack: {}".format(highest_attack)
        self.make_result_window(4, text, creatures_with_highest_attack)



if __name__ == "__main__":
    MainWindow()
