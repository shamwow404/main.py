# import modules
import pandas as pd
from tkinter import ttk


class CardReader:
    def __init__(self, main_window):
        self.df = None
        self.main_window = main_window
        self.trv = None

    def trv_refresh(self):  #Refresh the Treeview to reflect changes
        global df, trv, l1, l2

        r_set = df.to_numpy().tolist()  # create list of list using rows

        trv = ttk.Treeview(self.main_window.my_w, selectmode='browse', height=10,
                           show='headings', columns=l1)
        trv.grid(row=4, column=1, columnspan=3, padx=10, pady=20)

        for i in l1:
            trv.column(i, width=120, anchor='c')
            trv.heading(i, text=str(i))
        for dt in r_set:
            v = [r for r in dt]
            trv.insert("", 'end', iid=v[0], values=v)



    def read_file(self):
        global df, df2, l1
# Set up columns
        df = pd.read_csv(
            r"pricetest.csv",
            usecols=['cardName', 'cardCmc', 'cardType', 'creatureType', 'powTough', 'set', 'setNum',
                     'rarity', 'language', 'cardImage', 'price']
        )

        l1 = list(df)  # List of column names as header
        str1 = "Rows:" + str(df.shape[0]) + " , Columns:" + str(df.shape[1])
        # print(str1)
        self.df = df
        #self.trv_refresh()
        self.analyze_cards(df)  # Call analyze_cards to assign the DataFrame

    def analyze_cards(self, df):
        self.df = df
# below are all the functions for each question

    def calculate_red_creature_cards(self):
        creatures = []
        redCount = 0
        idx = 0

        for type in df.cardType.values:
            if 'Creature' in type.strip():
                creatures.append(df.cardCmc[idx])
            idx += 1

        for cmc in creatures:
            if '{R}' in cmc:
                redCount += 1

        # print(redCount)
        return redCount

    def calculate_total_instant_cards(self):
        instant_cards = self.df[self.df['cardType'] == 'Instant']
        return len(instant_cards)

    def get_highest_and_lowest_priced_card(self):
        highest_priced_card = self.df[self.df['price'] == self.df['price'].max()]
        lowest_priced_card = self.df[self.df['price'] == self.df['price'].min()]
        return highest_priced_card['cardName'].values[0], lowest_priced_card['cardName'].values[0]

    def get_creatures_with_highest_attack(self, top_n=5):
        creatures = []
        idx = 0
        highest_power = 0
        most_powerful_creatures_list = []

        for type in df.cardType.values:
            if 'Creature' in type:
                # print(df['powTough'].values[idx])
                try:
                    power = int(str(df['powTough'].values[idx]).split('/')[0])
                except ValueError:
                    continue
                creatures.append((df['cardName'].values[idx], power))
                if power > highest_power:
                    highest_power = power
            idx += 1
        # print(creatures)

        for (name, power) in creatures:
            if power == highest_power:
                most_powerful_creatures_list.append(name)

        return highest_power, most_powerful_creatures_list
