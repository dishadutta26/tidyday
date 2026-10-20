# Tidy Day

The simplest daily planner. Habits, tasks and appointments sit on one calm timeline.
You install it from a link with no app store needed (it's a PWA). Everything is saved on the phone. No account.

**Live:** https://dishadutta26.github.io/tidyday/

## Plan your day
- **One timeline:** everything in time order, with free hours shown and "Now / Next" at the top.
  If something from earlier is unfinished, it offers to reschedule it.
- **Top 3:** pick the three things that would make the day a win.
- **Add in two steps:** type it, then pick when. Typed shortcuts work, for example
  "Dentist Friday 3pm remind 1 hour before" fills in the date, time, reminder and type.
- **Priority, lists and checklists:** mark items ❗ High, group them into lists (Work, Personal, Family or your own),
  and break a task into ticked steps.
- **Overlap warnings:** if two items clash, it suggests the next free slot.
- **Quick reschedule:** +15 min, +1 hour, next free slot or tomorrow. "Reschedule" fits missed items into free time.
- **Repeats:** daily, weekdays, chosen weekdays, every 2 weeks, every X days, monthly
  (the 31st falls back to the last day of shorter months), last day of the month, and an optional end date.
  You can change the time or skip **just one day** of a repeating item.
- **Search:** titles, notes and checklist steps, filtered by type, status and list.
- **Daily review:** sort yesterday's leftovers. A leftover whose time has passed goes into the next free slot.
- **Undo** after deleting or rescheduling, **duplicate**, and **archive**.
- **Week view**, **Someday** ideas, low-priority **chores**, and a **focus timer** with breaks.

## Build habits (Habits tab)
- All habits are in one place: the daily basics and your own. Turn off any defaults during setup, or archive them later.
- An optional step-by-step **habit plan**, inspired by the four laws of behaviour change in *Atomic Habits*
  by James Clear (not affiliated). It covers identity, a 2-minute start, levels, cues, pairing and rewards,
  plus a "break a bad habit" mode.
- **Flexible schedules:** every day, weekdays, chosen days or "3 times a week".
- **Track amounts:** pages, minutes, reps, km, glasses and more.
- **Busy-day tiny version:** complete level 1 just for today. Each completion records which level you did.
- **Rest days and pause:** neither breaks your streak. Progress counts only scheduled days.
- **Routines:** link a habit to run right after another one.
- **"What got in the way?"** after a missed day: Forgot, No time, Too hard or Not for me. Each gets a specific fix.
- **Weekly reflection:** what worked, what didn't, and one change for next week.
  That change then shows on the Habits tab all week.
- **Goals with milestones:** link habits and tasks to them.

## Reminders, calendar and devices
- Reminders work while the app is open or running in the background. **Phones may pause web apps**, so the Me tab
  shows how many reminders depend on that. "Add to phone calendar" (all items, or one from its edit screen)
  creates calendar alarms that ring even when Tidy Day is closed.
- **Import a calendar file** (.ics from Google, Outlook or Apple Calendar). Repeats are kept and duplicates are skipped.
- **Moving devices:** "Send backup to another device", then Restore on the other one. There's no server, so there's
  no automatic sync. That's what keeps the data private on your phone.

## Files
`index.html` (the whole app), `manifest.webmanifest` (install info), `sw.js` (offline + notification taps), `icons/`.

## Install on a phone
- **Android (Chrome):** open the link and tap **Install app**.
- **iPhone (Safari):** tap Share → **Add to Home Screen**, then open it from the home screen and allow notifications.

## Updating
After changing any file, bump `CACHE` in `sw.js`, then commit and push. GitHub Pages redeploys in about a minute.
