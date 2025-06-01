from server import CalDAVClient

cliente = CalDAVClient('http://host.docker.internal:5232/radicale/', 'dudustefanello', 'Duckbill')
cliente.connect()
print(cliente.get_calendar())