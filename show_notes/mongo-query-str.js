/*
How to Query for a Portion of a String in a MongoDB Document


> db.books.insert({
...     "name": "Deep Work: Rules for Focused Success in a Distracted World",
...     "publishedDate": new Date(),
...     "authors": [
...         {"name": "Cal Newport"}
...     ]
... });
WriteResult({ "nInserted" : 1 })


> db.books.findOne({ name: /.*deep work.* /i })

{
	"_id" : ObjectId("6016607af77699c4688e5711"),
	"name" : "Deep Work: Rules for Focused Success in a Distracted World",
	"publishedDate" : ISODate("2021-01-31T07:47:06.834Z"),
	"authors" : [
		{
			"name" : "Cal Newport"
		}
	]
}
> 


Notes:

In this excersise we query by using a portion of a string by use
of regular expressions in mongoDB.

MongoDB returns null if an exact match isn't found. For example
if I queried just name: 'deep work' there would be no match
therefore null is returned.

Text between slashes generally indicates a regular expression.
The asterix is used as a wildcard character. In this case 
having it before and after indicates that we look to find this
string contained anywhere inside the name of the document.

PS I added a space to not break the comment on line 15 after *
*/