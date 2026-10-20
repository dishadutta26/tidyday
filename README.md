# DayBoost

A daily planner you install from a link, with no app store needed. It's a PWA (Progressive Web App).
All data stays in the phone's browser storage. Nothing is uploaded.

## Files
- `index.html`: the whole app (UI, logic, reminders)
- `manifest.webmanifest`: makes it installable (name, icon, colours)
- `sw.js`: service worker for offline use and notification taps
- `icons/`: app icons

## Put it online (free, needs HTTPS)
Installing only works over HTTPS, so host the `dayboost` folder on any static host:

**Netlify Drop (easiest, no setup):** go to https://app.netlify.com/drop and drag the `dayboost` folder in. You get a link like `https://something.netlify.app`.

**GitHub Pages:** push the folder to a repo, then go to Settings → Pages → Deploy from branch.

## Install on a phone
- **Android (Chrome):** open the link and tap **Install app** in the banner, or use menu ⋮ → Install app.
- **iPhone (Safari):** open the link, tap Share → **Add to Home Screen**, then open it from the home screen and allow notifications (iOS 16.4+).

## Run locally
```
python3 -m http.server 5173 --directory dayboost
```

## Updating
After changing any file, bump `CACHE` in `sw.js` (e.g. `dayboost-v2`) so installed phones pick up the new version.

## About reminders
Websites can't schedule alarms while fully closed, so reminders fire while the app is open or still
running in the background. For alarms that always ring, use **Me → Add reminders to phone calendar**.
It exports your habit reminders (daily) and appointments as a calendar file with alerts.
