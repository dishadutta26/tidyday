# Tidy Day

The simplest daily planner. Habits, tasks and appointments sit on one calm timeline.
You install it from a link with no app store needed (it's a PWA). Everything is saved on the phone.

**Live:** https://dishadutta26.github.io/tidyday/

## What it does
- **One timeline:** everything for the day in time order, with "Now / Next" at the top and your free hours shown.
- **Daily non-negotiables:** water (counts glasses), workout, cardio, self-care, protein, fruit, quiet time,
  connecting with someone, and planning tomorrow. Each has a time and an optional reminder.
- **Add in two steps:** type it, then pick when. Repeat, length, reminders and colour are under "More options".
- **Repeating items:** daily, weekdays, weekly (pick days) or monthly.
- **Week view:** see the whole week at a glance.
- **Daily review:** sort yesterday's unfinished tasks into Today, Tomorrow or Someday, or drop them.
- **Focus timer:** Pomodoro (25/5), Quick, Deep work or Long, with breaks built in.
- **Reminders:** at start or minutes, hours or a day before, with gentle sounds. There's also a "what's left"
  check-in every few hours.
- **When you have time:** low-priority chores that come back weekly or monthly.
- **Someday:** a place to jot ideas and give them a day later.
- **Look:** a soft cream-and-sage palette, light and dark themes, 4 accent colours, and icons and colours per item.
- **Private:** no account. You can back up or restore from a file, and export to your phone's calendar.

## Files
`index.html` (the whole app), `manifest.webmanifest` (install info), `sw.js` (offline + notification taps), `icons/`.

## Install on a phone
- **Android (Chrome):** open the link and tap **Install app**.
- **iPhone (Safari):** tap Share → **Add to Home Screen**, then open it from the home screen and allow notifications.

## Updating
After changing any file, bump `CACHE` in `sw.js` so installed phones pick up the new version, then commit and push.
GitHub Pages redeploys in about a minute.

## About reminders
A website can't ring alarms while it's fully closed. Reminders fire while the app is open or running in the background.
For alarms that always ring, use **Me → Add to phone calendar**.
