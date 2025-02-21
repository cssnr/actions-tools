$ErrorActionPreference = "Stop"

$egg_dir = ".\src\*.egg-info"
if (Test-Path $egg_dir) {
    Write-Output "Removing: $egg_dir"
    Remove-Item -Force -Recurse $egg_dir
}
if (Test-Path ".\dist") {
    Write-Output "Removing: .\dist"
    Remove-Item -Force -Recurse ".\dist"
}

if ($args[0] -eq "clean") {
    Write-Output "Clean Only. Not Building!"
    exit
}

python.exe -m build
#python -m pip uninstall actions-tools
#python -m pip install .\dist\actions_tools-0.0.1-py3-none-any.whl

Write-Output "Success."
