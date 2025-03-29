import os

def load_env(file_path=".env"):
    env_vars = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    env_vars[key.strip()] = value.strip()
    return env_vars

def get_env(key, file_path=".env"):
    env_vars = load_env(file_path)
    return env_vars.get(key, None)

