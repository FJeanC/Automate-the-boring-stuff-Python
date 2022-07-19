tableData = [   ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
                #['Teste', 'Teste2', 'Teste33','Teste44']
            ]

def print_table(table):

    colWidth = [0] * len(table)
    # Find the biggest string for ever row to
    # correctly justify the content in the columns when printing 
    for list_index, list_items in enumerate(table):
        colWidth[list_index] = len(max(list_items, key=len))
    
    # Transposing the list of list 
    table = [list(i) for i in zip(*table)]
    
    for item_list in table:
        for index, item in enumerate(item_list):
            print(item.rjust(colWidth[index]), end=" ")
        print()

print_table(tableData)


