$ErrorActionPreference = "Continue"
$py = (Get-Command py).Source
$ex = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\export-cursor-sessions.py"
Write-Host "=== REF single + archive ==="
& $py $ex --composer-id "c36b6eba-22c9-445e-bbcf-3e01ba02b2f1" --archive-old
Write-Host "EXIT: $LASTEXITCODE"
