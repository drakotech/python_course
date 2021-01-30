/*
Introduction to MongoDB Projections


> db.books.find(
...     {
...         name: "Confident Ruby"
...     },
...     {
...         publishedDate: 1,
...         authors: 1
...     }
... ).pretty()

{
	"_id" : ObjectId("6014ceb8451bd27e8326a3df"),
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Avdi Grimm"
		}
	]
}


> db.books.find(
...     {
...         name: "Confident Ruby"
...     },
...     {
...         name: 1,
...         publishedDate: 1,
...         authors: 1
...     }
... ).pretty()

{
	"_id" : ObjectId("6014ceb8451bd27e8326a3df"),
	"name" : "Confident Ruby",
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Avdi Grimm"
		}
	]
}


> db.books.find(
...     {
...         name: "Confident Ruby"
...     },
...     {
...         name: 1,
...         authors: 1
...     }
... ).pretty()

{
	"_id" : ObjectId("6014ceb8451bd27e8326a3df"),
	"name" : "Confident Ruby",
	"authors" : [
		{
			"name" : "Avdi Grimm"
		}
	]
}


> db.books.find(
...     {
...         name: "Confident Ruby"
...     },
...     {
...         _id: 0,
...         name: 1,
...         authors: 1
...     }
... ).pretty()

{
	"name" : "Confident Ruby",
	"authors" : [
		{
			"name" : "Avdi Grimm"
		}
	]
}


Notes: 

In order to query only specific keys from a document you can
use a projection.

A projection can be passed as a second argument object in the
find() query. Here you can label what values you want with 
a 1, and the ones you don't want with a 0. 

By default the keys you omit will be marked as a 0 except 
for the _id. To not have the _id returned you will need to
specify a 0 to it. It is the only special case.

*/