---
type: project
status: sprout
deadline: 2025-12-23
related_progress: "[[Winter Break]]"
tags:
  - progress
---
# Battery Replacement
- How to do it, [official video](https://www.dell.com/support/contents/en-us/videos/videoplayer/how-to-replace-the-battery-4-cell-on-latitude-5530/6368839521112)
- 
# Goal of This Project
Create a clean laptop environment where:
- **C: drive = system + essential apps only**
- **D: drive = all files, projects, work, downloads, games**
- **WSL/coding workflow is organized and safe**
- Zero clutter on desktop
- Maximum free space on C
- No risk of corrupting Windows or Linux
## 🗂️ Windows Drive Layout (Final Desired State)
### C: Drive (Leave these on C)
- Windows OS
- Program Files / Program Files (x86)
- AppData
- WSL system files
- Drivers
- Browsers (Chrome/Edge/Firefox)
- VS Code
- Microsoft Store apps
- Small utilities (Discord, Zoom, Spotify, 7zip, etc.)
- Python / Node / Java toolchains
- Git
> ⚠️ Do NOT move or reinstall these to D. They rely on system paths or the Windows user profile.
### D: Drive (Everything YOU use goes here)
- Documents
- Desktop contents
- Downloads
- Pictures / Videos / Music
- Coding projects
- Git repos
- Virtual machines
- School work
- Notes
- Games
- Heavy applications that support custom install
- All large files
## 📦 1. Move Personal Folders to D: (Safe + Recommended)
You _cannot_ move your entire user folder,  
but you _can_ relocate each personal folder safely
Move these using: **Right-click folder → Properties → Location → Move → choose D:**
Folders to move:
- Desktop → `D:\Desktop`
- Documents → `D:\Documents`
- Downloads → `D:\Downloads`
- Pictures → `D:\Pictures`
- Videos → `D:\Videos`
- Music → `D:\Music`
> 🟦 After relocation, Windows automatically saves to D: No more C: clutter.
## 🏗️ 2. Create Your Workspace Structure on D:
Recommended folder layout:
```
D:\Workspace     ├── Code     ├── School     ├── Projects     ├── Notes     ├── Media     ├── Backups
```
All your work should live here.
## 🐧 3. WSL + Coding Setup (Correct Procedure)
### Keep WSL **installed on C:**
⚠️ Cannot be moved.  
⚠️ Do NOT store big repos in Linux home directories.
### Instead → Store code on D: and access via WSL:
`cd /mnt/d/Workspace/Code`
All coding/repos stay on D.  
WSL reads them safely and instantly.
Benefits:
- No corruption
- Frees C: space
- Backup is easy
- Cleaner structure
## 🎮 4. Apps: Which Must Stay on C & Which Can Move
### Apps that MUST stay on C (cannot move / safe to keep here)
- Windows OS
- VS Code
- Chrome/Edge/Firefox
- WSL distributions (Ubuntu)
- Git
- Python / Node / Java toolchains
- Microsoft Store apps
- Steam Launcher (the app itself), though _games_ can be moved
- NVIDIA/AMD drivers
- MSI Afterburner
- Virtualization drivers (Docker Desktop engine files stay on C)
### Apps You Can Move or Reinstall on D (Large or Heavy Apps)
**These should be moved or reinstalled to D: to save space:**
- Steam / Epic / Battle.net → Install games to `D:\Games`
- Adobe software
- Unity
- Unreal Engine
- Blender
- Large IDEs (PyCharm, IntelliJ, Android Studio)
- Virtual machines (VMware, VirtualBox images)
- DaVinci Resolve
- Large compilers/SDKs
> How to move?  ❌ You **cannot drag-and-drop the folder.**  
> ✔ You **must uninstall and reinstall** with “Custom Install → D:\Programs”.
### Apps That Can Be Moved Without Reinstall
Some UWP apps allow relocation:
Check: **Settings → Apps → Installed Apps → Click app → Move**
If the Move button appears → you’re good.
## 🔧 5. Fixing Uninstall Issues ("app running")
### If Windows says a folder/app is running:
1. Open Task Manager → **Details** tab
2. Find app.exe → End task
3. If not visible → Open **Resource Monitor → CPU tab**
4. Search app name → End process tree
5. If nothing works → Uninstall in **Safe Mode**
## 🧹 6. C: Drive Cleanup Steps
### Do this after moving folders + reinstalling heavy apps:
- Run **Disk Cleanup (System Files)**
- Delete old installers
- Clear Windows Temp:`%temp%`
- Clear browser cache
- Empty Recycle Bin
- Remove unused OneDrive sync folders
Expected free-up: **20–80 GB** depending on your current clutter.