from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# Replace these with your own values
bucket_name = 'gpt-j-train'
source_blob_name = 'GPT-Reddit-output-V2.2-v3/9a2e902d060e4e17b67923b51a356c9c/streaming_params'
destination_file_name = 'flax-weights.msgpack'

download_blob(bucket_name, source_blob_name, destination_file_name)
