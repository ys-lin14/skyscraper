import numpy as np
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
        idea_filename = sys.argv[1]
        output_filename = sys.argv[2]
        
        idea_file = open(idea_filename, 'r')
        ideas = idea_file.read()
    else:
        sample_input = 'data/sample_ideas.txt'
        sample_output = 'data/sample_ideas.csv'
        print('Please specify the input and output files.')
        print(f'Sample input: 1_preprocess_data.py {sample_input} {sample_output}')
        return
    
    # remove indicator for whether the message was edited
    filtered_ideas = re.sub(r'(edited)', '', ideas) 
    splits = re.split('\n*(.*)(\d{2}/\d{2}/2020)\n*', filtered_ideas)
    del splits[0] # delete empty match
    
    names = splits[::3]
    dates = splits[1::3]
    ideas = splits[2::3]
    
    assert len(names) == len(dates) == len(ideas)
    
    idea_data = pd.DataFrame({
        'name': names,
        'date': dates,
        'idea': ideas
    })

    # replace missing values with nan
    idea_data.replace('', np.nan, inplace=True)
     
    ideas_contain_na = idea_data.isna().any().any()
    print(f'Ideas contain missing values: {ideas_contain_na}')
    
    # drop missing values
    if (ideas_contain_na): 
        idea_data.dropna(inplace=True)
        print(f'Rows left after dropping NA: {idea_data.shape[0]}\n')
        
    duplicate_ideas = idea_data[['name', 'idea']].duplicated()
    ideas_contain_duplicates = duplicate_ideas.any()
    print(f'Ideas contain duplicates: {ideas_contain_duplicates}')

    # drop duplicates 
    # does not catch duplicate ideas from those who changed their names
    if (ideas_contain_duplicates): 
        idea_data.drop_duplicates(subset=['name', 'idea'], inplace=True)
        print(f'Rows left after dropping duplicates: {idea_data.shape[0]}')

    idea_data.reset_index(drop=True, inplace=True)
    
    idea_data['date'] = idea_data['date'].apply(to_datetime)
    idea_data.to_csv(output_filename, index=False)

if __name__ == '__main__':
    main()
