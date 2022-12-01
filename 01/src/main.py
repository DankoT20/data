import pandas as pd
import matplotlib.pyplot as plt

# Panda egy Python könyvtár ami adatok feldolgozását könnyíti meg.
# Nagyban segít az adatok tisztításába, analízisében, manipulációjában.

# print(pd.__version__) attribútum megadja a pandas verzióját
# print(df.loc["day2"])


def main():
    print('1-----------1---------1-------'*4)

    data = { #lista
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    df = pd.DataFrame(data, index=["day1", "day2", "day3"]) #idexek nevei

    print(df)

    print('2--------2----------2---------' * 4)

    print(df.loc["day2"])    #day2 nevű indexre mutat, megadja értékeit, nevét, típusát

    print('3--------3----------3---------' * 4)

    df = pd.read_csv('MOCK_DATA.csv')  # adat beolvasása excelből
    print(df.to_string())  # teljes adathalmaz megjelenítése

    print('4--------4----------4---------' * 4)

    print(pd.options.display.max_rows) #visszaadja a maximum sor számát, max 60 de módosítható
    pd.options.display.max_rows = 9999 #max visszaadható sorok száma
    print(pd.options.display.max_rows) #itt már 9999

    print('5--------5-----------5--------' * 4)

    df = pd.read_json('MOCK_DATA.json') # json = python szótár
    print(df.head()) #visszaadja az első 5 sort

    print('6--------6-----------6--------' * 4)

    print(df.tail()) #visszaadja az utolsó 5 sort
    print(df.info()) # információt ad az adatokról, pl mennyi null érték van

    print('7--------7-----------7--------' * 4)

    new_df = df.dropna() # egy új dataFramet ad vissza, nem változtatja az eredetit,
    # üres cellákat, null értéket, NaN értéket nem veszi figyelembe, megtiszítja az adatbázist
    print(new_df.to_string())
    #df.dropna(inplace=True) #ugyan úgy működik, viszont ez már az eredeti dataFramet módosítja
    #df.fillna(130, inplace=True) #minden üres cellát feltölt 130-al
    #df["Calories"].fillna(130, inplace=True) #minden calories tag el jelölt üres mezőt feltölt 130 al
    print('8--------8-----------8--------' * 4)
    print(df.duplicated())  #True értéket ad vissza ha a sor duplikálva van
    df.drop_duplicates(inplace=True) #eldobja az összes duplikált mezőt

    print('9--------9-----------9--------' * 4)
    df.corr()    #megmutatja az adatok közötti korrelációt /kapcsolatot/
    df.plot()    #létrehoz egy grafikont
    plt.show()  #megmutatja a grafikont















if __name__ == '__main__':
    main()


