import pandas as pd

data = pd.read_csv("resource\Abha_database.csv")

data.set_index("Abha No.", inplace=True)

def search(aNo):
    try:
        curr_rec = data.loc[aNo]
        name = curr_rec[0]
        age = curr_rec[1]
        major_ailment = curr_rec[2]
        return name, age, major_ailment
    except KeyError:
        print("Wrong Abha No.")




if __name__=="__main__":
    name, age, major_ailment=search(1001)
    print(name, age, major_ailment)
