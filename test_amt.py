import amt.client

obj = amt.client.Client(address='192.168.0.2',
                        password='P@ssw0rd',
                        username='admin',
                        protocol='https')

obj.power_status()