from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# System configuration for user setup
SYSTEM_BOT_TOKEN = os.getenv("SYSTEM_BOT_TOKEN")  # Main bot token for user setup
SYSTEM_CHANNEL = int(os.getenv("SYSTEM_CHANNEL", "0"))  # System channel ID (optional)
SYSTEM_CHANNEL_MSG_ID = int(os.getenv("SYSTEM_CHANNEL_MSG_ID", "0"))  # System message ID (optional)

# Website configuration
WEBSITE_URL = os.getenv("WEBSITE_URL", "http://localhost:8000")

# Telegram API credentials (only needed for system bot)
API_ID = int(os.getenv("API_ID", "0"))  # Default to 0 if not set
API_HASH = os.getenv("API_HASH", "")  # Default to empty if not set

# File handling configuration
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "209715200"))  # Default: 200MB
MAX_SIMULTANEOUS_DOWNLOADS = int(os.getenv("MAX_SIMULTANEOUS_DOWNLOADS", "3"))

# Optional configuration
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")  # Default to "admin" if not set

# Validate required configurations
required_configs = [
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SYSTEM_BOT_TOKEN",
    "WEBSITE_URL"
]

for config in required_configs:
    if not os.getenv(config):
        raise ValueError(f"Missing required configuration: {config}")
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Domain to auto-ping and keep the website active
WEBSITE_URL = os.getenv("WEBSITE_URL", "http://localhost:8000")

# Bot Mode Configuration
SYSTEM_BOT_TOKEN = os.getenv("SYSTEM_BOT_TOKEN", "")
if SYSTEM_BOT_TOKEN.strip() == "":
    raise ValueError("SYSTEM_BOT_TOKEN is required for system configuration")

# Telegram API credentials for system bot
API_ID = int(os.getenv("API_ID", "0"))  # Default to 0 if not set
API_HASH = os.getenv("API_HASH", "")  # Default to empty if not set

# Optional system channel configuration
SYSTEM_CHANNEL = int(os.getenv("SYSTEM_CHANNEL", "0"))  # Optional, used for system files
SYSTEM_CHANNEL_MSG_ID = int(os.getenv("SYSTEM_CHANNEL_MSG_ID", "0"))  # Optional, used for system backups

# Admin configuration
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")  # Default to "admin" if not set

# File handling configuration
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "209715200"))  # Default: 200MB
MAX_SIMULTANEOUS_DOWNLOADS = int(os.getenv("MAX_SIMULTANEOUS_DOWNLOADS", "3"))
