# Guide to NoSQL Databases for Developers

MongoDB_document_store = "https://www.mongodb.com/"
Redis_memory_data_store = "http://redis.io/"
Google_BigTable = "https://cloud.google.com/bigtable/"

"""
The main difference between SQL and NoSQL is that SQL language
is a structured query language designed for managing data in 
a relational database management systems. Relational database 
management systems are often called SQL databases since they 
use the SQL language. Since the mid-1980s, SQL has been a 
standard for querying and managing RDBMS data sets.

Oracle SQl server or MySQL have a tablular structure and
interface similar to spreadsheets, whereas NoSQL databases 
have various types of formats and can therefore be much more 
flexible.

For example where users need to create surveys with a different
number of fields. SQL database could handle it but it would 
be very clunky. A NoSQL database can handle it no problem by 
allowing the fields to be created dynamically and then each 
record will be stored with each of its unique characteristics.

Its important to note that one of the greatest strengths of
NoSQL, its flexibility, also presents its greatest challenge.

Imagine that you are building out an inventory application 
that has fields that need to connect to other tables, such as
a user table for the employee entering the information, a 
vendor table, and a tax table to calculate depreciation. If 
you were to attempt to implement a NoSQL database for this 
inventory option you’d end up having to work very hard to map 
the values between the models and it would also make for a 
very difficult application to maintain. In this case study, a
relational database (rdms) would work perfectly.

So when you’re trying to decide on which database to use, it 
really comes down to what the requirements of the application
are. If you wanted to chop a tree down you wouldn’t use a 
hammer, you’d use an ax because it’s basic common sense to 
utilize the right tool for the right job. And it’s the same 
way with software development, I don’t believe in the SQL vs 
NoSQL debate, they are both tools and they are the most 
effective when used in an application that works well with 
their strengths.

A good rule of thumb is to simply follow the guidelines given
by the names themselves:

 * If you have data that relies heavily on relationships then 
   it’s probably the best fit to utilize a relational SQL 
   database.
 * If you have an unstructured data set that needs flexibility,
   then it may be the best option to go with a database that is
   Not SQL, such as a NoSQL database.

NoSQL looks like JSON and its actually called BSON (Binary JSON)
and it really is just a set of key-value pair data stores that
can be structured however your application needs.

A relational SQL database is built around relationships whereas
as NoSQL database is all encapsulated into a single object.

It’s important to understand that there is no such thing as a 
standard NoSQL database, there are many different variations. 
There are Key/Value pair stores, wide-column family stores, 
document databases, and graph databases.

The above links are some examples of these.

"""