# Church Service Timer - operator handbook

Onboarding and reference guide for Church Service Timer 0.18.0 by I-Proton.

Website: https://kosenuel.github.io/church-service-timer-guide/
Source: [teaching.md](teaching.md).

Includes 17 lessons, example screenshots, troubleshooting, a trainer checklist,
search, reading progress and a printable complete guide.

## Update the guide

Edit teaching.md and approved example images in site/assets/images.
With Python 3.11 or newer, run from this repository:

    python -m pip install --require-hashes -r site/requirements.txt
    python scripts/build-handbook.py --output docs
    python scripts/check-handbook.py docs
    python -m http.server 8841 --directory docs

Review http://localhost:8841, then commit and push source and docs changes.
GitHub Pages publishes the docs folder on main.

Only public teaching material belongs here. Application source remains private.
Do not add passwords, pairing invitations, private notes or device logs.
