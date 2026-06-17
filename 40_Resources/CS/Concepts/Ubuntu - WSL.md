---
type: concept
course: BOOM
status: sprout
mastery (1/10): 0
created:
topics: []
related:
  - "[[40_Resources/CS/Links|Links]]"
---
# Ubuntu (WSL) - Linux
## MOC
- [[W__ L__ - ...]]
- [[HW__ - ...]]
## Definition
- 
## Storage
- How to view Linux files in Explorer: 
	- In File Explorer address bar, type: `\\wsl$\Ubuntu\home\anant_gupta\projects`
	- That is the “bridge” to your WSL filesystem.
- Just `\\wsl$` will give the entire linux environment.
- - WSL2 runs Linux on a virtual disk (ext4) stored as a file: 
	- Your Linux files live inside: `D:\WSL\Ubuntu\ext4.vhdx`
	- So `/home/anant_gupta` is inside that VHDX, not inside `C:\home`.
## Run
- Use `wsl ~` to open in the most basic directory.
	- Just `wsl` will open the file director inside c folder cause that's where the root got installed but everything is run on d drive now.
- 
## Resources
- 
## How to use them
1. 
2. 
3. 
## Common mistakes
## Flashcards (best 3–8)

