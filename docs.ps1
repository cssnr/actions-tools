param (
    [switch]$c
)

$ErrorActionPreference = "Stop"

write-output "Clean:      $c"

if ($c) {
    Write-Host -ForegroundColor Yellow "Cleaning Docs..."
    $site_dir = ".\site"
    if (Test-Path $site_dir) {
        Write-Host -ForegroundColor Cyan "Removing: $site_dir"
        Remove-Item -Force -Recurse $site_dir
    }
    $cache_dir = ".\.cache"
    if (Test-Path $cache_dir) {
        Write-Host -ForegroundColor Cyan "Removing: $cache_dir"
        Remove-Item -Force -Recurse $cache_dir
    }
}

zensical serve
