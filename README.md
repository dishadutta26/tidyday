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
- **Habits tab:** a step-by-step habit builder, inspired by the four laws of behaviour change in *Atomic Habits*
  by James Clear (not affiliated).
  - Start from who you want to become ("I am someone who keeps a calm, tidy home").
  - Begin with a 2-minute version and grow through up to 4 levels. The app suggests levelling up after
    14 strong days, and stepping back when a level feels too heavy.
  - Plan when and where, stacked on an existing habit ("After I finish dinner, I will…"), with a visual cue.
    Pair it with something you enjoy, and pick a small reward.
  - Break bad habits with the reverse: make it invisible, unattractive, difficult and unsatisfying.
  - Press and hold to complete, then see your streak, best streak, a 12-week grid and a "never miss twice" nudge.
  - Ready-made plans: tidy home, grow tech skills, reading, fitness, sleep, calm, journaling, money,
    less phone and less junk food. There's also a daily tip.
- **Week view:** see the whole week at a glance (link under the day strip on Today).
- **Daily review:** sort yesterday's unfinished tasks into Today, Tomorrow or Someday, or drop them.
- **Focus timer:** Pomodoro (25/5), Quick, Deep work or Long, with breaks built in.
- **Reminders:** at start or minutes, hours or a day before, with gentle sounds. There's also a "what's left"
  check-in every few hours.
- **When you have time:** low-priority chores that come back weekly or monthly.
- **Someday:** a place to jot ideas and give them a day later.
- **Easy on the eyes:** a readability-first palette (all text passes WCAG AA, body text about 14:1). Light mode has a soft grey page with near-black text; dark mode is dark grey (not pure black) with off-white text. There are 4 accent colours, plus icons and colours per item.
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
