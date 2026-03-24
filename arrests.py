import pandas as pd


def types(file):

   df = pd.read_csv(file)

   return df['PD_DESC'].unique()


if __name__ == '__main__' :
   
   x = types('NYPD_Arrests.csv')
   print(len(x))
