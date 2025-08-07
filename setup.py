# -- SETUP FILE FOR SECRETS --
from pathlib import Path

def create_env_file():
    print("Discord Bot Setup Wizard")
    discord_token = input("Enter your Discord Token: ").strip()

    file_content = f"""# Discord Bot Configuration
    DISCORD_TOKEN={discord_token}"""

    # Create file
    env_path = Path(".env")

    if env_path.exists():
        print(".env file already exists, skipping creation.")
        return
    
    env_path.write_text(file_content)
    print(f"Created .env file at {env_path.absolute()}")

if __name__ == "__main__":
    create_env_file()