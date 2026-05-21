import kagglehub

# Download latest version
path = kagglehub.dataset_download("gvyshnya/gold-future-prices")

print("Path to dataset files:", path)