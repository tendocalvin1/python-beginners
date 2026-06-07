

from server import Server

server1 = Server("backend-01",192.168, "running")
server2 = Server("backend-02",192.168, "stopped")
server3 = Server("backend-03",192.168, "restarted")


# server1.status = "Running"
# server2.status = "Stopped"

server2.stop()
server1.start()
server3.restart()