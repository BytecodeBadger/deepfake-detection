param(
    [string]$OutFile = "$env:USERPROFILE\Downloads\deepfake-and-real-images.zip",
    [string]$Url = "https://www.kaggle.com/api/v1/datasets/download/manjilkarki/deepfake-and-real-images"
)

$curl = "curl.exe"
Write-Host "Downloading dataset to $OutFile..."
& $curl -L -o $OutFile $Url
if ($LASTEXITCODE -ne 0) {
    Write-Error "Download failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}
Write-Host "Download complete."
