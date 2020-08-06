from fabric import Connection
import concurrent.futures


def get_ping(host):
    """'The method for check ping"""
    get_host = (host)
    thread = concurrent.futures.ThreadPoolExecutor()
    # command = os.popen(f"ping -c4 {get_host } | tail  -2 | head -1 ").read().split(" ").pop(3)
    server_list = ['91.201.25.57', '185.250.206.220','35.178.203.123']
    awk = "awk '{print $1}'"
    cmd = f'''ping -c 4 {get_host} | tail  -2 | head -1 | cut -d "," -f 2 | {awk} '''
    fun = lambda x: Connection(f'root@{x}').run(cmd , hide=True).stdout
    g = [ ]
    for i in thread.map(fun, server_list):
        g.append(str(i).rstrip('\n'))
    return g
print(get_ping('8.8.8.8'))

