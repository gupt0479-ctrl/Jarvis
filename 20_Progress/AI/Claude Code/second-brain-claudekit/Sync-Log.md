2026-07-30 12:41:14 +0400  TRANSFER ERRORS  exit=2
```
Warning: No archive files were found for these roots, whose canonical names are:
	/home/anant_gupta/projects/ai/claude/second-brain-claudekit
	/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
This can happen either
because this is the first time you have synchronized these roots, 
or because you have upgraded Unison to a new version with a different
archive format.  

Update detection may take a while on this run if the replicas are 
large.

Unison will assume that the 'last synchronized state' of both replicas
was completely empty.  This means that any files that are different
will be reported as conflicts, and any files that exist only on one
replica will be judged as new and propagated to the other replica.
If the two replicas are identical, then no changes will be reported.

If you see this message repeatedly, it may be because one of your machines
is getting its address from DHCP, which is causing its host name to change
between synchronizations.  See the documentation for the UNISONLOCALHOSTNAME
environment variable for advice on how to correct this.


dir      ---->            .claude/agents  
dir      ---->            .claude/commands  
dir      ---->            .claude/hooks  
file     ---->            .claude/settings.json  
file     ---->            CLAUDE.md  
[BGN] Copying .claude/agents from /home/anant_gupta/projects/ai/claude/second-brain-claudekit to /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
Failed [.claude/agents]: Failed to set permissions of file /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit/.claude to rwxr-xr-x: the permissions was set to rwxrwxrwx instead. The filesystem probably does not support all permission bits. If this is a FAT filesystem, you should set the "fat" option to true. Otherwise, you should probably set the "perms" option to 0o1755 (or to 0 if you don't need to synchronize permissions).
[BGN] Copying .claude/commands from /home/anant_gupta/projects/ai/claude/second-brain-claudekit to /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
Failed [.claude/commands]: Failed to set permissions of file /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit/.claude/.unison.commands.581106b2917358e73c9036f678424717.unison.tmp to rwxr-xr-x: the permissions was set to rwxrwxrwx instead. The filesystem probably does not support all permission bits. If this is a FAT filesystem, you should set the "fat" option to true. Otherwise, you should probably set the "perms" option to 0o1755 (or to 0 if you don't need to synchronize permissions).
[BGN] Copying .claude/hooks from /home/anant_gupta/projects/ai/claude/second-brain-claudekit to /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
Failed [.claude/hooks]: Failed to set permissions of file /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit/.claude/.unison.hooks.581106b2917358e73c9036f678424717.unison.tmp to rwxr-xr-x: the permissions was set to rwxrwxrwx instead. The filesystem probably does not support all permission bits. If this is a FAT filesystem, you should set the "fat" option to true. Otherwise, you should probably set the "perms" option to 0o1755 (or to 0 if you don't need to synchronize permissions).
[BGN] Copying .claude/settings.json from /home/anant_gupta/projects/ai/claude/second-brain-claudekit to /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
Failed [.claude/settings.json]: Failed to set permissions of file /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit/.claude/.unison.settings.json.581106b2917358e73c9036f678424717.unison.tmp to rw-r--r--: the permissions was set to rwxrwxrwx instead. The filesystem probably does not support all permission bits. If this is a FAT filesystem, you should set the "fat" option to true. Otherwise, you should probably set the "perms" option to 0o1644 (or to 0 if you don't need to synchronize permissions).
[BGN] Copying CLAUDE.md from /home/anant_gupta/projects/ai/claude/second-brain-claudekit to /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit
Failed [CLAUDE.md]: Failed to set permissions of file /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/AI/Claude Code/second-brain-claudekit/.unison.CLAUDE.md.581106b2917358e73c9036f678424717.unison.tmp to rw-r--r--: the permissions was set to rwxrwxrwx instead. The filesystem probably does not support all permission bits. If this is a FAT filesystem, you should set the "fat" option to true. Otherwise, you should probably set the "perms" option to 0o1644 (or to 0 if you don't need to synchronize permissions).
Synchronization incomplete at 12:41:15  (0 items transferred, 0 skipped, 5 failed)
  failed: .claude/agents
  failed: .claude/commands
  failed: .claude/hooks
  failed: .claude/settings.json
  failed: CLAUDE.md
```
2026-07-30 12:41:52 +0400  OK  exit=0
2026-07-30 12:44:04 +0400  OK  exit=0
2026-07-30 12:44:31 +0400  OK  exit=0
2026-07-30 12:44:47 +0400  CONFLICTS (skipped, see below)  exit=1
```
changed  <-?-> changed    .claude/commands/today.md  
No updates to propagate
Synchronization complete at 12:44:48  (0 items transferred, 1 skipped, 0 failed)
  skipped: .claude/commands/today.md (contents changed on both sides)
```
2026-07-30 12:45:27 +0400  OK  exit=0
2026-07-30 12:49:04 +0400  OK  exit=0
2026-07-30 14:05:01 +0400  OK  exit=0
2026-07-30 14:20:01 +0400  OK  exit=0
2026-07-30 14:35:01 +0400  OK  exit=0
2026-07-30 14:50:01 +0400  OK  exit=0
2026-07-30 15:05:02 +0400  OK  exit=0
2026-07-30 15:20:02 +0400  OK  exit=0
2026-07-30 15:35:01 +0400  OK  exit=0
2026-07-30 15:50:01 +0400  OK  exit=0
2026-07-30 16:05:01 +0400  OK  exit=0
2026-07-30 16:20:01 +0400  OK  exit=0
2026-07-30 16:35:01 +0400  OK  exit=0
2026-07-30 16:50:02 +0400  OK  exit=0
2026-07-30 17:05:01 +0400  OK  exit=0
2026-07-30 17:20:01 +0400  OK  exit=0
2026-07-30 17:35:01 +0400  OK  exit=0
2026-07-30 17:50:02 +0400  OK  exit=0
2026-07-30 18:05:02 +0400  OK  exit=0
2026-07-30 18:20:02 +0400  OK  exit=0
2026-07-30 18:35:02 +0400  OK  exit=0
2026-07-30 18:50:02 +0400  OK  exit=0
2026-07-30 19:05:03 +0400  OK  exit=0
2026-07-30 19:20:01 +0400  OK  exit=0
2026-07-30 19:22:21 +0400  OK  exit=0
2026-07-30 19:35:00 +0400  OK  exit=0
2026-07-30 19:50:00 +0400  OK  exit=0
2026-07-30 20:05:00 +0400  OK  exit=0
2026-07-30 20:20:00 +0400  OK  exit=0
2026-07-30 20:35:00 +0400  OK  exit=0
2026-07-30 20:50:00 +0400  OK  exit=0
2026-07-30 21:05:00 +0400  OK  exit=0
2026-07-30 21:20:00 +0400  OK  exit=0
2026-07-30 21:35:00 +0400  OK  exit=0
2026-07-30 21:50:00 +0400  OK  exit=0
2026-07-30 22:05:01 +0400  OK  exit=0
2026-07-30 22:20:00 +0400  OK  exit=0
2026-07-30 22:35:01 +0400  OK  exit=0
2026-07-30 22:50:02 +0400  OK  exit=0
2026-07-30 23:05:02 +0400  OK  exit=0
2026-07-30 23:20:02 +0400  OK  exit=0
2026-07-30 23:35:02 +0400  OK  exit=0
2026-07-30 23:50:02 +0400  OK  exit=0
2026-07-31 00:05:01 +0400  OK  exit=0
2026-07-31 00:20:01 +0400  OK  exit=0
2026-07-31 00:35:01 +0400  OK  exit=0
2026-07-31 00:50:01 +0400  OK  exit=0
2026-07-31 01:05:01 +0400  OK  exit=0
2026-07-31 01:20:02 +0400  OK  exit=0
2026-07-31 01:35:02 +0400  OK  exit=0
2026-07-31 01:50:04 +0400  OK  exit=0
2026-07-31 02:05:03 +0400  OK  exit=0
2026-07-31 02:20:04 +0400  OK  exit=0
2026-07-31 02:35:03 +0400  OK  exit=0
2026-07-31 02:50:04 +0400  OK  exit=0
2026-07-31 03:05:04 +0400  OK  exit=0
2026-07-31 12:05:23 +0400  OK  exit=0
2026-07-31 12:20:07 +0400  OK  exit=0
2026-07-31 12:35:03 +0400  OK  exit=0
2026-07-31 18:21:59 +0400  SKIPPED  another sync is already running
2026-07-31 18:21:59 +0400  OK  exit=0
2026-07-31 18:35:06 +0400  OK  exit=0
2026-07-31 18:50:03 +0400  OK  exit=0
2026-07-31 19:05:03 +0400  OK  exit=0
2026-07-31 19:19:59 +0400  OK  exit=0
2026-07-31 19:34:58 +0400  OK  exit=0
2026-07-31 19:49:58 +0400  OK  exit=0
2026-07-31 20:54:07 +0400  OK  exit=0
2026-07-31 21:05:00 +0400  OK  exit=0
2026-07-31 21:20:01 +0400  OK  exit=0
2026-07-31 21:35:01 +0400  OK  exit=0
2026-07-31 21:50:01 +0400  OK  exit=0
2026-07-31 22:05:01 +0400  OK  exit=0
2026-07-31 23:36:19 +0400  OK  exit=0
2026-07-31 23:51:03 +0400  OK  exit=0
2026-08-01 00:06:04 +0400  OK  exit=0
2026-08-01 00:21:03 +0400  OK  exit=0
2026-08-01 00:36:03 +0400  OK  exit=0
2026-08-01 00:51:03 +0400  OK  exit=0
2026-08-01 01:06:03 +0400  OK  exit=0
2026-08-01 01:21:03 +0400  OK  exit=0
2026-08-01 01:36:03 +0400  OK  exit=0
2026-08-01 01:51:03 +0400  OK  exit=0
2026-08-01 02:05:27 +0400  OK  exit=0
2026-08-01 09:59:33 +0400  OK  exit=0
2026-08-01 10:06:03 +0400  OK  exit=0
2026-08-01 10:21:03 +0400  OK  exit=0
2026-08-01 10:32:02 +0400  OK  exit=0
2026-08-01 10:51:02 +0400  OK  exit=0
2026-08-01 11:06:03 +0400  OK  exit=0
2026-08-01 11:21:03 +0400  OK  exit=0
2026-08-01 11:36:05 +0400  OK  exit=0
2026-08-01 11:51:05 +0400  OK  exit=0
2026-08-01 12:06:03 +0400  OK  exit=0
2026-08-01 12:21:03 +0400  OK  exit=0
2026-08-01 12:36:08 +0400  OK  exit=0
2026-08-01 12:51:07 +0400  OK  exit=0
2026-08-01 13:06:03 +0400  OK  exit=0
2026-08-01 13:21:02 +0400  OK  exit=0
2026-08-01 13:36:02 +0400  OK  exit=0
2026-08-02 01:40:30 +0400  OK  exit=0
2026-08-02 01:43:03 +0400  OK  exit=0
2026-08-02 12:10:29 +0400  OK  exit=0
2026-08-02 12:25:29 +0400  OK  exit=0
2026-08-02 16:51:23 +0400  OK  exit=0
2026-08-02 22:25:30 +0400  OK  exit=0
2026-08-02 22:35:01 +0400  OK  exit=0
2026-08-02 22:40:30 +0400  OK  exit=0
2026-08-03 06:24:05 +0400  OK  exit=0
2026-08-03 08:00:12 +0400  OK  exit=0
2026-08-03 08:05:02 +0400  OK  exit=0
2026-08-03 08:20:02 +0400  OK  exit=0
2026-08-03 08:35:02 +0400  OK  exit=0
2026-08-03 09:21:10 +0400  OK  exit=0
2026-08-03 09:35:02 +0400  OK  exit=0
2026-08-03 09:50:02 +0400  OK  exit=0
2026-08-03 10:09:09 +0400  OK  exit=0
2026-08-03 10:20:02 +0400  OK  exit=0
2026-08-03 10:35:02 +0400  OK  exit=0
2026-08-03 10:39:45 +0400  OK  exit=0
2026-08-03 11:35:02 +0400  OK  exit=0
2026-08-03 11:50:02 +0400  OK  exit=0
2026-08-03 12:05:02 +0400  OK  exit=0
2026-08-03 12:20:02 +0400  OK  exit=0
2026-08-03 12:35:05 +0400  OK  exit=0
2026-08-03 12:50:02 +0400  OK  exit=0
2026-08-03 13:05:02 +0400  OK  exit=0
2026-08-03 13:20:02 +0400  OK  exit=0
2026-08-03 13:35:02 +0400  OK  exit=0
2026-08-03 13:50:02 +0400  OK  exit=0
2026-08-03 14:05:02 +0400  OK  exit=0
2026-08-03 14:20:02 +0400  OK  exit=0
2026-08-03 14:35:02 +0400  OK  exit=0
2026-08-03 14:50:02 +0400  OK  exit=0
2026-08-03 15:10:40 +0400  OK  exit=0
2026-08-03 15:25:45 +0400  OK  exit=0
2026-08-03 15:35:32 +0400  OK  exit=0
2026-08-03 15:50:05 +0400  OK  exit=0
2026-08-03 16:05:02 +0400  OK  exit=0
2026-08-03 20:40:19 +0400  OK  exit=0
2026-08-03 20:50:02 +0400  OK  exit=0
2026-08-03 21:05:01 +0400  OK  exit=0
2026-08-03 21:20:02 +0400  OK  exit=0
2026-08-03 23:02:47 +0400  OK  exit=0
2026-08-04 04:15:39 +0400  OK  exit=0
2026-08-04 04:17:39 +0400  OK  exit=0
2026-08-04 09:29:32 +0400  OK  exit=0
2026-08-04 09:32:39 +0400  OK  exit=0
2026-08-04 09:47:40 +0400  OK  exit=0
2026-08-04 11:02:03 +0400  OK  exit=0
2026-08-04 11:02:54 +0400  OK  exit=0
2026-08-04 11:17:40 +0400  OK  exit=0
2026-08-04 11:33:20 +0400  OK  exit=0
2026-08-04 11:47:42 +0400  OK  exit=0
2026-08-04 12:02:41 +0400  OK  exit=0
2026-08-04 12:45:45 +0400  OK  exit=0
2026-08-04 12:47:43 +0400  OK  exit=0
2026-08-04 13:02:41 +0400  OK  exit=0
2026-08-04 13:17:45 +0400  OK  exit=0
2026-08-04 13:32:43 +0400  OK  exit=0
2026-08-04 18:52:32 +0400  OK  exit=0
2026-08-04 18:52:34 +0400  OK  exit=0
2026-08-04 19:02:42 +0400  OK  exit=0
2026-08-04 19:17:40 +0400  OK  exit=0
2026-08-04 19:23:11 +0400  OK  exit=0
2026-08-04 19:47:40 +0400  OK  exit=0
2026-08-04 20:02:39 +0400  OK  exit=0
2026-08-04 21:17:04 +0400  OK  exit=0
2026-08-04 21:17:42 +0400  OK  exit=0
2026-08-04 21:35:56 +0400  OK  exit=0
2026-08-04 21:47:40 +0400  OK  exit=0
2026-08-05 19:37:17 +0400  OK  exit=0
2026-08-05 19:50:30 +0400  OK  exit=0
2026-08-05 20:05:29 +0400  OK  exit=0
2026-08-05 20:20:23 +0400  OK  exit=0
2026-08-05 20:35:31 +0400  OK  exit=0
2026-08-05 20:50:52 +0400  OK  exit=0
2026-08-06 08:22:07 +0400  OK  exit=0
2026-08-06 08:37:55 +0400  OK  exit=0
2026-08-06 08:50:25 +0400  OK  exit=0
2026-08-06 08:50:56 +0400  OK  exit=0
2026-08-06 09:06:55 +0400  OK  exit=0
2026-08-06 09:20:24 +0400  OK  exit=0
2026-08-06 09:20:56 +0400  OK  exit=0
2026-08-06 09:35:23 +0400  OK  exit=0
2026-08-06 09:35:56 +0400  OK  exit=0
2026-08-06 09:59:19 +0400  OK  exit=0
2026-08-06 10:05:37 +0400  OK  exit=0
2026-08-06 10:06:24 +0400  OK  exit=0
2026-08-06 10:20:27 +0400  OK  exit=0
2026-08-06 10:21:03 +0400  OK  exit=0
2026-08-06 10:35:24 +0400  OK  exit=0
2026-08-06 10:35:56 +0400  OK  exit=0
2026-08-06 10:50:26 +0400  OK  exit=0
2026-08-06 10:50:57 +0400  OK  exit=0
2026-08-06 11:14:47 +0400  OK  exit=0
2026-08-06 11:20:26 +0400  OK  exit=0
2026-08-06 11:21:03 +0400  OK  exit=0
2026-08-06 11:37:08 +0400  OK  exit=0
2026-08-06 11:50:26 +0400  OK  exit=0
2026-08-06 11:50:58 +0400  OK  exit=0
2026-08-06 16:31:29 +0400  OK  exit=0
2026-08-06 16:31:36 +0400  OK  exit=0
2026-08-09 00:39:04 +0400  OK  exit=0
2026-08-09 00:50:00 +0400  OK  exit=0
2026-08-09 09:37:53 +0400  OK  exit=0
2026-08-09 09:50:01 +0400  OK  exit=0
2026-08-09 10:05:01 +0400  OK  exit=0
2026-08-09 10:20:00 +0400  OK  exit=0
2026-08-09 10:35:00 +0400  OK  exit=0
2026-08-09 10:50:01 +0400  OK  exit=0
2026-08-09 11:05:00 +0400  OK  exit=0
2026-08-09 11:20:00 +0400  OK  exit=0
2026-08-09 11:35:00 +0400  OK  exit=0
2026-08-09 11:50:01 +0400  OK  exit=0
2026-08-09 12:05:00 +0400  OK  exit=0
2026-08-09 12:20:00 +0400  OK  exit=0
2026-08-09 12:35:00 +0400  OK  exit=0
2026-08-09 12:50:01 +0400  OK  exit=0
2026-08-09 13:05:00 +0400  OK  exit=0
2026-08-09 13:20:01 +0400  OK  exit=0
2026-08-09 13:35:00 +0400  OK  exit=0
2026-08-09 13:50:00 +0400  OK  exit=0
2026-08-09 14:05:02 +0400  OK  exit=0
2026-08-09 14:20:00 +0400  OK  exit=0
2026-08-09 14:35:00 +0400  OK  exit=0
2026-08-09 14:50:01 +0400  OK  exit=0
2026-08-09 15:00:22 +0400  OK  exit=0
2026-08-09 18:35:00 +0400  OK  exit=0
2026-08-09 18:50:00 +0400  OK  exit=0
2026-08-09 19:05:00 +0400  OK  exit=0
2026-08-09 19:20:00 +0400  OK  exit=0
2026-08-09 19:35:00 +0400  OK  exit=0
2026-08-09 19:50:00 +0400  OK  exit=0
2026-08-09 20:05:00 +0400  OK  exit=0
2026-08-09 20:20:00 +0400  OK  exit=0
2026-08-09 20:35:00 +0400  OK  exit=0
2026-08-09 20:50:00 +0400  OK  exit=0
2026-08-09 21:05:00 +0400  OK  exit=0
2026-08-09 21:20:02 +0400  OK  exit=0
2026-08-09 21:35:00 +0400  OK  exit=0
2026-08-09 21:50:00 +0400  OK  exit=0
2026-08-09 22:05:00 +0400  OK  exit=0
2026-08-09 22:20:00 +0400  OK  exit=0
2026-08-09 23:14:40 +0400  OK  exit=0
2026-08-09 23:29:37 +0400  OK  exit=0
2026-08-09 23:44:39 +0400  OK  exit=0
2026-08-10 08:21:00 +0400  OK  exit=0
2026-08-10 08:29:38 +0400  OK  exit=0
2026-08-10 08:44:36 +0400  OK  exit=0
2026-08-10 08:59:36 +0400  OK  exit=0
2026-08-10 09:14:36 +0400  OK  exit=0
2026-08-10 09:23:53 +0400  OK  exit=0
2026-08-10 09:59:36 +0400  OK  exit=0
2026-08-10 10:14:36 +0400  OK  exit=0
2026-08-10 10:29:36 +0400  OK  exit=0
2026-08-10 10:44:36 +0400  OK  exit=0
2026-08-10 10:59:36 +0400  OK  exit=0
2026-08-10 11:14:36 +0400  OK  exit=0
2026-08-10 11:29:36 +0400  OK  exit=0
2026-08-10 11:44:36 +0400  OK  exit=0
2026-08-10 11:59:36 +0400  OK  exit=0
2026-08-10 12:14:36 +0400  OK  exit=0
2026-08-10 12:29:36 +0400  OK  exit=0
2026-08-10 12:44:36 +0400  OK  exit=0
2026-08-10 12:59:36 +0400  OK  exit=0
2026-08-10 13:14:36 +0400  OK  exit=0
2026-08-10 13:29:36 +0400  OK  exit=0
2026-08-10 13:44:37 +0400  OK  exit=0
2026-08-10 13:59:37 +0400  OK  exit=0
2026-08-10 14:14:40 +0400  OK  exit=0
2026-08-10 14:17:43 +0400  OK  exit=0
2026-08-10 14:17:55 +0400  OK  exit=0
2026-08-10 14:19:48 +0400  OK  exit=0
2026-08-10 14:34:35 +0400  OK  exit=0
2026-08-10 14:48:28 +0400  OK  exit=0
2026-08-10 14:49:36 +0400  OK  exit=0
2026-08-10 14:55:15 +0400  OK  exit=0
2026-08-10 15:04:34 +0400  OK  exit=0
2026-08-10 17:48:20 +0400  OK  exit=0
2026-08-10 17:49:35 +0400  OK  exit=0
2026-08-10 18:04:35 +0400  OK  exit=0
2026-08-10 18:19:34 +0400  OK  exit=0
2026-08-10 18:33:42 +0400  OK  exit=0
2026-08-10 18:34:36 +0400  OK  exit=0
2026-08-10 18:49:35 +0400  OK  exit=0
2026-08-10 19:04:35 +0400  OK  exit=0
2026-08-10 19:19:35 +0400  OK  exit=0
2026-08-10 19:34:34 +0400  OK  exit=0
2026-08-10 19:53:14 +0400  OK  exit=0
