# ainvest manage_tracking Snapshot Overview

- Environment: `ainvest`
- Generated at: `2026-05-11T13:50:00+08:00`
- Source directory: `/Users/zyhjr/Downloads`

| Metric | Value |
| --- | --- |
| Apps | 23 |
| Pages | 1279 |
| Sections | 1690 |
| Elements | 2801 |
| Tracks | 13500 |
| Relation rows | 29301 |
| Non-self relation edges | 27878 |
| Unique non-self relation edges | 27878 |
| Tracks with relation coverage | 4096 / 13498 |

## Source Files

| Group | File | Exists | Rows | SHA256 prefix |
| --- | --- | --- | --- | --- |
| apps | app_info.csv | yes | 23 | 8baa6fc08bba0db6 |
| pages | page_info.csv | yes | 1279 | 5f3c800bc0926873 |
| pages | page_info1.csv | no | - | - |
| pages | page_info2.csv | yes | 1279 | 5f3c800bc0926873 |
| sections | qk1.csv | yes | 1690 | d026bf7b7ee2d3c6 |
| sections | qk2.csv | yes | 1690 | d026bf7b7ee2d3c6 |
| elements | ys1.csv | yes | 2801 | bbed28e8686a32f1 |
| elements | ys2.csv | yes | 2801 | bbed28e8686a32f1 |
| elements | ys3.csv | yes | 2801 | bbed28e8686a32f1 |
| tracks | track_info.csv | yes | 13500 | 91b462e8b039d4af |
| relations | track_info_realtion.csv | yes | 29301 | 96133fb9fb1a0992 |

## Notes

- `page_info2.csv` is byte-identical to `page_info.csv`; `page_info1.csv` was not present.
- `qk2.csv` is byte-identical to `qk1.csv`.
- `ys2.csv` and `ys3.csv` are byte-identical to `ys1.csv`.
- The relation file is interpreted as `from_stat_id` -> `stat_id`, where `from_stat_id` is the previous track key and `stat_id` is the current track key.
