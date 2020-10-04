import pandas as pd
import re
import sys

from datetime import datetime

def to_datetime(date):
    """Convert date to datetime

    Args:
        date (str):
            the date (mm/dd/yyyy) on which the suggestion
            was written

    Returns:
        dt (datetime): datetime representation of the date
    """
    
    dt = datetime.strptime(date, '%m/%d/%Y')
    return dt

def main():

    if len(sys.argv) == 3:
        wishlist_filename = sys.argv[1]
        output_filename = sys.argv[2]
        
        wishlist_file = open(wishlist_filename, 'r')
        wishlist = wishlist_file.read()
    else:
        sample_input = 'data/sample_wishlist.txt'
        sample_output = 'data/sample_wishlist.csv'
        print('Please specify the input and output files.')
        print(f'Sample input: 1_preprocess_data.py {sample_input} {sample_output}')
        return
    
    # remove indicator for whether the message was edited
    filtered_wishlist = re.sub(r'(edited)', '', wishlist) 
    splits = re.split('\n*(.*)(\d{2}/\d{2}/2020)\n*', filtered_wishlist)
    del splits[0] # delete empty match
    
    name = splits[::3]
    date = splits[1::3]
    wish = splits[2::3] # wish / idea 

    assert len(name) == len(date) == len(wish)
    
    wishlist_data = pd.DataFrame({
        'name': name,
        'date': date,
        'wish': wish
    })
    
    wishlist_data['date'] = wishlist_data['date'].apply(to_datetime)
    wishlist_data.dropna(how='any', inplace=True)
    wishlist_data.to_csv(output_filename, index=False)

if __name__ == '__main__':
    main()
