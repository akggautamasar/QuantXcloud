import asyncio
import config
from pathlib import Path
from pyrogram import Client
from utils.logger import Logger
import os
import signal

logger = Logger(__name__)

# Initialize empty dictionaries for clients and workloads
multi_clients = {}
premium_clients = {}
work_loads = {}
premium_work_loads = {}
main_bot = None

async def initialize_clients():
    global multi_clients, work_loads, premium_clients, premium_work_loads
    logger.info("Initializing Clients")

    # Create cache directory if it doesn't exist
    session_cache_path = Path(f"./cache")
    session_cache_path.parent.mkdir(parents=True, exist_ok=True)

    # Initialize single bot client
    client_id = 1
    bot_token = config.SYSTEM_BOT_TOKEN

    async def start_client(client_id, token, type):
        try:
            logger.info(f"Starting - {type.title()} Client {client_id}")

            if type == "bot":
                # Create a single bot client
                client = Client(
                    name=str(client_id),
                    bot_token=token,
                    workdir=str(session_cache_path),
                    no_updates=True,  # Disable updates to save memory
                    takeout=True,    # Use takeout session to reduce memory usage
                    max_concurrent_transmissions=1,  # Limit concurrent operations
                    **({"api_id": config.API_ID, "api_hash": config.API_HASH} if config.API_ID and config.API_HASH else {})
                )

                await client.start()
                multi_clients[client_id] = client
                work_loads[client_id] = 0
                logger.info(f"Started - {type.title()} Client {client_id} successfully")

        except Exception as e:
            logger.error(f"Error starting {type} client {client_id}: {str(e)}")
            raise

    # Start the single bot client
    await start_client(client_id, bot_token, "bot")
    logger.info("All clients initialized successfully")

    return True

async def get_client():
    """Get a client with the lowest workload"""
    if not multi_clients:
        await initialize_clients()
    
    index = min(work_loads, key=work_loads.get)
    work_loads[index] += 1
    return multi_clients[index]

async def release_client(client):
    """Release a client and decrease its workload"""
    for client_id, c in multi_clients.items():
        if c == client:
            work_loads[client_id] -= 1
            break
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    bot_token=token,
                    workdir=session_cache_path,
                )
                client.loop = asyncio.get_running_loop()
                await client.start()
                await client.send_message(
                    config.STORAGE_CHANNEL,
                    f"Started - {type.title()} Client {client_id}",
                )
                multi_clients[client_id] = client
                work_loads[client_id] = 0
            elif type == "user":
                client = await Client(
                    name=str(client_id),
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=token,
                    sleep_threshold=config.SLEEP_THRESHOLD,
                    workdir=session_cache_path,
                    no_updates=True,
                ).start()
                await client.send_message(
                    config.STORAGE_CHANNEL,
                    f"Started - {type.title()} Client {client_id}",
                )
                premium_clients[client_id] = client
                premium_work_loads[client_id] = 0

            logger.info(f"Started - {type.title()} Client {client_id}")
        except Exception as e:
            logger.error(
                f"Failed To Start {type.title()} Client - {client_id} Error: {e}"
            )

    await asyncio.gather(
        *(
            [
                start_client(client_id, client, "bot")
                for client_id, client in all_tokens.items()
            ]
            + [
                start_client(client_id, client, "user")
                for client_id, client in all_sessions.items()
            ]
        )
    )
    if len(multi_clients) == 0:
        logger.error("No Clients Were Initialized")

        # Forcefully terminates the program immediately
        os.kill(os.getpid(), signal.SIGKILL)

    if len(premium_clients) == 0:
        logger.info("No Premium Clients Were Initialized")

    logger.info("Clients Initialized")

    # Load the drive data
    await loadDriveData()

    # Start the backup drive data task
    asyncio.create_task(backup_drive_data())


def get_client(premium_required=False) -> Client:
    global multi_clients, work_loads, premium_clients, premium_work_loads

    if premium_required:
        index = min(premium_work_loads, key=premium_work_loads.get)
        premium_work_loads[index] += 1
        return premium_clients[index]

    index = min(work_loads, key=work_loads.get)
    work_loads[index] += 1
    return multi_clients[index]
