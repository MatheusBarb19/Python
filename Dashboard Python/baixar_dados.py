import kagglehub

# Download latest version
path = kagglehub.dataset_download("ezequielalvessoares/pib-dos-municpios-brasileiros")

print("Path to dataset files:", path)