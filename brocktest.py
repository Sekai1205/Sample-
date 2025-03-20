import hashlib
import json
import random

# Define a geodesic grid with unique IDs for cells
def generate_geodesic_grid(num_cells):
    grid = {}
    for i in range(num_cells):
        grid[f"Cell-{i+1}"] = {
            "GIS_data": {
                "coordinates": (random.uniform(-90, 90), random.uniform(-180, 180)),
                "address": f"Address-{i+1}",
                "zip_code": random.randint(10000, 99999)
            },
            "blockchain_hash": None
        }
    return grid

# Blockchain functions
def create_block(data, previous_hash='0'):
    block = {
        'data': data,
        'previous_hash': previous_hash,
        'hash': hashlib.sha256(json.dumps(data).encode()).hexdigest()
    }
    return block

def add_to_blockchain(grid):
    blockchain = []
    previous_hash = '0'
    
    for cell_id, cell_data in grid.items():
        block_data = {
            "cell_id": cell_id,
            "GIS_data": cell_data["GIS_data"]
        }
        block = create_block(block_data, previous_hash)
        blockchain.append(block)
        grid[cell_id]["blockchain_hash"] = block["hash"]
        previous_hash = block["hash"]
    
    return blockchain

# Generate grid and blockchain
num_cells = 10  # Number of cells in the grid
geodesic_grid = generate_geodesic_grid(num_cells)
blockchain = add_to_blockchain(geodesic_grid)

# Output grid and blockchain
print("Geodesic Grid:")
for cell_id, data in geodesic_grid.items():
    print(f"{cell_id}: {data}")

print("\nBlockchain:")
for block in blockchain:
    print(block)
