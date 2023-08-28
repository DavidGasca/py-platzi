items = [
  {'product':'camisa', 'price':50},
  {'product':'pantalon', 'price':70},
  {'product':'sombrero', 'price':65},
]

prices = list( map( lambda item: item['price'], items ) )
print( prices )

def addTaxes(item):
  item['taxes'] = item['price'] * 0.16
  return item

def addTaxesInmutable(item):
  newItem = item.copy()
  newItem['taxes'] = newItem['price'] * 0.16
  return newItem

itemTaxes = list( map(addTaxesInmutable, items) )
  
#new_items = list( map( lambda x: x|{'tax': x['price']*0.16} ,items))
#new_items = list( map(lambda item: {**item, **{'tax':item['price']*0.16}}, items))
print('DICT BASE')
print(items)
print('DICT MODIFICADO')
print(itemTaxes)
#print(new_items)

#items mutables, afecta la lista original
itemTaxes = list( map(addTaxes, items) )
print('DICT BASE - alterado por addTaxes')
print(items)