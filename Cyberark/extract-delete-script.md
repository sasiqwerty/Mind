---
aliases: 
tags: 
date created: Monday, September 18th 2023, 8:36:32 pm
date modified: Saturday, January 27th 2024, 6:59:37 pm
---
code to extract all zip files and deletes the zip files

```powershell
# Ensure the required assembly is loaded
Add-Type -AssemblyName System.IO.Compression.FileSystem

# Get all .zip files in the current directory
$zipFiles = Get-ChildItem -Path .\*.zip

# Loop through each .zip file
foreach ($zipFile in $zipFiles) {
    # Create a directory named after the zip file (without .zip extension)
    $extractPath = Join-Path -Path $zipFile.DirectoryName -ChildPath ($zipFile.BaseName)
    New-Item -Path $extractPath -ItemType Directory -Force

    # Extract the .zip file into the new directory
    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipFile.FullName, $extractPath)

    # Delete the .zip file
    Remove-Item -Path $zipFile.FullName -Force
}

Write-Output "All zip files extracted into their respective folders and zip files deleted."
```