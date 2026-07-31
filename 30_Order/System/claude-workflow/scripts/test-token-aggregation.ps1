# Standalone proof that tools_used/tokens/cost_usd/model aggregation actually
# populates (not the WSL-style silent-empty bug) before running any real
# backfill. Feeds Export-Session a hand-built fake transcript with known
# values and diffs the written frontmatter against expected numbers.

$ErrorActionPreference = "Stop"

$scriptPath = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\scripts\export-claude-session.ps1"
. $scriptPath   # dispatch is guarded off since no -TranscriptPath/-BackfillAll passed here

$testOutRoot = Join-Path $env:TEMP "export-agg-test-$(Get-Random)"
$OutRoot = $testOutRoot
New-Item -ItemType Directory -Path $testOutRoot -Force | Out-Null

$fakeTranscript = "C:\Users\ANANTG~1\AppData\Local\Temp\claude\D--Users--Anant-10-Areas-Documents-Jarvis\5bae38bb-7118-4ab6-a0dd-091c5a2ac57c\scratchpad\fake-transcript.jsonl"

$r = Export-Session -TranscriptPathIn $fakeTranscript -SessionIdIn "test-session-001" -CwdIn "D:\Users\_Anant\10_Areas\Documents\Jarvis" -SourceAppIn "ClaudeCode"

Write-Output "Export-Session status: $($r.Status)"
Write-Output "Project dir: $($r.ProjectDir)"

$mdFile = Get-ChildItem -LiteralPath $r.ProjectDir -Filter "*.md" | Select-Object -First 1
if (-not $mdFile) {
    Write-Output "FAIL: no markdown file was written"
    exit 1
}

$content = Get-Content -LiteralPath $mdFile.FullName -Raw
Write-Output "--- written frontmatter ---"
Write-Output ($content -split '---')[1]

$expected = @{
    '(?m)^\s+Bash: 2\s*$'   = 'tools_used.Bash == 2'
    '(?m)^\s+Read: 1\s*$'   = 'tools_used.Read == 1'
    '(?m)^\s+Write: 1\s*$'  = 'tools_used.Write == 1'
    'input: 300'                    = 'tokens.input == 300'
    'output: 135'                   = 'tokens.output == 135'
    'cache_creation: 15'             = 'tokens.cache_creation == 15'
    'cache_read: 20'                 = 'tokens.cache_read == 20'
    'total: 470'                     = 'tokens.total == 470'
    'cost_usd: 0.001999'             = 'cost_usd == 0.001999'
    'claude-sonnet-5'                = 'model list contains claude-sonnet-5'
    '/tmp/a.txt'                     = 'files_touched contains /tmp/a.txt'
    '/tmp/b.txt'                     = 'files_touched contains /tmp/b.txt'
}

$allPass = $true
foreach ($pattern in $expected.Keys) {
    $label = $expected[$pattern]
    if ($content -match $pattern) {
        Write-Output "PASS: $label"
    }
    else {
        Write-Output "FAIL: $label (pattern not found: $pattern)"
        $allPass = $false
    }
}

Remove-Item -LiteralPath $testOutRoot -Recurse -Force -ErrorAction SilentlyContinue

if ($allPass) {
    Write-Output "=== ALL AGGREGATION CHECKS PASSED ==="
    exit 0
}
else {
    Write-Output "=== AGGREGATION CHECKS FAILED ==="
    exit 1
}
