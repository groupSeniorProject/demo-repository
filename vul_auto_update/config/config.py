# api
CWE_API_URL = "https://cwe-api.mitre.org/api/v1"
OSV_API_URL = "https://osv.dev/api/v1/query"


# Neo4j Database
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"


# Scheduling Configuration
UPDATE_INTERVAL = "daily"  # daily, weekly, monthly

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "vul_auto_update.log"

# Retry and Timeout Settings
REQUEST_RETRIES = 3
REQUEST_TIMEOUT = 10  # seconds

# Proxy Configuration
PROXY = None  # "http://proxyserver:port"
