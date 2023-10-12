---
aliases: 
tags:
date created: Sunday, July 30th 2023, 11:58:50 am
date modified: Monday, July 31st 2023, 1:45:56 pm
---
How to using PowerShell how to rename 20 files #script
- Each file has a common part of the name that I wish to remove  
- The common phrase should be gone and the rest of the file name should remain

```
Get-ChildItem | ForEach-Object {
    $NewName = $_.Name -replace "-PAM-ADMIN", ""
    Rename-Item -Path $_.FullName -NewName $NewName
}
```

This is meant to delete the folders sri is not supposed to see

```
# Set the folder names you want to search for and delete (separated by commas)
$targetFolderNames = "TargetFolder1,TargetFolder2,TargetFolder3"

# Convert the target folder names to an array
$targetFolders = $targetFolderNames -split ','

# Get a list of all folders with the specified names in the current directory and its subdirectories
$foldersToDelete = Get-ChildItem -Path "C:\Path\To\Your\Root\Folder" -Recurse |
    Where-Object { $_.PSIsContainer -and $targetFolders -contains $_.Name }

# Check if any matching folders were found
if ($foldersToDelete.Count -eq 0) {
    Write-Host "No folders with the specified names found."
}
else {
    Write-Host "Folders with the specified names found:"

    # Print the names of the matching folders
    foreach ($folder in $foldersToDelete) {
        Write-Host $folder.FullName
    }

    # Ask for confirmation before deleting the folders
    $confirmation = Read-Host "Do you want to delete these folders? (Y/N)"
    if ($confirmation -eq "Y" -or $confirmation -eq "y") {
        # Delete the folders and their contents
        $foldersToDelete | Remove-Item -Recurse -Force
        Write-Host "Folders deleted successfully."
    }
    else {
        Write-Host "Folders were not deleted."
    }
}

```