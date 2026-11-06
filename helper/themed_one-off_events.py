# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = "zettai_knee_socks"  # ==== 絶対ニーソ ====
    if i not in disabled_events:
        event_name = "zettai_knee_socks"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "zettai_knee_socks_yuri_otome_no_rakuen_ttc09.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC９・制服宣言２・絶対ニーソ・百合乙女の楽園 チラシ絵 朝倉亮 様（水無月亭）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["絶対ニーソ", "Zettai Knee Socks"],
            dates="2018.11.04",
            links=["http://ttc.ninja-web.net/"],
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
                Source(
                    "Joint venue: https://web.archive.org/web/20190408141004/http://ttc.ninja-web.net/nagoya-doujin-fes/circle_list.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source("Alias transliteration: guess", (RT.Guess, OT.Unsourced)),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 (ツインテールカーニバル9, 制服宣言2, 絶対ニーソ and 百合乙女の楽園) joint venue, which also features 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "yuri_otome_no_rakuen"  # ==== 百合乙女の楽園 ====
    if i not in disabled_events:
        event_name = "yuri_otome_no_rakuen"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "zettai_knee_socks_yuri_otome_no_rakuen_ttc09.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC９・制服宣言２・絶対ニーソ・百合乙女の楽園 チラシ絵 朝倉亮 様（水無月亭）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["百合乙女の楽園", "Yuri Otome no Rakuen"],
            dates="2018.11.04",
            links=["http://ttc.ninja-web.net/"],
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
                Source(
                    "Joint venue: https://web.archive.org/web/20190408141004/http://ttc.ninja-web.net/nagoya-doujin-fes/circle_list.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source("Alias transliteration: guess", (RT.Guess, OT.Unsourced)),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 (ツインテールカーニバル9, 制服宣言2, 絶対ニーソ and 百合乙女の楽園) joint venue, which also features 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "lyrical_heart"  # ==== リリカルハート ====
    if i not in disabled_events:
        event_name = "lyrical_heart"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "lyrical_heart_nanoha-heart01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070208135135/http://nanoha-heart.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="リリカルハート チラシ絵 早矢志さくら 様 （ぱるふぇ）",
            ),
            Medium(
                "lyrical_heart_nano-heart01_hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111119213207/http://nanoha-heart.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="（リリカルハート・まきますか？まきませんか？ex 共通カタログ） リリカルハート側 カタログ表紙絵 中村べーた 様 「ロマンティック身体検査」",
            ),
            Medium(
                "lyrical_heart_nano-heart-bn01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111119213207/http://nanoha-heart.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "lyrical_heart_nano-heart-bn.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111119213207/http://nanoha-heart.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "lyrical_heart_nano-maki_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20080609052410/http://nanoha-heart.ket.jp/nanoha-heart_list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.0960914, 136.9241402),
                address="5 Chome-1-16 Higashimatabeecho, Minami Ward, Nagoya, Aichi 457-0833, Japan",
                description="日本ガイシフォーラム　（旧称：名古屋市総合体育館 サン笠寺）",
                sources=[
                    Source(
                        "https://web.archive.org/web/20111119213207/http://nanoha-heart.ket.jp/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmj8MzT8MDc2f6y-m4HKbW409CgcjzT-W5sICqc_6FGCydMMyIdsr37ZfspiGt3FF4_viq4XCwlLXeK4sHeI428n6LGylj2FGApSjctQAT_dR0dwUcv0i9FQt7mKQ5a4YH401m5Ig=s0?imgmax=0",
                url="https://maps.app.goo.gl/UY9XC3cm89b4qD8g7",
            ),
        ]
        event = Event(
            aliases=["リリカルハート", "Lyrical Heart", "Nanoha Heart"],
            dates="2007.06.24",
            links=["http://nanoha-heart.ket.jp/"],
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20111119213207/http://nanoha-heart.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    'Alias "Lyrical Heart": direct transliteration',
                    (RT.Guess, OT.Unsourced),
                ),
                Source(
                    'Date: "Nanoha Heart": from website url', (RT.Guess, OT.Unsourced)
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20080609052410/http://nanoha-heart.ket.jp/nanoha-heart_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with まきますか？まきませんか？ex and 月下の祭典",
            comments="Successor event group: ユニゾンイン",
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "oshiro_matsuri"  # ==== 御城まつり ====
    if i not in disabled_events:
        event_name = "oshiro_matsuri"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "oshiro_matsuri_oshiro.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20240714040747/http://ttc.ninja-web.net/oshiro/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="御城まつり チラシ絵 紗汐冴 様 （おむつスナイパー）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール （名古屋市熱田区）",
                sources=[
                    Source(
                        "https://web.archive.org/web/20240714040747/http://ttc.ninja-web.net/oshiro/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["御城まつり", "Oshiro Matsuri"],
            dates="2018.11.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20240714040747/http://ttc.ninja-web.net/oshiro/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 joint venue, featuring ツインテールカーニバル9, 制服宣言2, 絶対ニーソ, 百合乙女の楽園, 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "tsuki_no_utage"  # ==== 月之宴 ====
    if i not in disabled_events:
        event_name = "tsuki_no_utage"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "tsuki_no_utage_applicate.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="イラスト：桐島りおな(SilverStone)",
            ),
            Medium(
                "tsuki_no_utage_tukinoutage.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "tsuki_no_utage_logo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(34.7355454, 135.4914229),
                address="2 Chome-2-2 Nishimiyahara, Yodogawa Ward, Osaka, 532-0004, Japan",
                description="新大阪センイシティー ２号館 ５階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9TD5ZxYDtclsLXFDQRPoy69FqVPCPqeniwGyAUf3N68_g8q8EWVmd9nhEuvLkTrJ9EKhbYs8247tOzKA_bQx2VOFwcrRrH23KoXweXaxs4_AIxCtaSm4smXLSYOd2jWQDIkwmNLutiJ-zcg=s0?imgmax=0",
                url="https://maps.app.goo.gl/vhxPykERA7vdhLPs7",
            ),
        ]
        event = Event(
            aliases=["月之宴", "Tsuki no Utage"],
            dates="2006.07.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070108151249/http://tukinoutage.com/circlelist.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with August Festival",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "august_festival"  # ==== August Festival ====
    if i not in disabled_events:
        # event_name = f"{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "august_festival_august1.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20051030094047/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "august_festival_hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070202161721/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "august_festival_AFbnr01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20081211011652id_/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "august_festival_AFbnr02.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20081211011652id_/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "august_festival_AFbnr03.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20081211011652id_/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "august_festival_AFbnr04.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20081211011652id_/http://august-fes.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(34.7355454, 135.4914229),
                address="2 Chome-2-2 Nishimiyahara, Yodogawa Ward, Osaka, 532-0004, Japan",
                description="新大阪センイシティ　2号館5階",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070210003520/http://tukinoutage.com/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9TD5ZxYDtclsLXFDQRPoy69FqVPCPqeniwGyAUf3N68_g8q8EWVmd9nhEuvLkTrJ9EKhbYs8247tOzKA_bQx2VOFwcrRrH23KoXweXaxs4_AIxCtaSm4smXLSYOd2jWQDIkwmNLutiJ-zcg=s0?imgmax=0",
                url="https://maps.app.goo.gl/vhxPykERA7vdhLPs7",
            ),
        ]
        event = Event(
            aliases=["August Festival"],
            dates="2006.07.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20051030094047id_/http://august-fes.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20071215114508/http://august-fes.ket.jp/untitled.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 月之宴",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "princess_diary"  # ==== PrincessDiary ====
    if i not in disabled_events:
        event_name = "princess_diary"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "princess_diary_paper01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261103080507/https://mattari-an.net/PD/paper01.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_paper02.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20230923132424/https://mattari-an.net/PD/gallery.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：白苺 様 (WhiteStrawberry)",
            ),
            Medium(
                "princess_diary_paper03.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20230923132424/https://mattari-an.net/PD/gallery.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="表紙絵提供：ナナセミオリ 様 (山猫WeBox)",
            ),
            Medium(
                "princess_diary_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20230923151902/https://mattari-an.net/PD/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20230923151902/https://mattari-an.net/PD/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20230923151902/https://mattari-an.net/PD/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd00.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd01.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd02.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd03.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd04.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd05.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd06.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd07.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd08.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd09.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd10.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd11.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd12.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd13.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd14.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd15.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd16.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd17.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd18.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "princess_diary_bnrpd19.png",
                [
                    Source(
                        "https://web.archive.org/web/20261103232453/https://mattari-an.net/PD/link.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.0960914, 136.9241402),
                address="5 Chome-1-16 Higashimatabeecho, Minami Ward, Nagoya, Aichi 457-0833, Japan",
                description="日本ガイシフォーラム",
                sources=[
                    Source(
                        "https://web.archive.org/web/20090428215325/http://mattari-an.net/PD/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmj8MzT8MDc2f6y-m4HKbW409CgcjzT-W5sICqc_6FGCydMMyIdsr37ZfspiGt3FF4_viq4XCwlLXeK4sHeI428n6LGylj2FGApSjctQAT_dR0dwUcv0i9FQt7mKQ5a4YH401m5Ig=s0?imgmax=0",
                url="https://maps.app.goo.gl/UY9XC3cm89b4qD8g7",
            ),
        ]
        event = Event(
            aliases=["PrincessDiary", "プリンセスダイアリー"],
            dates="2009.06.28",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20090428215325/http://mattari-an.net/PD/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20230923151902/https://mattari-an.net/PD/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.11.03",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ====  ====
    # if i not in disabled_events:
    #     # event_name = f"{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    event_group = EventGroup(
        aliases=[
            "One-off Touhou Project events",
        ],
        events=events,
        media=[],
        links=[],
        sources=[],
        comments=None,
        description="Collection of one-off events with miscellaneous themes.",
        last_edited="2026.10.13",
    )

    # Check for missing media files and unreferenced media files
    media = [m for e in event_group.events for m in e.media or []] + (event_group.media or [])
    for m in media:
        if m.path.startswith(("http://", "https://")):
            continue
        p = PATH_MEDIA / m.path
        if not p.exists():
            print(f"Warning: Medium file not found: {p}")

    referenced = {m.path for m in media}
    for p in PATH_MEDIA.rglob("*"):
        if p.is_file() and p.relative_to(PATH_MEDIA).as_posix() not in referenced:
            print(f"Warning: Media file not referenced in event group: {p}")

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
