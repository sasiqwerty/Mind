---
aliases: 
tags: 
date created: Saturday, August 12th 2023, 11:48:30 am
date modified: Saturday, August 12th 2023, 1:16:39 pm
---
```powershell
# Ask the user for the directory path or use the current directory if none is provided
$directoryPath = Read-Host "Enter the directory path (or press Enter to use the current directory)"
if (-not $directoryPath) {
    $directoryPath = Get-Location
}
# Search for files containing "untitled" in their name in the specified directory and its subdirectories
$files = Get-ChildItem -Path $directoryPath -Recurse | Where-Object { $_.Name -like "*untitled*" }
# Display the list of files found
$files | ForEach-Object {
    Write-Output "Found file: $($_.FullName)"
}
# Delete the files
$files | ForEach-Object {
    Write-Output "Deleting file: $($_.FullName)"
    Remove-Item $_.FullName -Force
}
```