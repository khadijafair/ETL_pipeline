import os
import airbyte as ab
import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

source = ab.get_source(
    "source-github",
    install_if_missing=True,
    config={
        "repositories": ["airbytehq/quickstarts"],
        "credentials": {
            "personal_access_token": ab.get_secret("GITHUB_PERSONAL_ACCESS_TOKEN"),
        },
    },
)

source.check()
source.get_available_streams()
source.set_streams(["pull_requests", "issues", "reviews", "stargazers"])

cache = ab.get_default_cache()
result = source.read(cache=cache)

reviews = cache["reviews"].to_pandas()
stargazers = cache["stargazers"].to_pandas()
pull_requests = cache["pull_requests"].to_pandas()
issues = cache["issues"].to_pandas()

conn = snow.connect(
    user="khadija",
    password=os.environ.get("SNOWFLAKE_PASSWORD"), 
    account="MIJGHVH-ST58008",                             
    warehouse="COMPUTE_WH",                        
    database="GITHUB_DATA",                        
    schema="PUBLIC"                               
)

write_pandas(conn, issues, "GITHUB_ISSUES", auto_create_table=True)