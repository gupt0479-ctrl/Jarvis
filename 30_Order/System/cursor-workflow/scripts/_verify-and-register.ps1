$ErrorActionPreference = "Continue"
$reg = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\register-cursor-export-task.ps1"
& $reg
Write-Host "=== verify counts ==="
$wsl = (Get-ChildItem -Path "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\WSL\Cursor" -Recurse -Filter "*.md" | Where-Object { $_.Name -notlike "00 -*" -and $_.FullName -notmatch "_archive" }).Count
$win = (Get-ChildItem -Path "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Cursor" -Recurse -Filter "*.md" | Where-Object { $_.Name -notlike "00 -*" -and $_.FullName -notmatch "_archive" }).Count
Write-Host "WSL notes: $wsl"
Write-Host "Windows notes: $win"
Write-Host "=== sample Windows note head ==="
Get-ChildItem "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Cursor" -Recurse -Filter "*.md" |
  Where-Object { $_.Name -notlike "00 -*" -and $_.FullName -notmatch "_archive" } |
  Select-Object -First 1 |
  ForEach-Object { Write-Host $_.FullName; Get-Content $_.FullName -TotalCount 35 }
Write-Host "=== junctions? ==="
Get-ChildItem "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Cursor" -Directory |
  ForEach-Object {
    $raw = Join-Path $_.FullName "_raw_jsonl"
    if (Test-Path $raw) {
      $item = Get-Item $raw
      Write-Host ("{0} attributes={1} target={2}" -f $raw, $item.Attributes, $item.Target)
    }
  }
