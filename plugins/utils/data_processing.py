from datetime import datetime
import pandas as pd
from io import StringIO, BytesIO
import os



def transform_weather_data(raw):
    if not raw or raw.get("cod") != 200:
        return None
    try:
        return {
            "city": raw.get("name"),
            "country": raw.get("sys", {}).get("country"),
            "temperature": raw.get("main", {}).get("temp"),
            "humidity": raw.get("main", {}).get("humidity"),
            "pressure": raw.get("main", {}).get("pressure"),
            "description": raw.get("weather", [{}])[0].get("description"),
            "wind_speed": raw.get("wind", {}).get("speed"),
            "coordinates": raw.get("coord", {}),
            "timestamp": datetime.utcnow().isoformat(),
            "status": "success"
        }
    except:
        return None

def fetch_and_process_weather(hook, cities):
    raw_list = [hook.fetch_current_weather(city) for city in cities]
    cleaned = [transform_weather_data(r) for r in raw_list if transform_weather_data(r)]
    return pd.DataFrame(cleaned)

def save_dataframe_to_csv(df, prefix="weather_data", output_dir="data/output"):
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{prefix}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)
    return file_name


def upload_df_to_s3(df,s3_hook, bucket_name, s3_key_prefix="weather_data"):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    bytes_buffer = BytesIO(csv_buffer.getvalue().encode('utf-8'))
    bytes_buffer.seek(0)

    s3_key = f"{s3_key_prefix}_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    s3_hook.upload_fileobj(bytes_buffer, bucket_name, s3_key)
    return s3_key
