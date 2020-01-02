def convert_all_columns(df):
    """ Convert a byte column in dataframe to a regular string
    
    :param dataframe df
    """
    df = df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)
    return df

tdef = convert_byte_columns(tdf) 


def convert_byte_column_json_string(df, column):
    """ Convert a nested json byte string to json string
    
    :param datafrmae df
    :param series column
    """
    df['byte_conversion'] = df.apply(lambda x: convert_byte_to_string(x[column]), axis=1)
    
def convert_byte_to_string(byte_value):
    try:
        byte_str = byte_value.decode('utf8')
        data = json.loads(byte_str)
        s = json.dumps(data, sort_keys=False)
        return s
    
    except (UnicodeDecodeError, AttributeError):
        print("FAIL")
        pass

d = {'fruit': ['apple', 'orange', 'banana']
    , 'color': [b'red', b'orange', b'yellow']
    , 'count': ['4', '5', '3']
  }

d2 = {"food": ["fruit"
               , "vegetable"]
    , "color": ["red"
                , "orange"]
    , "data": [b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]'
               , b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]']
     }


simple_food_df = pd.DataFrame(d)
complex_food_df = pd.DataFrame(d2)

convert_simple_food_df = convert_all_columns(simple_food_df)

# DOES NOT CHECK IF YOU SEND IT BYTE ("b'")
convert_byte_column(complex_food_df, 'data')
