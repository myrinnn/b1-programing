devices = [
("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]),
("192.168.1.12", [23, 80, 3389])
]
print("Scanning network devices...")
print()

risky_ports = [21, 23, 3389]
risks ={}

risk_count = 0

for ip, ports in devices:
    risks[ip] = 0
    for port in ports:
        for risky_port in risky_ports:
            if port == risky_port:
                risks[ip] += 1
                risk_count += 1
                print("WARNING: " + ip + " has risky port " + str(port) + " open")
    print(ip + " has " + str(risks[ip]) + " risky port(s)")    
    print()

print("Scan complete: " + str(risk_count) + " security risks found")

    