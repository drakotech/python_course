/*
Query for a Portion of a Nested Array Element in a 
Document using $slice


> db.books.find(
...     {
...         name: "Blink"
...     },
...     {
...         publishedDate: 1,
...         name: 1,
...         authors: { $slice: 1}
...     }
... ).pretty()

{
	"_id" : ObjectId("6014e3371ff225f159e17ea2"),
	"name" : "Blink",
	"authors" : [
		{
			"name" : "Malcolm Gladwell"
		}
	]
}


> db.books.find(
...     {
...         name: "Blink"
...     },
...     {
...         publishedDate: 1,
...         name: 1,
...         authors: { $slice: 2}
...     }
... ).pretty()

{
	"_id" : ObjectId("6014e3371ff225f159e17ea2"),
	"name" : "Blink",
	"authors" : [
		{
			"name" : "Malcolm Gladwell"
		},
		{
			"name" : "Ghost Writer"
		}
	]
}



> db.books.find(
...     {
...         name: "Blink"
...     },
...     {
...         publishedDate: 1,
...         name: 1,
...         authors: { $slice: -1}
...     }
... ).pretty()

{
	"_id" : ObjectId("6014e3371ff225f159e17ea2"),
	"name" : "Blink",
	"authors" : [
		{
			"name" : "Ghost Writer"
		}
	]
}


Notes:

When accessing a nested list inside a key you can request
a specific element by using the $slice method. This method
can grab a specific nested element in a collection.

Using $slice: 1 grabs the first element, 2 grabs the first
2 elements, -1 grabs the last element etc.

*/