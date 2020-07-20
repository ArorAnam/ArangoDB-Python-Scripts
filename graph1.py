from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('test', username='root', password='naman02')

# List existing graphs in the database.
db.graphs()

# Create a new graph named "school" if it does not already exist.
# This returns an API wrapper for "school" graph.
if db.has_graph('school'):
    school = db.graph('school')
else:
    school = db.create_graph('school')

# Retrieve various graph properties.
print(school.name)
print(school.db_name)
print(school.vertex_collections())
print(school.edge_definitions())

# Delete the graph.
db.delete_graph('school')