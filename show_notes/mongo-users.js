db.createUser({
    user:  'jon',
    pwd: 'password',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})

/*
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use mongoCourse
switched to db mongoCourse
> db
mongoCourse
> db.createUser({
    ...     user:  'george',
    ...     pwd: 'password',
    ...     customData: { startDate: new Date() },
    ...     roles: [
        ...         { role: 'clusterAdmin', db: 'admin' },
        ...         { role: 'readAnyDatabase', db: 'admin' },
        ...         'readWrite'
        ...     ]
		... })
		
> Successfully added user: {
    "user" : "george",
    "customData" : {
    "startDate" : ISODate("2021-01-29T22:54:01.579Z")
	},
	"roles" : [
		{
			"role" : "clusterAdmin",
			"db" : "admin"
		},
		{
			"role" : "readAnyDatabase",
			"db" : "admin"
		},
		"readWrite"
	]
}

> db.createUser({
...     user:  'jon',
...     pwd: 'password',
...     customData: { startDate: new Date() },
...     roles: [
...         { role: 'clusterAdmin', db: 'admin' },
...         { role: 'readAnyDatabase', db: 'admin' },
...         'readWrite'
...     ]
... })
Successfully added user: {
	"user" : "jon",
	"customData" : {
		"startDate" : ISODate("2021-01-29T22:55:54.790Z")
	},
	"roles" : [
		{
			"role" : "clusterAdmin",
			"db" : "admin"
		},
		{
			"role" : "readAnyDatabase",
			"db" : "admin"
		},
		"readWrite"
	]
}
> db.getUsers()
[
	{
		"_id" : "mongoCourse.george",
		"userId" : UUID("7f64f48c-b030-4f2f-a54b-d219aa074c70"),
		"user" : "george",
		"db" : "mongoCourse",
		"customData" : {
			"startDate" : ISODate("2021-01-29T22:54:01.579Z")
		},
		"roles" : [
			{
				"role" : "clusterAdmin",
				"db" : "admin"
			},
			{
				"role" : "readAnyDatabase",
				"db" : "admin"
			},
			{
				"role" : "readWrite",
				"db" : "mongoCourse"
			}
		],
		"mechanisms" : [
			"SCRAM-SHA-1",
			"SCRAM-SHA-256"
		]
	},
	{
		"_id" : "mongoCourse.jon",
		"userId" : UUID("26069df4-1a78-48c0-a8f5-cbbe248d7067"),
		"user" : "jon",
		"db" : "mongoCourse",
		"customData" : {
			"startDate" : ISODate("2021-01-29T22:55:54.790Z")
		},
		"roles" : [
			{
				"role" : "clusterAdmin",
				"db" : "admin"
			},
			{
				"role" : "readAnyDatabase",
				"db" : "admin"
			},
			{
				"role" : "readWrite",
				"db" : "mongoCourse"
			}
		],
		"mechanisms" : [
			"SCRAM-SHA-1",
			"SCRAM-SHA-256"
		]
	}
]
> db.dropUser('jon')
true
> db.getUsers()
[
	{
		"_id" : "mongoCourse.george",
		"userId" : UUID("7f64f48c-b030-4f2f-a54b-d219aa074c70"),
		"user" : "george",
		"db" : "mongoCourse",
		"customData" : {
			"startDate" : ISODate("2021-01-29T22:54:01.579Z")
		},
		"roles" : [
			{
				"role" : "clusterAdmin",
				"db" : "admin"
			},
			{
				"role" : "readAnyDatabase",
				"db" : "admin"
			},
			{
				"role" : "readWrite",
				"db" : "mongoCourse"
			}
		],
		"mechanisms" : [
			"SCRAM-SHA-1",
			"SCRAM-SHA-256"
		]
	}
]


Notes:

Important commands to remember: 

  db.createUser() is used to create a user by passing an object
  following specific notations to customize via the javascript
  notation.

  db.getUsers() returns a json object with all users.

  db.dropUser('user') removed user from database.

*/