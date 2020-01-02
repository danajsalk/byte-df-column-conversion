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
  

![simple_byte](https://user-images.githubusercontent.com/46821074/71698359-7f1aa700-2d78-11ea-993a-5cd55d18f40b.png)


**Converted**

![simple_byte_converted](https://user-images.githubusercontent.com/46821074/71698378-935ea400-2d78-11ea-9b20-fb4cefbc7879.png)



**Complex Example** Nested JSON Byte
* d2 = {"food": ["fruit"
               , "vegetable"]
    , "color": ["red"
                , "orange"]
    , "data": [b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]'
               , b'[{"type":"fruit", "data": {"apple":"red", "orange":"orange"}}, {"type": "vegetable", "data": {"onion":"white", "carrot": "orange"}}]']
     }
     
 ![complex_byte_conversion](https://user-images.githubusercontent.com/46821074/71698391-9c4f7580-2d78-11ea-86e4-1d8598a2f8ac.png)

    

## How to Run: 
</br>

* Run converting_df_byte_columns.py
