# Converting Dataframe Byte Columns to JSON String
</br>

## Summary
Data from different sources comes in many different datatypes including "bytes". If you end up with a dataframe with a byte column, this repository has examples of how to convert byte dataframe columns to standard strings or JSON strings.  


## Example SQL Data: 

**Byte Format Example:**

* d = pd.DataFrame({'fruit': ['apple', 'orange', 'banana']
   
   , 'color': [b'red', b'orange', b'yellow']
   
   , 'count': ['4', '5', '3']
  })
  

![simple_byte.png](attachment:simple_byte.png)

**Converted**

![simple_byte_converted.png](attachment:simple_byte_converted.png)

**Complex Example** Nested JSON Byte
* d2 = {"food": ["fruit"
               , "vegetable"]
    , "color": ["red"
                , "orange"]
    , "data": [b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]'
               , b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]']
     }
     
![complex_byte_conversion.png](attachment:complex_byte_conversion.png)     
    

## How to Run: 
</br>

* Run converting_df_byte_columns.py
