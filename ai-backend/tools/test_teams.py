import sys
import os
from dotenv import load_dotenv
load_dotenv()

# Add the parent folder (ai-backend) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio
from sports_apis import APIFootballClient  # Make sure this matches your module name

async def main():
    api_key = os.getenv("API_FOOTBALL_KEY")
    base_url = os.getenv("API_FOOTBALL_BASE_URL")
    client = APIFootballClient(api_key,base_url)

    # get all teams
    result = await client.get_teams(39, 2025)  # 7131=Estadio Libertadores de América,2025

    # get one team
    result = await client.get_team(3997)  

if __name__ == "__main__":
    asyncio.run(main())
