from airflow.models import BaseOperator
from plugins.utils.data_processing import fetch_and_process_weather, save_dataframe_to_csv, upload_df_to_s3
from plugins.custom_hooks.weather_api_hook import WeatherAPIHook
from plugins.custom_hooks.aws_s3_hook import AwsS3Hook

def UploadToS3Operator():
    hook = WeatherAPIHook()
    test_data = hook.fetch_current_weather("London")
    if not test_data or test_data.get("cod") != 200:
        print("API connection failed")
        return
    
    cities = ["London", "Paris", "Tokyo", "New York"]
    df = fetch_and_process_weather(hook, cities)

    if df.empty:
        print("No valid data to process")
        return

    # For Saving to Local Drive
    saved_file = save_dataframe_to_csv(df)
    print(f"Saved local CSV file: {saved_file}")

    # For Uploading to AWS Bucket
    s3_hook = AwsS3Hook(region_name="ap-southeast-2")
    bucket_name = "weather1data"
    s3_key = upload_df_to_s3(df, s3_hook, bucket_name)
    print(f"Uploaded weather data to s3://{bucket_name}/{s3_key}")