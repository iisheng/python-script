import records

rows = [
	{"x": 1, "y": 2},
	{"x": 2, "y": 3},
	{"x": 3, "y": 4},
	{"x": 4, "y": 5}
]
results = records.RecordCollection(iter(rows))
with open('demo.xlsx', 'wb') as f:
	f.write(results.export('xlsx'))
