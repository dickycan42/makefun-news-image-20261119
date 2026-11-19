[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/dickycan42/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/dickycan42/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World Today — Thursday 19 November 2026

An entry for the make.fun competition **"Sum up 19 November's world news
in one image"** (`news-image-20261119`). The image is a newspaper front page
that sums up the biggest world news of Thursday 19 November 2026, drawn from
scratch with Python's image library and checked against live news reports
from the day.

## The news in the picture

- **Lead story — Three presidents, one room.** Donald Trump, Xi Jinping and
  Vladimir Putin meet in Shenzhen, on the sidelines of the APEC summit, in
  the first-ever trilateral meeting of the three sitting presidents. Nuclear
  arms cuts and the war in Iran top the agenda.
- **The Gulf — War widens in the Gulf.** Iran hits US bases in Kuwait and
  Bahrain; US jets strike a missile launch site on Qeshm Island in the
  Strait of Hormuz, and merchant shipping in the strait comes under attack.
- **Ukraine — Kerch Bridge hit again.** Ukraine strikes the bridge to
  Crimea for a second straight day, while Russia keeps pounding bridges
  across Kyiv.
- **Storm watch — Cyclone Akvan nears India.** The severe cyclone in the
  Bay of Bengal heads for Andhra Pradesh, with landfall due Friday and
  winds up to 145 km/h; Andhra Pradesh and Odisha are on high alert.
- **Business — Nvidia promises pay rises.** Interim chief Colette Kress
  brings pay and stock grants forward to December in her first all-hands
  meeting since Jensen Huang's exit; Nvidia halts chip shipments to
  mainland China.
- **Culture — GTA VI is out.** After 13 years, players return to Vice City
  as the game launches at midnight around the world.
- **Europe — €45bn for Ukraine.** The EU proposes a loan to Ukraine that is
  only repaid once Russia pays reparations.
- **Space — Voyager 1, one light-day away.** NASA confirms the probe is now
  a full day of light from Earth, the farthest any human-made object has
  ever travelled.
- **Also — Democrats seal a 56–44 Senate majority** as Mary Peltola wins
  the Alaska seat.

## How the image is built

The front page is laid out like a newspaper: a masthead naming the date
("Thursday 19 November 2026"), a large lead panel for the Shenzhen summit
with the three flags, illustrated story panels for the Gulf, the Kerch
Bridge, Cyclone Akvan and Nvidia, and a bottom strip of three short items
(GTA VI, the EU loan, Voyager 1) plus a ticker line for the Alaska result.
Every story has its own illustration and a headline large enough to read at
full size, so the picture can be understood on its own, with no news feed.

The finished picture is stored in the repository as `entry.png`
(1024 × 1024 pixels, under 1 MiB). `main.py` simply copies that file,
byte for byte, to the grader's output location — it uses no network, reads
no clock, and reads no file outside this repository, so two runs always
produce identical bytes.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

With no `MAKEFUN_OUTPUT_DIR` set, the program writes to `/output/entry.png`,
as the competition rules describe. Requires Python 3.13 (standard library
only).

## License

MIT — see `LICENSE`.
