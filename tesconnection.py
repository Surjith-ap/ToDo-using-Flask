from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

db_url = os.getenv('DATABASE_URL')
print(f"Testing connection...")
print(f"Database URL: {db_url[:50]}...{db_url[-20:]}")  # Hide middle part

try:
    from urllib.parse import urlparse
    
    result = urlparse(db_url)
    
    print(f"\n=== Connection Details ===")
    print(f"Host: {result.hostname}")
    print(f"Port: {result.port}")
    print(f"User: {result.username}")
    print(f"Database: {result.path[1:]}")
    
    # Try to connect
    print(f"\n=== Attempting Connection ===")
    conn = psycopg2.connect(
        host=result.hostname,
        port=result.port,
        user=result.username,
        password=result.password,
        database=result.path[1:]
    )
    print("✅ CONNECTION SUCCESSFUL!")
    
    # Test query
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ PostgreSQL Version: {version[0][:50]}...")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ CONNECTION FAILED!")
    print(f"Error: {e}")
