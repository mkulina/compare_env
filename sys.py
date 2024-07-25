import sys
from dotenv import dotenv_values

def compare_env_files(file1, file2):
    env1 = dotenv_values(file1)
    env2 = dotenv_values(file2)

    diff = {}

    all_keys = set(env1.keys()).union(env2.keys())

    for key in all_keys:
        value1 = env1.get(key)
        value2 = env2.get(key)
        if value1 != value2:
            diff[key] = (value1, value2)

    return diff

if len(sys.argv) != 3:
    print("Usage: python compare_env.py <path/to/first/.env> <path/to/second/.env>")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

differences = compare_env_files(file1, file2)

if differences:
    print("Differences found:")
    for key, values in differences.items():
        print(f"{key}: {values[0]} != {values[1]}")
else:
    print("No differences found.")
