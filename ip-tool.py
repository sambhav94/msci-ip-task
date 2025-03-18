import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description="IP Tool to check IP networks and collisions in Kubernetes.")
parser.add_argument('--checkcollision', type=str, help="Path to the file containing IP networks to check for collisions.")
parser.add_argument('--report', action='store_true', help="Report the current IP networks of the container.")
args = parser.parse_args()

def get_ip_networks():
    try:
        # Run a command to gather all IP networks from the container
        result = subprocess.run(['ip', 'addr', 'show'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ip_data = result.stdout.decode('utf-8')

        # Extract the IP networks from the command output
        ip_networks = []
        for line in ip_data.splitlines():
            if 'inet' in line:
                parts = line.strip().split()
                ip_networks.append(parts[1])  # Add the IP network (e.g., 192.168.1.0/24)
        return ip_networks
    except Exception as e:
        print(f"Error fetching IP networks: {e}")
        return []

def check_ip_collision(file_path):
    try:
        with open(file_path, 'r') as f:
            ip_networks = f.readlines()
        seen_networks = set()
        collisions = []

        for network in ip_networks:
            network = network.strip()
            if network in seen_networks:
                collisions.append(network)
            else:
                seen_networks.add(network)
        
        return collisions
    except Exception as e:
        print(f"Error checking for collisions: {e}")
        return []

def main():




if __name__ == '__main__':
    if args.report:
        ip_networks = get_ip_networks()
        print("IP Networks in this container:")
        for network in ip_networks:
            print(network)
    
    if args.checkcollision:
        collisions = check_ip_collision(args.checkcollision)
        if collisions:
            print("Colliding IP Networks Found:")
            for collision in collisions:
                print(collision)
        else:
            print("No collisions found.")
