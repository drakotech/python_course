/*
How to Query for Specific Documents in a MongoDB Collection


> db.books.find({ name: "The War of Art" }).pretty()
{
	"_id" : ObjectId("6014ceb8451bd27e8326a3e0"),
	"name" : "The War of Art",
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Steven Pressfield"
		}
	]
}


> db.books.find({ name: "OOP Programming" }).pretty()
{
	"_id" : ObjectId("60149e20451bd27e8326a3dc"),
	"name" : "OOP Programming",
	"publishedDate" : ISODate("2021-01-29T23:45:36.583Z"),
	"authors" : [
		{
			"name" : "Jon Snow"
		},
		{
			"name" : "Ned Stark"
		}
	]
}
{
	"_id" : ObjectId("60149f2b451bd27e8326a3dd"),
	"name" : "OOP Programming",
	"publishedDate" : ISODate("2021-01-29T23:50:03.798Z"),
	"authors" : [
		{
			"name" : "Jon Snow Jr"
		}
	]
}
{
	"_id" : ObjectId("60149fba451bd27e8326a3de"),
	"name" : "OOP Programming",
	"startDate" : ISODate("2021-01-29T23:52:26.345Z"),
	"authors" : [
		{
			"name" : "Jon Snow Jr"
		}
	]
}


Notes: 

Running the find query on a collection and passing specific
arguments to it will return a specific document from that
collection. 

Note that it will return every document that satisfies the
query.


*/