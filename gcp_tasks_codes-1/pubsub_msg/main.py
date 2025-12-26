main.py:
import functions_framework
import base64
import json
from google.cloud import bigquery
from datetime import datetime
 
bq_client = bigquery.Client()
 
@functions_framework.cloud_event
def pubsub_to_bigquery(cloud_event):
    msg = cloud_event.data["message"]
    payload = base64.b64decode(msg["data"]).decode("utf-8")
    data = json.loads(payload)
 
    row = {
        "event": data.get("event"),
        "user": data.get("user"),
        "ts": datetime.utcnow().isoformat()
    }
 
    table_id = "pavanp.pavan_events_ds.user_events"    ("pavanp inplace of give project id  & pavan_events_ds this also according to the our creating name")
 
    errors = bq_client.insert_rows_json(table_id, [row]) # inserting
 
    if errors:
        print(f"Bigquery Insert Failed: {errors}")
        raise RuntimeError(errors)
    
    print(f"Bigquery Insert Succeeded", row)

