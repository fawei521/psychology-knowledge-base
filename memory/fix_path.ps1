$newPaths = @('E:\ai-tools\.venv\Scripts', 'E:\.cargo\bin')
$current = [Environment]::GetEnvironmentVariable('Path', 'User')
if ($current -and $current -ne ';') {
    $existing = $current -split ';' | Where-Object { $_ -and $_ -ne 'C:\msys64\mingw64\bin' }
    foreach ($p in $existing) {
        if ($newPaths -notcontains $p) {
            $newPaths += $p
        }
    }
}
$newPath = $newPaths -join ';'
[Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
Write-Host $newPath
