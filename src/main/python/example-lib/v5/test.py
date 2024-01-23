from example import HelloAdapter

adapter = HelloAdapter()
adapter.hello()
adapter.hello_world(name='Rajan')
adapter.hello_world_n_times(message='hello world', count=4)
print(adapter.reverse(text='asdf'))
