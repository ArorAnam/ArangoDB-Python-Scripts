from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('test', username='root', password='naman02')

# Get the API wrapper for graph "school".
school = db.graph('school')

# Get the API wrapper for edge collection "teach".
if school.has_edge_definition('teaches'):
    teaches = school.edge_collection('teaches')
else:
    teaches = school.create_edge_definition(
        edge_collection='teaches',
        from_vertex_collections=['teachers'],
        to_vertex_collections=['lectures']
    )

# Edge collections have a similar interface as standard collections.
teaches.insert({
    '_key': 'jon-CSC101',
    '_from': 'teachers/jon',
    '_to': 'lectures/CSC101'
})
teaches.replace({
    '_key': 'jon-CSC101',
    '_from': 'teachers/jon',
    '_to': 'lectures/CSC101',
    'online': False
})
teaches.update({
    '_key': 'jon-CSC101',
    'online': True
})
teaches.has('jon-CSC101')
teaches.get('jon-CSC101')
teaches.delete('jon-CSC101')

# Create an edge between two vertices (essentially the same as insert).
teaches.link('teachers/jon', 'lectures/CSC101', data={'online': False})

# List edges going in/out of a vertex.
print(teaches.edges('teachers/jon', direction='in'))
print(teaches.edges('teachers/jon', direction='out'))